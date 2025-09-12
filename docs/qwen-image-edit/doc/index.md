<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">✏️ Qwen-Image-Edit 图像编辑</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 精准文字编辑与语义外观双重编辑能力</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📝 精准文字编辑</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎨 语义外观编辑</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🌐 中英双语</span>
  </div>
</div>

## 📋 Qwen-Image-Edit 模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Qwen-Image-Edit** 是 Qwen-Image 的图像编辑版本。它基于 20B 的 Qwen-Image 模型进一步训练，成功将 Qwen-Image 的文本渲染特色能力拓展到编辑任务上，以支持精准的文字编辑。此外，Qwen-Image-Edit 将输入图像同时输入到 Qwen2.5-VL（获取视觉语义控制）和 VAE Encoder（获得视觉外观控制），以同时获得语义/外观双重编辑能力。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">📝</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">精准文字编辑</h4>
<p style="margin: 0; color: #1e40af;">支持中英双语文字编辑，保留文字大小/字体/风格的前提下进行增删改</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">语义/外观双重编辑</h4>
<p style="margin: 0; color: #065f46;">支持 low-level 视觉外观编辑和 high-level 视觉语义编辑</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏆</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">SOTA 性能表现</h4>
<p style="margin: 0; color: #9a3412;">在多个公开基准测试中均获得 SOTA，强大的图像生成基础模型</p>
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 官方资源</strong><br>
  • <strong>GitHub 仓库</strong>：<a href="https://github.com/QwenLM/Qwen-Image" target="_blank" style="color: #2563eb;">QwenLM/Qwen-Image</a><br>
  • <strong>Hugging Face</strong>：<a href="https://huggingface.co/Qwen/Qwen-Image-Edit" target="_blank" style="color: #2563eb;">🤗 Qwen/Qwen-Image-Edit</a><br>
  • <strong>ModelScope</strong>：<a href="https://modelscope.cn/models/qwen/Qwen-Image-Edit" target="_blank" style="color: #2563eb;">ModelScope</a>
</div>

### 🎯 核心编辑能力

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<h4 style="color: #d97706; margin: 0 0 8px 0;">🔤 Low-Level 视觉外观编辑</h4>
<ul style="margin: 0; padding-left: 20px; color: #9a3412;">
  <li>风格迁移</li>
  <li>图像增删改</li>
  <li>色彩调整</li>
  <li>纹理修改</li>
</ul>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🧠 High-Level 视觉语义编辑</h4>
<ul style="margin: 0; padding-left: 20px; color: #5b21b6;">
  <li>IP 制作</li>
  <li>物体旋转</li>
  <li>场景重构</li>
  <li>概念替换</li>
</ul>
</div>

</div>

</div>

## 🎥 ComfyOrg Qwen-Image-Edit 直播回放

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

观看官方直播回放，了解 Qwen-Image-Edit 在 ComfyUI 中的详细使用方法和最佳实践。

<div style="text-align: center; margin: 20px 0;">
  <iframe style="width: 100%; aspect-ratio: 16/9; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://www.youtube.com/embed/TZIijn-tvoc?si=Vb-ZNwTvJC67_UEE" title="Qwen-Image Edit in ComfyUI - Image Editing Model / August 19th, 2025" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

</div>

## 🚀 Qwen-Image-Edit ComfyUI 原生工作流

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

更新 ComfyUI 后可以从模板中找到工作流文件，或者将下面的工作流拖入 ComfyUI 中加载。

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-edit/qwen_image_edit.png" alt="Qwen-Image-Edit 工作流" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载，拖入 ComfyUI 加载工作流</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_edit.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 下载 JSON 格式工作流
  </a>
</div>

### 📁 示例输入图片

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 示例输入图片</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-edit/input.png" alt="示例输入图片" style="max-width: 400px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 13px;">右键保存图片，用于工作流测试</p>
</div>

</div>

### 🔗 步骤二：模型文件


#### 📂 模型文件结构

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_fp8_e4m3fn.safetensors
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors</code></pre>
</div>


### 🔧 步骤三：工作流配置操作

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/qwen_image_edit.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=98a706bfa8f1578a4dfd7f2a0a415926" alt="Qwen-Image-Edit 工作流配置步骤" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 详细配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 模型加载</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>：<br><code>qwen_image_edit_fp8_e4m3fn.safetensors</code></li>
  <li><strong>Load CLIP</strong>：<br><code>qwen_2.5_vl_7b_fp8_scaled.safetensors</code></li>
  <li><strong>Load VAE</strong>：<br><code>qwen_image_vae.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 图片加载</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">在 <strong>Load Image</strong> 节点中上传用于编辑的图片</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">📝 提示词设置</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">在 <strong>CLIP Text Encoder</strong> 节点中设置编辑提示词</p>
</div>

</div>

#### ⚙️ 高级配置选项

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<h4 style="color: #d97706; margin: 0 0 8px 0;">📐 图像尺寸处理</h4>
<p style="margin: 0 0 8px 0; color: #9a3412; font-size: 14px;"><strong>Scale Image to Total Pixels</strong> 节点会将输入图片缩放到总像素为一百万像素</p>
<ul style="margin: 0; padding-left: 20px; color: #9a3412; font-size: 13px;">
  <li>避免输入图片尺寸过大（如 2048×2048）导致的输出图像质量损失</li>
  <li>如果了解输入图片尺寸，可使用 <strong>Ctrl+B</strong> 绕过此节点</li>
</ul>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">⚡ Lightning LoRA 加速</h4>
<p style="margin: 0 0 8px 0; color: #5b21b6; font-size: 14px;">使用 4 步 Lightning LoRA 实现图片生成提速</p>
<ul style="margin: 0; padding-left: 20px; color: #5b21b6; font-size: 13px;">
  <li>选中 <strong>LoraLoaderModelOnly</strong> 节点</li>
  <li>按 <strong>Ctrl+B</strong> 启用该节点</li>
</ul>
</div>

</div>

#### 🎛️ KSampler 参数调优

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔧 KSampler 节点参数设置</strong><br>
  对于 <code>steps</code> 和 <code>cfg</code> 设置，工作流在节点下方提供了参数建议笔记，可以测试最佳的参数设置：<br>
  • <strong>Steps</strong>：推荐 20-50 步<br>
  • <strong>CFG</strong>：推荐 3.5-7.5<br>
  • <strong>Sampler</strong>：推荐 DPM++ 2M Karras
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

# Configuration Parameters - Qwen Image Edit Specific
COMFYUI_SERVER = "127.0.0.1:8188"  # Local server
COMFYUI_TOKEN = ""  # Usually no token needed for local

# Model Configuration
UNET_MODEL = "qwen_image_edit_fp8_e4m3fn.safetensors"
CLIP_MODEL = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE_MODEL = "qwen_image_vae.safetensors"

# Default Parameters
DEFAULT_EDIT_PROMPT = "Remove all UI text elements from the image. Keep the feeling that the characters and scene are in water. Also, remove the green UI elements at the bottom."
DEFAULT_NEGATIVE_PROMPT = ""
DEFAULT_INPUT_IMAGE = "Qwen-Image_00043_.png"

class ComfyUIQwenImageEditClient:
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url = f"http://{server}"
        self.token = token
        self.client_id = str(uuid.uuid4())
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def upload_image(self, image_path):
        """Upload image to ComfyUI server"""
        try:
            with open(image_path, 'rb') as f:
                files = {'image': f}
                response = requests.post(f"{self.base_url}/upload/image", files=files)
                if response.status_code == 200:
                    result = response.json()
                    return result.get('name', os.path.basename(image_path))
                else:
                    raise Exception(f"Failed to upload image: {response.text}")
        except Exception as e:
            print(f"Image upload error: {e}")
            return None

    def edit_image_with_qwen(self, edit_prompt, input_image_path=None, 
                            input_image_name=None, negative_prompt="",
                            steps=20, cfg=2.5, seed=None, shift=3.0,
                            cfg_norm_strength=1.0, megapixels=1.0,
                            upscale_method="lanczos"):
        """Edit image using Qwen Image Edit model based on original JSON workflow"""
        print("Starting Qwen Image Edit generation...")
        
        # Generate random seed if not provided
        if seed is None:
            seed = random.randint(1, 1000000000000000)

        # Handle input image
        if input_image_path and not input_image_name:
            input_image_name = self.upload_image(input_image_path)
            if not input_image_name:
                raise Exception("Failed to upload input image")
        elif not input_image_name:
            input_image_name = DEFAULT_INPUT_IMAGE

        # Workflow based on your provided JSON
        workflow = {
            "3": {
                "inputs": {
                    "seed": seed,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "denoise": 1,
                    "model": ["75", 0],
                    "positive": ["76", 0],
                    "negative": ["77", 0],
                    "latent_image": ["88", 0]
                },
                "class_type": "KSampler",
                "_meta": {"title": "K Sampler"}
            },
            "8": {
                "inputs": {
                    "samples": ["3", 0],
                    "vae": ["39", 0]
                },
                "class_type": "VAEDecode",
                "_meta": {"title": "VAE Decode"}
            },
            "37": {
                "inputs": {
                    "unet_name": UNET_MODEL,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader"}
            },
            "38": {
                "inputs": {
                    "clip_name": CLIP_MODEL,
                    "type": "qwen_image",
                    "device": "default"
                },
                "class_type": "CLIPLoader",
                "_meta": {"title": "CLIP Loader"}
            },
            "39": {
                "inputs": {
                    "vae_name": VAE_MODEL
                },
                "class_type": "VAELoader",
                "_meta": {"title": "VAE Loader"}
            },
            "60": {
                "inputs": {
                    "filename_prefix": "qwen_image_edit",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage",
                "_meta": {"title": "Save Image"}
            },
            "66": {
                "inputs": {
                    "shift": shift,
                    "model": ["37", 0]
                },
                "class_type": "ModelSamplingAuraFlow",
                "_meta": {"title": "Model Sampling AuraFlow"}
            },
            "75": {
                "inputs": {
                    "strength": cfg_norm_strength,
                    "model": ["66", 0]
                },
                "class_type": "CFGNorm",
                "_meta": {"title": "CFG Norm"}
            },
            "76": {
                "inputs": {
                    "prompt": edit_prompt,
                    "clip": ["38", 0],
                    "vae": ["39", 0],
                    "image": ["93", 0]
                },
                "class_type": "TextEncodeQwenImageEdit",
                "_meta": {"title": "Text Encode Qwen Image Edit (Positive)"}
            },
            "77": {
                "inputs": {
                    "prompt": negative_prompt,
                    "clip": ["38", 0],
                    "vae": ["39", 0],
                    "image": ["93", 0]
                },
                "class_type": "TextEncodeQwenImageEdit",
                "_meta": {"title": "Text Encode Qwen Image Edit (Negative)"}
            },
            "78": {
                "inputs": {
                    "image": input_image_name
                },
                "class_type": "LoadImage",
                "_meta": {"title": "Load Input Image"}
            },
            "88": {
                "inputs": {
                    "pixels": ["93", 0],
                    "vae": ["39", 0]
                },
                "class_type": "VAEEncode",
                "_meta": {"title": "VAE Encode"}
            },
            "93": {
                "inputs": {
                    "upscale_method": upscale_method,
                    "megapixels": megapixels,
                    "image": ["78", 0]
                },
                "class_type": "ImageScaleToTotalPixels",
                "_meta": {"title": "Image Scale To Total Pixels"}
            }
        }

        print("Submitting Qwen Image Edit workflow...")
        print(f"Edit Prompt: {edit_prompt}")
        print(f"Input Image: {input_image_name}")
        print(f"Steps: {steps}")
        print(f"CFG: {cfg}")
        print(f"Seed: {seed}")
        print(f"Megapixels: {megapixels}")
        print(f"Upscale Method: {upscale_method}")
        
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

    def generate_batch(self, edit_configs, **kwargs):
        """Batch edit images with different configurations"""
        results = []
        
        for i, config in enumerate(edit_configs):
            print(f"\nStarting image edit task {i+1}/{len(edit_configs)}...")
            
            try:
                task_id, seed = self.edit_image_with_qwen(**config, **kwargs)
                
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
                            'config': config
                        })
                        break
                    elif status == "failed":
                        print(f"Task {i+1} failed")
                        break
                    
                    time.sleep(5)
                    
            except Exception as e:
                print(f"Task {i+1} error: {e}")
        
        return results

    def edit_with_quality_presets(self, edit_prompt, input_image_path, 
                                 quality_preset="high"):
        """Edit image with predefined quality settings"""
        quality_presets = {
            "fast": {
                "steps": 10,
                "cfg": 2.0,
                "megapixels": 0.5,
                "upscale_method": "nearest-exact"
            },
            "balanced": {
                "steps": 15,
                "cfg": 2.5,
                "megapixels": 1.0,
                "upscale_method": "bilinear"
            },
            "high": {
                "steps": 20,
                "cfg": 3.0,
                "megapixels": 1.5,
                "upscale_method": "lanczos"
            },
            "ultra": {
                "steps": 30,
                "cfg": 3.5,
                "megapixels": 2.0,
                "upscale_method": "lanczos"
            }
        }
        
        settings = quality_presets.get(quality_preset, quality_presets["high"])
        return self.edit_image_with_qwen(
            edit_prompt=edit_prompt,
            input_image_path=input_image_path,
            **settings
        )

    def generate_edit_variations(self, base_image_path, edit_prompts):
        """Generate multiple edit variations of the same image"""
        results = []
        
        for i, prompt in enumerate(edit_prompts):
            print(f"\nGenerating edit variation {i+1}: {prompt[:50]}...")
            
            try:
                task_id, seed = self.edit_image_with_qwen(
                    edit_prompt=prompt,
                    input_image_path=base_image_path
                )
                
                # Wait for completion
                while True:
                    status = self.get_status(task_id)
                    if status == "completed":
                        files = self.download_image(task_id)
                        results.append({
                            'prompt': prompt,
                            'files': files,
                            'seed': seed
                        })
                        break
                    elif status == "failed":
                        print(f"Edit variation {i+1} failed")
                        break
                    time.sleep(5)
                    
            except Exception as e:
                print(f"Edit variation {i+1} error: {e}")
        
        return results

def main():
    """Main function - Execute Qwen Image Edit"""
    client = ComfyUIQwenImageEditClient()
    
    try:
        print("Qwen Image Edit client started...")
        
        # Single image edit example
        print("\n=== Single Image Edit ===")
        
        # You can provide a local image path or use existing image name
        input_image_path = None  # Set to your image path, e.g., "input.jpg"
        
        task_id, seed = client.edit_image_with_qwen(
            edit_prompt=DEFAULT_EDIT_PROMPT,
            input_image_path=input_image_path,
            input_image_name=DEFAULT_INPUT_IMAGE,
            negative_prompt=DEFAULT_NEGATIVE_PROMPT,
            steps=20,
            cfg=2.5,
            shift=3.0,
            megapixels=1.0,
            upscale_method="lanczos"
        )
        
        print(f"Task ID: {task_id}")
        print(f"Seed: {seed}")

        # Wait for task completion
        while True:
            status = client.get_status(task_id)
            print(f"Current status: {status}")
            
            if status == "completed":
                print("Image edit completed!")
                break
            elif status == "failed":
                print("Edit failed!")
                return
            
            time.sleep(5)

        # Download edited images
        downloaded_files = client.download_image(task_id)
        if downloaded_files:
            print(f"Successfully downloaded {len(downloaded_files)} files!")
            for file in downloaded_files:
                print(f"File path: {file}")
        else:
            print("Download failed")

        # Quality preset example
        print("\n=== Quality Preset Example ===")
        # Uncomment to test different quality settings
        # if input_image_path:
        #     for preset in ["fast", "balanced", "high"]:
        #         print(f"Editing with {preset} quality...")
        #         task_id, seed = client.edit_with_quality_presets(
        #             "Remove background and make it white", input_image_path, preset
        #         )
        #         # Wait and download logic here...

        # Edit variations example
        print("\n=== Edit Variations Example ===")
        edit_variations = [
            "Remove all text and UI elements from the image",
            "Change the background to a sunset sky",
            "Make the image black and white",
            "Add more vibrant colors to the scene",
            "Remove people from the image"
        ]
        
        # Uncomment to run edit variations
        # if input_image_path:
        #     variation_results = client.generate_edit_variations(input_image_path, edit_variations)
        #     print(f"Generated {len(variation_results)} edit variations")

        # Batch edit example
        print("\n=== Batch Edit Example ===")
        batch_configs = [
            {
                'edit_prompt': "Remove all UI elements and make background transparent",
                'input_image_name': DEFAULT_INPUT_IMAGE,
                'steps': 15,
                'cfg': 2.0
            },
            {
                'edit_prompt': "Change the lighting to golden hour",
                'input_image_name': DEFAULT_INPUT_IMAGE,
                'steps': 20,
                'cfg': 2.5
            }
        ]
        
        # Uncomment to run batch editing
        # batch_results = client.generate_batch(batch_configs, megapixels=1.0)
        # print(f"Batch editing completed, processed {len(batch_results)} images")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


```

</details>


## 🎯 编辑应用场景

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">📝</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">文字编辑</h4>
<p style="margin: 0; color: #1e40af;">海报文字修改、标识更换、多语言本地化</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">风格转换</h4>
<p style="margin: 0; color: #065f46;">艺术风格迁移、色调调整、视觉效果增强</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏢</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">商业应用</h4>
<p style="margin: 0; color: #9a3412;">产品图片编辑、广告素材制作、品牌视觉统一</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🎭</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">创意设计</h4>
<p style="margin: 0; color: #5b21b6;">概念艺术创作、IP 角色设计、场景重构</p>
</div>

</div>

## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>使用清晰、具体的编辑指令</li>
  <li>保持输入图像质量和分辨率适中</li>
  <li>文字编辑时描述具体的字体和样式要求</li>
  <li>利用 Lightning LoRA 进行快速预览</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>避免输入图像尺寸过大影响生成质量</li>
  <li>复杂编辑任务可能需要多次迭代</li>
  <li>文字编辑效果与原图文字清晰度相关</li>
  <li>合理设置 CFG 值避免过度拟合</li>
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
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">最低要求</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">推荐配置</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">GPU 显存</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">12GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">系统内存</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">32GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">存储空间</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">20GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">50GB+ SSD</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">推荐 GPU</td>
      <td style="padding: 12px;">RTX 4060 Ti</td>
      <td style="padding: 12px;">RTX 4080 / RTX 4090</td>
    </tr>
  </tbody>
</table>
</div>

### 🎨 支持的编辑类型

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">文字编辑</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">风格迁移</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">物体替换</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">场景重构</span>
  </div>
  <div style="background: #fef3c7; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">色彩调整</span>
  </div>
  <div style="background: #fef2f2; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #dc2626; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">纹理修改</span>
  </div>
</div>

### 🌐 语言支持

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🔤 文字编辑支持</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">中文、英文双语文字的精准编辑和替换</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>💬 指令语言</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">支持中英文编辑指令，理解复杂的编辑需求</p>
</div>

</div>

</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    ✏️ <strong>Qwen-Image-Edit 图像编辑</strong> | 精准文字编辑与语义外观双重编辑的完美结合
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 阿里巴巴通义千问团队 | 开源协议 | 让图像编辑变得智能高效
  </p>
</div>