## 模型简介

Wan2.1-T2V-14B 是一个强大的文本到视频生成模型，能够在给定文本提示的情况下生成高质量的视频内容。该模型具有以下特点：

### 核心特性
- **参数规模**: 14B参数，提供强大的生成能力
- **多分辨率支持**: 支持480P和720P分辨率输出
- **先进架构**: 结合扩散变换器架构和变分自编码器（VAE）
- **内存优化**: 使用FP8量化技术，在有限GPU内存下高效生成
- **多语言支持**: 支持中文和英文文本提示
- **复杂场景理解**: 能够处理复杂的文本描述，生成逼真的视频场景

### 技术规格
- **模型类型**: 文本到视频生成（Text-to-Video）
- **量化方式**: FP8量化版本
- **支持分辨率**:
    - 720×1280
    - 1280×720
    - 480×832
    - 832×480
- **最大帧数**: 81帧
- **推荐帧率**: 16fps

## 使用说明

### 方式一：ComfyUI界面

1. 按图中指引选择工作流侧栏，选择wanx-21.json或wans.json并打开。![img.png](img/app2.png)
2. 在下图处选择文生视频。![img.png](img.png)
3. 在TextEncode处填写描述词。上面部分是你想要生成的内容，下面部分是你不想要生成的内容。![img.png](img/prompt.png)
4. 在ImageClip Encode处可设置图片的分辨率和帧数。![img.png](img/definition.png)
5. 其余参数可参考官网：https://comfyui-wiki.com/zh/interface/node-options  或以下文档：https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md

#### ComfyUI API调用示例
点击右上方按钮，打开底部面板，获取token：![img_1.png](img_1.png)
COMFYUI_SERVER的获取可参考：![img_2.png](img_2.png)
```python
import requests, json, uuid, time, random

# 配置参数
COMFYUI_SERVER, COMFYUI_TOKEN = "输入您的服务器地址", "输入您的token"
T5_MODEL, VIDEO_MODEL, VAE_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors", "Wan2_1-T2V-14B_fp8_e4m3fn.safetensors", "wan2.1/Wan2_1_VAE_bf16.safetensors"

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
        if "prompt_id" not in result: raise Exception(f"No prompt_id in response: {result}")
        return result["prompt_id"]

    def get_status(self, task_id):
        queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
        if any(item[1] == task_id for item in queue_data.get("queue_running", [])): return "processing"
        if any(item[1] == task_id for item in queue_data.get("queue_pending", [])): return "pending"
        history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
        return "completed" if history_response.status_code == 200 and task_id in history_response.json() else "processing"

    def download_video(self, task_id, output_path="generated_video.mp4"):
        response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
        history = response.json()
        if task_id in history:
            for output in history[task_id]['outputs'].values():
                if 'gifs' in output:
                    filename = output['gifs'][0]['filename']
                    video_response = requests.get(f"{self.base_url}/view?filename={filename}", headers=self.headers)
                    with open(output_path, "wb") as f: f.write(video_response.content)
                    return output_path
        return None

def main():
    client = ComfyUIClient()
    try:
        task_id = client.generate("A beautiful anime girl with long black hair dancing gracefully", "low quality, blurry, distorted", 15, 6, 832, 480, 81)
        print(f"Task ID: {task_id}")
        while True:
            status = client.get_status(task_id)
            print(f"Current status: {status}")
            if status == "completed": print("Video ready!"); break
            elif status == "failed": print("Generation failed!"); exit(1)
            time.sleep(10)
        output_file = client.download_video(task_id, "generated_video.mp4")
        print("Video downloaded successfully!" if output_file else "Failed to download video")
        if output_file: print(f"Saved as: {output_file}")
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": main()
```


## 相关资源

- [ComfyUI官方文档](https://comfyui-wiki.com/zh/interface/node-options)
- [WanVideo插件文档](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md)