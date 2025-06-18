# Wan2.1-T2V-1.3B 轻量版文生视频模型部署指南

## 模型简介

Wan2.1-T2V-1.3B 是 WanVideo 2.1 系列的轻量版文本到视频生成模型，专为资源受限环境设计。该模型在保持良好视频生成质量的同时，显著降低了硬件要求，使得更多用户能够在消费级设备上体验文生视频技术。

### 核心特性
- **轻量化设计**: 仅1.3B参数，相比14B版本大幅降低资源需求
- **高效生成**: 优化的推理速度，适合实时和批量生成
- **低显存需求**: 6GB显存即可运行，兼容更多设备
- **质量保证**: 在轻量化的同时保持良好的视频生成质量
- **多语言支持**: 支持中文和英文文本提示
- **灵活部署**: 支持单机和集群部署方式
- **开源友好**: 完全开源，支持二次开发和定制

### 技术规格
- **模型类型**: 文本到视频生成（Text-to-Video）
- **参数规模**: 1.3B参数
- **量化方式**: FP8量化版本
- **部署架构**: ACS集群部署
- **支持分辨率（480P）**:
    - 480×832
    - 832×480
- **最大帧数**: 81帧
- **推荐帧率**: 16fps
- **推荐步数**: 15-25步

### 与14B版本对比
- **参数规模**: 1.3B vs 14B（约10倍差异）
- **显存需求**: 6GB+ vs 12GB+
- **推理速度**: 更快的生成速度
- **生成质量**: 略低但仍保持良好水准
- **适用场景**: 更适合快速原型和批量生成

## 部署架构

### 方式一：ACS集群部署（推荐）

#### 系统配置
- **显存**: ppu
- **内存**: 96GB

### 方式二：ECS部署
- **显存**: A10等
- **内存**: 30GB


## 使用指南

### ComfyUI使用

1. **访问界面**: 单击"查看Web应用"打开UI界面
2. 选择工作流
3. 其中模型选择，
3. **设置参数**:
    - 输入文本描述（支持中英文）
    - 设置视频分辨率和帧数
    - 调整生成参数（步数、CFG等）
3. **快速生成**: 点击"Generate"按钮
4. **下载结果**: 生成完成后下载视频文件

### ComfyUI API调用示例
点击右上方按钮，打开底部面板，获取token：![img_1.png](img_1.png)
COMFYUI_SERVER的获取可参考：![img_2.png](img_2.png)
```python
import requests, json, uuid, time, random

# 配置参数
COMFYUI_SERVER, COMFYUI_TOKEN = "输入您的服务器地址", "输入您的token"
T5_MODEL, VIDEO_MODEL, VAE_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors", "wan2.1/Wan2_1-T2V-1_3B_fp8_e4m3fn.safetensors", "wan2.1/Wan2_1_VAE_bf16.safetensors"

class ComfyUIClient:
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url, self.token, self.client_id = f"http://{server}", token, str(uuid.uuid4())
        self.headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})}

    def generate(self, prompt, neg_prompt="", steps=15, cfg=6, width=832, height=480, frames=81):
        workflow = {
            "1": {"inputs": {"model_name": T5_MODEL, "precision": "bf16"}, "class_type": "LoadWanVideoT5TextEncoder"},
            "2": {"inputs": {"positive_prompt": prompt, "negative_prompt": neg_prompt, "force_offload": True, "t5": ["1", 0]}, "class_type": "WanVideoTextEncode"},
            "3": {"inputs": {"model": VIDEO_MODEL, "base_precision": "bf16", "quantization": "fp8_e4m3fn", "load_device": "offload_device"}, "class_type": "WanVideoModelLoader"},
            "4": {"inputs": {"width": width, "height": height, "num_frames": frames}, "class_type": "WanVideoEmptyEmbeds"},
            "5": {"inputs": {"model_name": VAE_MODEL, "precision": "bf16"}, "class_type": "WanVideoVAELoader"},
            "6": {"inputs": {"steps": steps, "cfg": cfg, "shift": 5, "seed": random.randint(1, 1000000), "force_offload": True, "scheduler": "dpm++", "riflex_freq_index": 0, "model": ["3", 0], "text_embeds": ["2", 0], "image_embeds": ["4", 0]}, "class_type": "WanVideoSampler"},
            "7": {"inputs": {"enable_vae_tiling": True, "tile_x": 272, "tile_y": 272, "tile_stride_x": 144, "tile_stride_y": 128, "vae": ["5", 0], "samples": ["6", 0]}, "class_type": "WanVideoDecode"},
            "8": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "generated_video", "format": "video/h264-mp4", "save_output": True, "pingpong": False, "images": ["7", 0]}, "class_type": "VHS_VideoCombine"}
        }
        response = requests.post(f"{self.base_url}/prompt", headers=self.headers, json={"prompt": workflow, "client_id": self.client_id})
        print(f"API Response: {response.text}")
        result = response.json()
        if "error" in result: raise Exception(f"Workflow error: {result['error']}")
        if "prompt_id" not in result: raise Exception(f"No prompt_id in response: {result}")
        return result["prompt_id"]

    def get_status(self, task_id):
        try:
            queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])): return "processing"
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])): return "pending"
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            return "completed" if history_response.status_code == 200 and task_id in history_response.json() else "processing"
        except: return "processing"

    def download_video(self, task_id, output_path="generated_video.mp4"):
        try:
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            if task_id in history:
                for output in history[task_id]['outputs'].values():
                    if 'gifs' in output:
                        filename = output['gifs'][0]['filename']
                        video_response = requests.get(f"{self.base_url}/view?filename={filename}", headers=self.headers)
                        with open(output_path, "wb") as f: f.write(video_response.content)
                        return output_path
        except Exception as e: print(f"Download error: {e}")
        return None

def main():
    client = ComfyUIClient()
    try:
        print("🎬 开始文生视频任务...")
        task_id = client.generate("A beautiful anime girl with long black hair dancing gracefully", "low quality, blurry, distorted", 15, 6, 832, 480, 81)
        print(f"🆔 Task ID: {task_id}")
        
        while True:
            status = client.get_status(task_id)
            print(f"📊 Current status: {status}")
            if status == "completed": print("✅ Video ready!"); break
            elif status == "failed": print("❌ Generation failed!"); exit(1)
            time.sleep(10)
            
        output_file = client.download_video(task_id, "generated_video.mp4")
        print("🎉 Video downloaded successfully!" if output_file else "❌ Failed to download video")
        if output_file: print(f"📁 Saved as: {output_file}")
        
    except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__": main()

```


## 性能对比与选择建议

### 与14B版本对比

| 特性 | T2V-1.3B | T2V-14B |
|------|----------|---------|
| 参数规模 | 1.3B | 14B |
| 显存需求 | 6GB+ | 12GB+ |
| 生成速度 | 快 | 中等 |
| 视频质量 | 良好 | 优秀 |
| 细节丰富度 | 中等 | 高 |
| 文本理解 | 良好 | 优秀 |
| 适用场景 | 快速生成、批量处理 | 高质量创作 |

## 最佳实践

### 提示词优化
1. **简洁明确**: 轻量版对简洁提示词响应更好
2. **关键词突出**: 使用核心关键词描述主要内容
3. **避免过度复杂**: 减少过于复杂的场景描述
4. **风格指定**: 明确指定视频风格和氛围


## 故障排除

### 常见问题
1. **显存不足**: 降低分辨率或启用lowvram模式
2. **生成质量不佳**: 增加步数或调整CFG
3. **速度过慢**: 检查量化设置和offload配置
4. **模型加载失败**: 确认模型文件路径和权限



## 相关资源

- [WanVideo 2.1 官方文档](https://github.com/WanVideo/Wan2.1)
- [轻量版模型下载](https://huggingface.co/WanVideo/Wan2.1-T2V-1.3B)
- [ComfyUI WanVideo插件](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [性能优化指南](https://docs.wanvideo.ai/optimization)
- [社区讨论区](https://github.com/WanVideo/Wan2.1/discussions)