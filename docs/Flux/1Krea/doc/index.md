<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎨 Flux.1 Krea Dev 图像生成</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 独特美学风格与自然细节的完美结合</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 独特美学</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">✨ 自然细节</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🏆 卓越真实感</span>
  </div>
</div>

## 📋 Flux.1 Krea Dev 模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=79640b1911971da78cf2bedb7b3b75ca" alt="Flux.1 Krea Dev 海报" style="max-width: 600px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

[Flux.1 Krea Dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) 是由 Black Forest Labs (BFL) 与 Krea 合作开发的先进文本生成图像模型。这是目前最好的开源权重 FLUX 模型，专为文本到图像生成而设计。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">独特美学风格</h4>
<p style="margin: 0; color: #1e40af;">专注于生成具有独特美学的图像，避免常见的"AI感"外观</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">✨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">自然细节</h4>
<p style="margin: 0; color: #065f46;">不会产生过曝的高光，保持自然的细节表现</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏆</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">卓越的真实感</h4>
<p style="margin: 0; color: #9a3412;">提供出色的真实感和图像质量</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🔧</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">完全兼容架构</h4>
<p style="margin: 0; color: #5b21b6;">与 FLUX.1 [dev] 完全兼容的架构设计</p>
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📄 模型许可</strong><br>
  该模型采用 <a href="https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/LICENSE.md" target="_blank" style="color: #2563eb;">flux-1-dev-non-commercial-license</a> 许可发布，仅限非商业用途。
</div>

</div>

## 🚀 Flux.1 Krea Dev ComfyUI 工作流

### ⚠️ 环境要求

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 使用前请确认</strong><br>
  • 确保 ComfyUI 已更新到最新版本<br>
  • 推荐使用最新开发版（nightly）获得完整功能<br>
  • 本指南的工作流可在 ComfyUI 的工作流模板中找到<br>
  • 如果加载工作流时有节点缺失，请检查 ComfyUI 版本或节点导入状态
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📥 下载链接</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><a href="https://www.comfy.org/download" target="_blank" style="color: #059669;">ComfyUI 下载</a></li>
  <li><a href="/zh-CN/installation/update_comfyui" target="_blank" style="color: #059669;">ComfyUI 更新教程</a></li>
  <li><a href="/zh-CN/interface/features/template" target="_blank" style="color: #059669;">工作流模板</a></li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🔧 常见问题</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>节点缺失：版本过旧或导入失败</li>
  <li>功能不全：使用稳定版而非开发版</li>
  <li>加载失败：启动时节点导入异常</li>
</ul>
</div>

</div>

### 📥 步骤一：工作流文件下载

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
从模版打开：

![img.png](img.png)

或下载以下图片或 JSON 文件，并拖入 ComfyUI 以加载对应工作流。

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/krea/flux1_krea_dev.png" alt="Flux Krea Dev 工作流" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载，拖入 ComfyUI 加载工作流</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/flux1_krea_dev.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 下载 JSON 格式工作流
  </a>
</div>

</div>

### 🔗 步骤二：模型文件

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

#### 📂 模型文件结构

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └── flux1-krea-dev_fp8_scaled.safetensors 或 flux1-krea-dev.safetensors
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors 或 t5xxl_fp8_e4m3fn.safetensors
│   └── vae/
│       └── ae.safetensors</code></pre>
</div>


#### 💡 模型版本选择建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">💚 FP8 量化版本</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px;">
  <li>显存需求：12-16GB</li>
  <li>适合：RTX 4060 Ti 16GB、RTX 4070 等</li>
  <li>质量：接近原版，显存友好</li>
</ul>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🔥 原始权重版本</h4>
<ul style="margin: 0; padding-left: 20px; color: #9a3412; font-size: 14px;">
  <li>显存需求：24GB+</li>
  <li>适合：RTX 4090、A100 等</li>
  <li>质量：最高质量输出</li>
</ul>
</div>

</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 重要提醒</strong><br>
  • <code>flux1-krea-dev.safetensors</code> 文件需要同意 <a href="https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/" target="_blank" style="color: #dc2626;">black-forest-labs/FLUX.1-Krea-dev</a> 的协议后才能下载<br>
  • 如果你使用过其他 Flux 工作流，Text Encoders 和 VAE 文件可以复用，无需重复下载
</div>

</div>

### 🔧 步骤三：工作流配置操作


<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 低显存用户提醒</strong><br>
  对于低显存用户，这个模型可能无法在你的设备上顺利运行，建议等待社区提供更多优化版本或使用 FP8 量化版本。
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8475817d518de939bb6c5aabf8c1770e" alt="ComfyUI Flux Krea Dev工作流" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 详细配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Diffusion Model 加载</h4>
<p style="margin: 0 0 8px 0; color: #1e40af; font-size: 14px;">在 <strong>Load Diffusion Model</strong> 节点中选择：</p>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li><code>flux1-krea-dev_fp8_scaled.safetensors</code>（推荐）</li>
  <li>或 <code>flux1-krea-dev.safetensors</code>（高显存）</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📝 Text Encoders 配置</h4>
<p style="margin: 0 0 8px 0; color: #065f46; font-size: 14px;">在 <strong>DualCLIPLoader</strong> 节点中确保：</p>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 13px;">
  <li><strong>clip_name1</strong>: t5xxl_fp16.safetensors 或 t5xxl_fp8_e4m3fn.safetensors</li>
  <li><strong>clip_name2</strong>: clip_l.safetensors</li>
</ul>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🎨 VAE 加载</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">在 <strong>Load VAE</strong> 节点中加载 <code>ae.safetensors</code></p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">📝 提示词设置</h4>
<p style="margin: 0; color: #5b21b6; font-size: 14px;">在 <strong>CLIP Text Encode</strong> 节点中输入你的创意提示词</p>
</div>

</div>

#### 🎛️ Text Encoder 选择指南

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">显存容量</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">推荐 T5 版本</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">< 16GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">t5xxl_fp8_e4m3fn.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">低显存优化版本</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">16-24GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">t5xxl_fp8_e4m3fn.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">平衡性能与质量</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">≥ 32GB</td>
      <td style="padding: 12px; font-family: monospace; font-size: 12px;">t5xxl_fp16.safetensors</td>
      <td style="padding: 12px;">最佳质量体验</td>
    </tr>
  </tbody>
</table>
</div>

#### 🚀 执行生成

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ 点击 Queue 按钮或使用快捷键 Ctrl(Cmd) + Enter 运行工作流</strong>
  </div>
</div>

</div>

## API调用
<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
📋 点击展开ComfyUI API调用Python代码
</summary>

```python

import requests
import json
import uuid
import time
import random
import os

# Configuration Parameters - Flux Krea Specific
COMFYUI_SERVER = "127.0.0.1:8188"  # Local server
COMFYUI_TOKEN = ""  # Usually no token needed for local
UNET_MODEL = "flux1-krea-dev_fp8_scaled.safetensors"
VAE_MODEL = "flux-ae.safetensors"
CLIP_L_MODEL = "clip_l_bf16.safetensors"
CLIP_T5_MODEL = "t5xxl_fp16.safetensors"

# Default Parameters
DEFAULT_PROMPT = "Highly realistic portrait of a Nordic woman with blonde hair and blue eyes, very few freckles on her face, gaze sharp and intellectual. The lighting should reflect the unique coolness of Northern Europe. Outfit is minimalist and modern, background is blurred in cool tones. Needs to perfectly capture the characteristics of a Scandinavian woman. solo, Centered composition"

class ComfyUIFluxKreaClient:
def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
self.base_url = f"http://{server}"
self.token = token
self.client_id = str(uuid.uuid4())
self.headers = {"Content-Type": "application/json"}
if token:
self.headers["Authorization"] = f"Bearer {token}"

    def generate_flux_krea_image(self, prompt, steps=20, cfg=1, 
                                width=1024, height=1024, seed=None):
        """Generate Flux Krea text-to-image based on original JSON workflow"""
        print("Starting Flux Krea text-to-image generation...")
        
        # Generate random seed if not provided
        if seed is None:
            seed = random.randint(1, 1000000000000000)

        # Workflow based on your provided JSON
        workflow = {
            "8": {
                "inputs": {
                    "samples": ["31", 0],
                    "vae": ["39", 0]
                },
                "class_type": "VAEDecode",
                "_meta": {"title": "VAE Decode"}
            },
            "9": {
                "inputs": {
                    "filename_prefix": "flux_krea/flux_krea",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage",
                "_meta": {"title": "Save Image"}
            },
            "27": {
                "inputs": {
                    "width": width,
                    "height": height,
                    "batch_size": 1
                },
                "class_type": "EmptySD3LatentImage",
                "_meta": {"title": "Empty SD3 Latent Image"}
            },
            "31": {
                "inputs": {
                    "seed": seed,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "denoise": 1,
                    "model": ["38", 0],
                    "positive": ["45", 0],
                    "negative": ["42", 0],
                    "latent_image": ["27", 0]
                },
                "class_type": "KSampler",
                "_meta": {"title": "K Sampler"}
            },
            "38": {
                "inputs": {
                    "unet_name": UNET_MODEL,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader"}
            },
            "39": {
                "inputs": {
                    "vae_name": VAE_MODEL
                },
                "class_type": "VAELoader",
                "_meta": {"title": "VAE Loader"}
            },
            "40": {
                "inputs": {
                    "clip_name1": CLIP_L_MODEL,
                    "clip_name2": CLIP_T5_MODEL,
                    "type": "flux",
                    "device": "default"
                },
                "class_type": "DualCLIPLoader",
                "_meta": {"title": "Dual CLIP Loader"}
            },
            "42": {
                "inputs": {
                    "conditioning": ["45", 0]
                },
                "class_type": "ConditioningZeroOut",
                "_meta": {"title": "Conditioning Zero Out"}
            },
            "45": {
                "inputs": {
                    "text": prompt,
                    "clip": ["40", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {"title": "CLIP Text Encode"}
            }
        }

        print("Submitting Flux Krea text-to-image workflow...")
        print(f"Prompt: {prompt}")
        print(f"Random Seed: {seed}")
        
        response = requests.post(
            f"{self.base_url}/prompt", 
            headers=self.headers, 
            json={"prompt": workflow, "client_id": self.client_id}
        )
        
        print(f"API Response: {response.text}")

        if response.status_code != 200:
            raise Exception(f"API request failed with status code: {response.status_code}")

        result = response.json()
        if "error" in result:
            raise Exception(f"Workflow error: {result['error']}")
        if "prompt_id" not in result:
            raise Exception(f"No prompt_id in response: {result}")
        
        return result["prompt_id"], seed

    def get_status(self, task_id):
        """Get task status"""
        try:
            # Check queue status
            queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
            
            # Check if in running queue
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])):
                return "processing"
            
            # Check if in pending queue
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])):
                return "pending"
            
            # Check history
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            if history_response.status_code == 200:
                history = history_response.json()
                if task_id in history:
                    return "completed"
            
            return "processing"
        except Exception as e:
            print(f"Status check error: {e}")
            return "processing"

    def download_image(self, task_id, output_dir="outputs"):
        """Download generated images"""
        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            
            if task_id in history:
                outputs = history[task_id]['outputs']
                downloaded_files = []
                
                for node_id, output in outputs.items():
                    if 'images' in output:
                        for img_info in output['images']:
                            filename = img_info['filename']
                            # Download image
                            img_response = requests.get(
                                f"{self.base_url}/view?filename={filename}", 
                                headers=self.headers
                            )
                            
                            if img_response.status_code == 200:
                                output_path = os.path.join(output_dir, filename)
                                with open(output_path, "wb") as f:
                                    f.write(img_response.content)
                                downloaded_files.append(output_path)
                                print(f"Image saved: {output_path}")
                
                return downloaded_files
                
        except Exception as e:
            print(f"Download error: {e}")
        
        return []

    def generate_batch(self, prompts_list, **kwargs):
        """Batch generate images"""
        results = []
        
        for i, prompt in enumerate(prompts_list):
            print(f"\nStarting task {i+1}/{len(prompts_list)}...")
            
            try:
                task_id, seed = self.generate_flux_krea_image(prompt, **kwargs)
                
                # Wait for completion
                while True:
                    status = self.get_status(task_id)
                    print(f"Task {i+1} status: {status}")
                    
                    if status == "completed":
                        files = self.download_image(task_id)
                        results.append({
                            'task_id': task_id,
                            'seed': seed,
                            'files': files,
                            'prompt': prompt
                        })
                        break
                    elif status == "failed":
                        print(f"Task {i+1} failed")
                        break
                    
                    time.sleep(5)
                    
            except Exception as e:
                print(f"Task {i+1} error: {e}")
        
        return results

    def generate_with_variations(self, base_prompt, variations, **kwargs):
        """Generate images with prompt variations"""
        prompts = [f"{base_prompt}, {variation}" for variation in variations]
        return self.generate_batch(prompts, **kwargs)

def main():
"""Main function - Execute Flux Krea text-to-image generation"""
client = ComfyUIFluxKreaClient()

    try:
        print("Flux Krea text-to-image client started...")
        
        # Single image generation example
        print("\n=== Single Image Generation ===")
        task_id, seed = client.generate_flux_krea_image(
            prompt=DEFAULT_PROMPT,
            steps=20,
            cfg=1,
            width=1024,
            height=1024
        )
        
        print(f"Task ID: {task_id}")
        print(f"Seed: {seed}")

        # Wait for task completion
        while True:
            status = client.get_status(task_id)
            print(f"Current status: {status}")
            
            if status == "completed":
                print("Image generation completed!")
                break
            elif status == "failed":
                print("Generation failed!")
                return
            
            time.sleep(5)

        # Download images
        downloaded_files = client.download_image(task_id)
        if downloaded_files:
            print(f"Successfully downloaded {len(downloaded_files)} files!")
            for file in downloaded_files:
                print(f"File path: {file}")
        else:
            print("Download failed")

        # Batch generation example
        print("\n=== Batch Generation Example ===")
        batch_prompts = [
            "Portrait of a young Asian woman with long black hair, wearing traditional kimono, cherry blossoms in background, soft lighting",
            "Professional headshot of a businessman in a navy suit, confident expression, office background, studio lighting",
            "Artistic portrait of an elderly man with a white beard, weathered face, dramatic side lighting, black and white"
        ]
        
        # Uncomment to run batch generation
        # batch_results = client.generate_batch(batch_prompts, steps=20, cfg=1)
        # print(f"Batch generation completed, generated {len(batch_results)} images")

        # Variation generation example
        print("\n=== Variation Generation Example ===")
        base_prompt = "Portrait of a woman"
        variations = [
            "smiling, warm lighting",
            "serious expression, dramatic lighting", 
            "laughing, natural outdoor lighting",
            "contemplative, soft studio lighting"
        ]
        
        # Uncomment to run variation generation
        # variation_results = client.generate_with_variations(base_prompt, variations, steps=15)
        # print(f"Variation generation completed, generated {len(variation_results)} images")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
main()

```

</details>


## 🎯 Flux.1 Krea Dev 特色优势

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">艺术美学</h4>
<p style="margin: 0; color: #1e40af;">独特的美学风格，避免常见的 AI 生成痕迹</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">📸</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">摄影级质感</h4>
<p style="margin: 0; color: #065f46;">自然的光影处理，不会产生过曝的高光效果</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏆</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">开源最佳</h4>
<p style="margin: 0; color: #9a3412;">目前最好的开源 FLUX 模型权重</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🔄</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">完全兼容</h4>
<p style="margin: 0; color: #5b21b6;">与现有 FLUX.1 [dev] 工作流完全兼容</p>
</div>

</div>

## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>使用详细、具体的提示词描述</li>
  <li>充分利用模型的美学风格特点</li>
  <li>根据显存情况选择合适的模型版本</li>
  <li>尝试不同的采样器和步数组合</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>确保有足够的显存运行模型</li>
  <li>原始权重版本需要更多计算资源</li>
  <li>注意模型的非商业许可限制</li>
  <li>首次运行可能需要较长加载时间</li>
</ul>
</div>

</div>

## 🔧 技术规格

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 💻 系统要求

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">配置项</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">FP8 版本</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">原始权重版本</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">GPU 显存</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">12-16GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">24GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">系统内存</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB+</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">32GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">存储空间</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">15GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">25GB</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">推荐 GPU</td>
      <td style="padding: 12px;">RTX 4060 Ti 16GB / RTX 4070</td>
      <td style="padding: 12px;">RTX 4090 / A100</td>
    </tr>
  </tbody>
</table>
</div>

### 🎨 生成能力

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">人物肖像</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">风景摄影</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">艺术创作</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">产品设计</span>
  </div>
  <div style="background: #fef3c7; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">建筑渲染</span>
  </div>
  <div style="background: #fef2f2; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #dc2626; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">概念艺术</span>
  </div>
</div>

</div>

## 🎯 应用场景

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">艺术创作</h4>
<p style="margin: 0; color: #1e40af;">概念艺术、插画设计、视觉艺术创作</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">📱</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">内容创作</h4>
<p style="margin: 0; color: #065f46;">社交媒体内容、博客配图、营销素材</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">影视制作</h4>
<p style="margin: 0; color: #9a3412;">分镜头设计、概念预览、视觉开发</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🔬</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">研究实验</h4>
<p style="margin: 0; color: #5b21b6;">AI 研究、模型对比、学术研究</p>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎨 <strong>Flux.1 Krea Dev 图像生成</strong> | 独特美学风格与自然细节的完美结合
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Black Forest Labs & Krea | 非商业许可 | 让 AI 图像生成更具艺术美感
  </p>
</div>