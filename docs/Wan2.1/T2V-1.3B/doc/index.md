# 🎬 Wan2.1-T2V-1.3B 模型介绍

<div align="center">

![Wan2.1-T2V](https://img.shields.io/badge/Wan2.1--T2V--1.3B-Lightweight%20Video%20AI-purple?style=for-the-badge&logo=video)
![Parameters](https://img.shields.io/badge/Parameters-1.3B-blue?style=for-the-badge&logo=cpu)
![VRAM](https://img.shields.io/badge/VRAM-6GB+-green?style=for-the-badge&logo=memory)
![Open Source](https://img.shields.io/badge/Open%20Source-MIT-orange?style=for-the-badge&logo=open-source-initiative)

</div>

Wan2.1-T2V-1.3B 是 WanVideo 2.1 系列文本到视频生成模型的轻量级版本，专为资源受限环境设计。该模型在保持良好视频生成质量的同时，显著降低了硬件要求，让更多用户能够在消费级设备上体验文本到视频技术。

---

## ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%); text-align: center;">
<h3>🪶 轻量设计</h3>
<p>仅 1.3B 参数，相比 14B 版本显著降低资源需求</p>
</div>

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%); text-align: center;">
<h3>⚡ 高效生成</h3>
<p>优化推理速度，适合实时和批量生成</p>
</div>

<div style="border: 2px solid #e17055; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%); text-align: center;">
<h3>💾 低显存需求</h3>
<p>仅需 6GB 显存即可运行，兼容更多设备</p>
</div>

<div style="border: 2px solid #0984e3; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%); text-align: center;">
<h3>🌍 多语言支持</h3>
<p>支持中文和英文文本提示</p>
</div>

<div style="border: 2px solid #fdcb6e; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #fffbf0 0%, #fff3e0 100%); text-align: center;">
<h3>🔧 灵活部署</h3>
<p>支持单机和集群部署</p>
</div>

<div style="border: 2px solid #a29bfe; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #faf8ff 0%, #f3e5f5 100%); text-align: center;">
<h3>🔓 开源友好</h3>
<p>完全开源，支持二次开发和定制</p>
</div>

</div>

---

## 📊 技术规格

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 15px; margin: 20px 0;">

<table style="width: 100%; color: white; border-collapse: collapse;">
<tr style="background: rgba(255,255,255,0.1);">
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2); font-weight: bold;">规格项目</td>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2); font-weight: bold;">详细信息</td>
</tr>
<tr>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">🎞️ 最大帧数</td>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">81 帧</td>
</tr>
<tr style="background: rgba(255,255,255,0.05);">
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">🎬 推荐帧率</td>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">16fps</td>
</tr>
<tr>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">⚙️ 推荐步数</td>
<td style="padding: 15px; border: 1px solid rgba(255,255,255,0.2);">15-25 步</td>
</tr>
</table>

</div>

---

## 🆚 与 14B 版本对比

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%);">
<h3 style="color: #00b894; text-align: center;">🪶 T2V-1.3B (轻量版)</h3>
<ul style="list-style: none; padding: 0;">
<li>✅ 参数规模：1.3B</li>
<li>✅ 显存需求：6GB+</li>
<li>✅ 推理速度：更快</li>
<li>✅ 适用场景：快速原型、批量生成</li>
</ul>
</div>

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h3 style="color: #6c5ce7; text-align: center;">🚀 T2V-14B (完整版)</h3>
<ul style="list-style: none; padding: 0;">
<li>⭐ 参数规模：14B</li>
<li>⭐ 显存需求：12GB+</li>
<li>⭐ 生成质量：卓越</li>
<li>⭐ 适用场景：高质量创作</li>
</ul>
</div>

</div>

---

## 🏗️ 部署架构

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">

<div style="border: 2px solid #0984e3; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%);">
<h3 style="color: #0984e3;">🎯 方法一：ACS 集群部署（推荐）</h3>
<div style="background: rgba(9, 132, 227, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;">
<p><strong>🖥️ 显存</strong>: GPU</p>
<p><strong>💾 内存</strong>: 96GB</p>
</div>
</div>

<div style="border: 2px solid #e17055; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%);">
<h3 style="color: #e17055;">🖥️ 方法二：ECS 部署</h3>
<div style="background: rgba(225, 112, 85, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;">
<p><strong>🎮 显存</strong>: A10 等</p>
<p><strong>💾 内存</strong>: 30GB</p>
</div>
</div>

</div>

---

# 📖 使用指南

## 🎛️ ComfyUI 使用方法

<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); color: white; padding: 25px; border-radius: 15px; margin: 20px 0;">

### 🚀 快速开始

1. **🌐 访问界面**: 点击服务实例的访问链接
   ![访问界面](img_3.png)

2. **⚙️ 选择工作流**: 选择适合的视频生成工作流

3. **🎯 模型选择**: 确认已选择 Wan2.1-T2V-1.3B 模型

4. **📝 设置参数**:
   - 输入文本描述（支持中英文）
   - 设置视频分辨率和帧数
   - 调整生成参数（步数、CFG 等）

5. **⚡ 快速生成**: 点击"生成"按钮

6. **📥 下载结果**: 生成完成后下载视频文件

</div>

### 🔌 ComfyUI API 调用

**获取 Token**: 点击右上角按钮，打开底部面板，获取 token
![Token获取](img_1.png)

**获取服务器地址**: 参考下图获取 COMFYUI_SERVER
![服务器地址](img_3.png)

<details style="border: 2px solid #0066cc; border-radius: 8px; padding: 15px; margin: 10px 0; background-color: #f8f9fa;">
<summary style="font-weight: bold; font-size: 18px; color: #0066cc; cursor: pointer;">
📋 点击展开 API 调用 Python 代码
</summary>

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
        print(f"API 响应: {response.text}")
        result = response.json()
        if "error" in result: raise Exception(f"工作流错误: {result['error']}")
        if "prompt_id" not in result: raise Exception(f"响应中没有 prompt_id: {result}")
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
        except Exception as e: print(f"下载错误: {e}")
        return None

def main():
    client = ComfyUIClient()
    try:
        print("🎬 开始文本到视频任务...")
        task_id = client.generate("一个美丽的动漫女孩，长长的黑发，优雅地跳舞", "低质量，模糊，扭曲", 15, 6, 832, 480, 81)
        print(f"🆔 任务ID: {task_id}")
        
        while True:
            status = client.get_status(task_id)
            print(f"📊 当前状态: {status}")
            if status == "completed": print("✅ 视频准备就绪!"); break
            elif status == "failed": print("❌ 生成失败!"); exit(1)
            time.sleep(10)
            
        output_file = client.download_video(task_id, "generated_video.mp4")
        print("🎉 视频下载成功!" if output_file else "❌ 视频下载失败")
        if output_file: print(f"📁 保存为: {output_file}")
        
    except Exception as e: print(f"❌ 错误: {e}")

if __name__ == "__main__": main()
```
</details>

---

## 📊 性能对比与选择指南

<div style="overflow-x: auto; margin: 20px 0;">

<table style="width: 100%; border-collapse: collapse; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px; overflow: hidden;">
<thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
<tr>
<th style="padding: 15px; text-align: left;">🏷️ 特性</th>
<th style="padding: 15px; text-align: center;">🪶 T2V-1.3B</th>
<th style="padding: 15px; text-align: center;">🚀 T2V-14B</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; font-weight: bold;">📊 参数规模</td>
<td style="padding: 15px; text-align: center; color: #00b894;">1.3B</td>
<td style="padding: 15px; text-align: center; color: #6c5ce7;">14B</td>
</tr>
<tr>
<td style="padding: 15px; font-weight: bold;">💾 显存需求</td>
<td style="padding: 15px; text-align: center; color: #00b894;">6GB+</td>
<td style="padding: 15px; text-align: center; color: #e17055;">12GB+</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; font-weight: bold;">⚡ 生成速度</td>
<td style="padding: 15px; text-align: center; color: #00b894;">快速</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">中等</td>
</tr>
<tr>
<td style="padding: 15px; font-weight: bold;">🎬 视频质量</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">良好</td>
<td style="padding: 15px; text-align: center; color: #00b894;">卓越</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; font-weight: bold;">🎯 适用场景</td>
<td style="padding: 15px; text-align: center; color: #0984e3;">快速生成、批量处理</td>
<td style="padding: 15px; text-align: center; color: #6c5ce7;">高质量创作</td>
</tr>
</tbody>
</table>

</div>

---

## 💡 最佳实践

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin: 20px 0;">

<div style="border-left: 5px solid #00b894; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%);">
<h3>📝 提示词优化</h3>
<ul>
<li><strong>简洁明了</strong>: 轻量版对简洁提示词响应更好</li>
<li><strong>突出关键词</strong>: 使用核心关键词描述主要内容</li>
<li><strong>避免过度复杂</strong>: 减少过于复杂的场景描述</li>
<li><strong>风格指定</strong>: 明确指定视频风格和氛围</li>
</ul>
</div>

<div style="border-left: 5px solid #6c5ce7; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h3>⚙️ 参数调优</h3>
<ul>
<li><strong>步数设置</strong>: 15-20 步为最佳平衡点</li>
<li><strong>CFG 调节</strong>: 6-8 范围内效果较好</li>
<li><strong>分辨率选择</strong>: 832x480 为推荐分辨率</li>
<li><strong>帧数控制</strong>: 根据内容复杂度调整帧数</li>
</ul>
</div>

</div>

---

## 🔧 故障排除

<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); color: white; padding: 25px; border-radius: 15px; margin: 20px 0;">

### 🚨 常见问题

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin: 20px 0;">

<div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
<h4>💾 显存不足</h4>
<p>降低分辨率或启用 lowvram 模式</p>
</div>

<div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
<h4>🎬 生成质量差</h4>
<p>增加步数或调整 CFG 值</p>
</div>

<div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
<h4>🐌 速度过慢</h4>
<p>检查量化设置和 offload 配置</p>
</div>

<div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
<h4>❌ 模型加载失败</h4>
<p>确认模型文件路径和权限</p>
</div>

</div>

</div>

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">

<div style="border: 2px solid #0984e3; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%); text-align: center;">
<h3>📖 官方文档</h3>
<a href="https://github.com/WanVideo/Wan2.1" style="color: #0984e3; text-decoration: none; font-weight: bold;">WanVideo 2.1 官方文档</a>
</div>

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%); text-align: center;">
<h3>📥 模型下载</h3>
<a href="https://huggingface.co/WanVideo/Wan2.1-T2V-1.3B" style="color: #00b894; text-decoration: none; font-weight: bold;">轻量级模型下载</a>
</div>

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%); text-align: center;">
<h3>🔌 插件支持</h3>
<a href="https://github.com/kijai/ComfyUI-WanVideoWrapper" style="color: #6c5ce7; text-decoration: none; font-weight: bold;">ComfyUI WanVideo 插件</a>
</div>

</div>

---

<div align="center" style="margin-top: 40px;">

### 🎬 开始您的 AI 视频创作之旅！

![开始创作](https://img.shields.io/badge/Ready%20to%20Create-Let's%20Make%20Videos!-brightgreen?style=for-the-badge&logo=video)

<p style="color: #666; font-style: italic; margin-top: 20px;">
轻量级 AI 视频生成，让创意触手可及
</p>

</div>