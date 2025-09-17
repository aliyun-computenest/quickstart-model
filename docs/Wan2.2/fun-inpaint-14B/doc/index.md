<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 Wan2.2-Fun-Inp 首尾帧视频生成</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 精确控制视频首尾帧的创意生成</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 首尾帧控制</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 影视级质量</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📐 多分辨率</span>
  </div>
</div>

## 📋 模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Wan2.2-Fun-Inp** 是 Alibaba PAI 团队推出的首尾帧控制视频生成模型，支持输入**首帧和尾帧图像**，生成中间过渡视频，为创作者带来更强的创意控制力。该模型采用 **Apache 2.0 许可协议**发布，支持商业使用。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>🎯 首尾帧控制</strong><br>
    <p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">支持输入首帧和尾帧图像，生成中间过渡视频</p>
  </div>

  <div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎬 高质量视频生成</strong><br>
    <p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">基于 Wan2.2 架构，输出影视级质量视频</p>
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>📐 多分辨率支持</strong><br>
    <p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">支持 512×512、768×768、1024×1024 等分辨率</p>
  </div>

  <div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>⚡ 14B 高性能版</strong><br>
    <p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">模型体积达 32GB+，效果更优但需高显存支持</p>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 相关资源</strong><br>
  • <strong>模型仓库</strong>：<a href="https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP" target="_blank" style="color: #2563eb;">🤗 Wan2.2-Fun-Inp-14B</a><br>
  • <strong>代码仓库</strong>：<a href="https://github.com/aigc-apps/VideoX-Fun" target="_blank" style="color: #2563eb;">VideoX-Fun</a>
</div>

</div>




### 📥 步骤一：工作流文件下载

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
你可以直接从Comfyui的模版打开

![img_1.png](img_1.png)
<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/wan2.2_14B_fun_inp.mp4"></video>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_fun_inpaint.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 下载 JSON 格式工作流
  </a>
</div>

### 📁 示例素材下载

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 首帧图像</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/start_image.png" alt="首帧素材" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🖼️ 尾帧图像</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/end_image.png" alt="尾帧素材" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
</div>

</div>

</div>

### 🔗 步骤二：模型文件



#### 📂 模型文件结构

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors</code></pre>
</div>


### 🔧 步骤三：工作流配置操作

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3d87de35d3eaa2f9599c35e9963c6c18" alt="工作流配置步骤图" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 重要提醒</strong><br>
  此工作流使用了 LoRA 加速版本，请确保对应的 Diffusion Model 和 LoRA 文件保持一致（高噪声对高噪声，低噪声对低噪声）。
</div>

#### 📋 详细配置步骤

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🔧 High Noise 模型配置</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>：<br><code>wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>：<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🔧 Low Noise 模型配置</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>：<br><code>wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>：<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors</code></li>
</ul>
</div>

</div>

#### 🎯 基础模型配置

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">节点名称</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">模型文件</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Load CLIP</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">umt5_xxl_fp8_e4m3fn_scaled.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">文本编码器</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Load VAE</td>
      <td style="padding: 12px; font-family: monospace; font-size: 12px;">wan_2.1_vae.safetensors</td>
      <td style="padding: 12px;">变分自编码器</td>
    </tr>
  </tbody>
</table>
</div>

#### 📁 输入配置

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ 首尾帧图片上传</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">分别上传首帧和尾帧图片素材到对应的 Load Image 节点</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📝 提示词输入</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">在 Prompt 组中输入描述视频内容的提示词</p>
</div>

</div>

#### ⚙️ 参数调整

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎬 WanFunInpaintToVideo 节点配置</strong><br>
  • <strong>width & height</strong>：调整视频尺寸，默认为 640×640<br>
  • <strong>length</strong>：设置视频总帧数，当前工作流 fps 为 16<br>
  • <strong>计算示例</strong>：生成 5 秒视频需要设置 5 × 16 = 80 帧
</div>

#### 🚀 执行生成

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ 点击 Run 按钮或使用快捷键 Ctrl(Cmd) + Enter 执行视频生成</strong>
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

# Configuration Parameters - Wan2.2 First-Last Frame to Video Specific
COMFYUI_SERVER = "127.0.0.1:8188"  # Local server
COMFYUI_TOKEN = ""  # Usually no token needed for local

# Model Configuration
HIGH_NOISE_UNET = "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors"
LOW_NOISE_UNET = "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"
CLIP_MODEL = "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
VAE_MODEL = "wan_2.1_vae.safetensors"
HIGH_NOISE_LORA = "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"
LOW_NOISE_LORA = "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"

# Default Parameters
DEFAULT_POSITIVE_PROMPT = """A bearded man with red facial hair wearing a yellow straw hat and dark coat in Van Gogh's self-portrait style, slowly and continuously transforms into a space astronaut. The transformation flows like liquid paint - his beard fades away strand by strand, the yellow hat melts and reforms smoothly into a silver space helmet, dark coat gradually lightens and restructures into a white spacesuit. The background swirling brushstrokes slowly organize and clarify into realistic stars and space, with Earth appearing gradually in the distance. Every change happens in seamless waves, maintaining visual continuity throughout the metamorphosis.

Consistent soft lighting throughout, medium close-up maintaining same framing, central composition stays fixed, gentle color temperature shift from warm to cool, gradual contrast increase, smooth style transition from painterly to photorealistic. Static camera with subtle slow zoom, emphasizing the flowing transformation process without abrupt changes."""

DEFAULT_NEGATIVE_PROMPT = "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"

DEFAULT_START_IMAGE = "ComfyUI_00592_.png"
DEFAULT_END_IMAGE = "Qwen-Image_00002_.png"

class ComfyUIWan22FirstLastFrameClient:
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

    def generate_first_last_frame_video(self, positive_prompt, negative_prompt=None,
                                       start_image_path=None, start_image_name=None,
                                       end_image_path=None, end_image_name=None,
                                       width=640, height=640, length=81, fps=16,
                                       steps=4, cfg=1, seed=None, shift=5.0,
                                       lora_strength=1.0):
        """Generate First-Last Frame video using Wan2.2 based on original JSON workflow"""
        print("Starting Wan2.2 First-Last Frame to Video generation...")
        
        # Use default negative prompt if not provided
        if negative_prompt is None:
            negative_prompt = DEFAULT_NEGATIVE_PROMPT
            
        # Generate random seed if not provided
        if seed is None:
            seed = random.randint(1, 1000000000000000)

        # Handle start image
        if start_image_path and not start_image_name:
            start_image_name = self.upload_image(start_image_path)
            if not start_image_name:
                raise Exception("Failed to upload start image")
        elif not start_image_name:
            start_image_name = DEFAULT_START_IMAGE

        # Handle end image
        if end_image_path and not end_image_name:
            end_image_name = self.upload_image(end_image_path)
            if not end_image_name:
                raise Exception("Failed to upload end image")
        elif not end_image_name:
            end_image_name = DEFAULT_END_IMAGE

        # Workflow based on your provided JSON
        workflow = {
            "6": {
                "inputs": {
                    "text": positive_prompt,
                    "clip": ["38", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {"title": "CLIP Text Encode (Positive Prompt)"}
            },
            "7": {
                "inputs": {
                    "text": negative_prompt,
                    "clip": ["38", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {"title": "CLIP Text Encode (Negative Prompt)"}
            },
            "8": {
                "inputs": {
                    "samples": ["58", 0],
                    "vae": ["39", 0]
                },
                "class_type": "VAEDecode",
                "_meta": {"title": "VAE Decode"}
            },
            "37": {
                "inputs": {
                    "unet_name": HIGH_NOISE_UNET,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader (High Noise)"}
            },
            "38": {
                "inputs": {
                    "clip_name": CLIP_MODEL,
                    "type": "wan",
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
            "54": {
                "inputs": {
                    "shift": shift,
                    "model": ["91", 0]
                },
                "class_type": "ModelSamplingSD3",
                "_meta": {"title": "Model Sampling SD3 (High Noise)"}
            },
            "55": {
                "inputs": {
                    "shift": shift,
                    "model": ["92", 0]
                },
                "class_type": "ModelSamplingSD3",
                "_meta": {"title": "Model Sampling SD3 (Low Noise)"}
            },
            "56": {
                "inputs": {
                    "unet_name": LOW_NOISE_UNET,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader (Low Noise)"}
            },
            "57": {
                "inputs": {
                    "add_noise": "enable",
                    "noise_seed": seed,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "start_at_step": 0,
                    "end_at_step": 2,
                    "return_with_leftover_noise": "enable",
                    "model": ["54", 0],
                    "positive": ["67", 0],
                    "negative": ["67", 1],
                    "latent_image": ["67", 2]
                },
                "class_type": "KSamplerAdvanced",
                "_meta": {"title": "K Sampler Advanced (High Noise Stage)"}
            },
            "58": {
                "inputs": {
                    "add_noise": "disable",
                    "noise_seed": 0,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "start_at_step": 2,
                    "end_at_step": 10000,
                    "return_with_leftover_noise": "disable",
                    "model": ["55", 0],
                    "positive": ["67", 0],
                    "negative": ["67", 1],
                    "latent_image": ["57", 0]
                },
                "class_type": "KSamplerAdvanced",
                "_meta": {"title": "K Sampler Advanced (Low Noise Stage)"}
            },
            "60": {
                "inputs": {
                    "fps": fps,
                    "images": ["8", 0]
                },
                "class_type": "CreateVideo",
                "_meta": {"title": "Create Video"}
            },
            "61": {
                "inputs": {
                    "filename_prefix": "wan22_first_last_frame/video",
                    "format": "auto",
                    "codec": "auto",
                    "video": ["60", 0]
                },
                "class_type": "SaveVideo",
                "_meta": {"title": "Save Video"}
            },
            "62": {
                "inputs": {
                    "image": end_image_name
                },
                "class_type": "LoadImage",
                "_meta": {"title": "Load End Image"}
            },
            "67": {
                "inputs": {
                    "width": width,
                    "height": height,
                    "length": length,
                    "batch_size": 1,
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "vae": ["39", 0],
                    "start_image": ["68", 0],
                    "end_image": ["62", 0]
                },
                "class_type": "WanFirstLastFrameToVideo",
                "_meta": {"title": "Wan First Last Frame To Video"}
            },
            "68": {
                "inputs": {
                    "image": start_image_name
                },
                "class_type": "LoadImage",
                "_meta": {"title": "Load Start Image"}
            },
            "91": {
                "inputs": {
                    "lora_name": HIGH_NOISE_LORA,
                    "strength_model": lora_strength,
                    "model": ["37", 0]
                },
                "class_type": "LoraLoaderModelOnly",
                "_meta": {"title": "LoRA Loader (High Noise)"}
            },
            "92": {
                "inputs": {
                    "lora_name": LOW_NOISE_LORA,
                    "strength_model": lora_strength,
                    "model": ["56", 0]
                },
                "class_type": "LoraLoaderModelOnly",
                "_meta": {"title": "LoRA Loader (Low Noise)"}
            }
        }

        print("Submitting Wan2.2 First-Last Frame to Video generation workflow...")
        print(f"Positive Prompt: {positive_prompt[:100]}...")
        print(f"Start Image: {start_image_name}")
        print(f"End Image: {end_image_name}")
        print(f"Video Dimensions: {width}x{height}")
        print(f"Video Length: {length} frames")
        print(f"FPS: {fps}")
        print(f"Steps: {steps}")
        print(f"CFG: {cfg}")
        print(f"Seed: {seed}")
        print(f"Shift: {shift}")
        
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

    def download_video(self, task_id, output_dir="outputs"):
        """Download generated video files"""
        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            
            if task_id in history:
                outputs = history[task_id]['outputs']
                downloaded_files = []
                
                for node_id, output in outputs.items():
                    # Check for video files
                    if 'videos' in output:
                        for video_info in output['videos']:
                            filename = video_info['filename']
                            # Download video
                            video_response = requests.get(
                                f"{self.base_url}/view?filename={filename}", 
                                headers=self.headers
                            )
                            
                            if video_response.status_code == 200:
                                output_path = os.path.join(output_dir, filename)
                                with open(output_path, "wb") as f:
                                    f.write(video_response.content)
                                downloaded_files.append(output_path)
                                print(f"Video saved: {output_path}")
                    
                    # Check for preview images
                    if 'images' in output:
                        for img_info in output['images']:
                            filename = img_info['filename']
                            # Download preview image
                            img_response = requests.get(
                                f"{self.base_url}/view?filename={filename}", 
                                headers=self.headers
                            )
                            
                            if img_response.status_code == 200:
                                output_path = os.path.join(output_dir, filename)
                                with open(output_path, "wb") as f:
                                    f.write(img_response.content)
                                downloaded_files.append(output_path)
                                print(f"Preview image saved: {output_path}")
                
                return downloaded_files
                
        except Exception as e:
            print(f"Download error: {e}")
        
        return []

    def generate_batch(self, configs, **kwargs):
        """Batch generate first-last frame videos with different configurations"""
        results = []
        
        for i, config in enumerate(configs):
            print(f"\nStarting First-Last Frame video generation task {i+1}/{len(configs)}...")
            
            try:
                task_id, seed = self.generate_first_last_frame_video(**config, **kwargs)
                
                # Wait for completion
                while True:
                    status = self.get_status(task_id)
                    print(f"Task {i+1} status: {status}")
                    
                    if status == "completed":
                        files = self.download_video(task_id)
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
                    
                    time.sleep(15)  # Video generation takes time
                    
            except Exception as e:
                print(f"Task {i+1} error: {e}")
        
        return results

    def generate_transformation_sequence(self, start_image_path, end_image_path, 
                                       transformation_prompt, length_preset="medium"):
        """Generate transformation video with predefined length settings"""
        length_presets = {
            "short": {"length": 49, "fps": 12},
            "medium": {"length": 81, "fps": 16},
            "long": {"length": 121, "fps": 20},
            "extra_long": {"length": 161, "fps": 24}
        }
        
        settings = length_presets.get(length_preset, length_presets["medium"])
        return self.generate_first_last_frame_video(
            positive_prompt=transformation_prompt,
            start_image_path=start_image_path,
            end_image_path=end_image_path,
            **settings
        )

    def generate_morphing_video(self, image_pairs, base_prompt_template):
        """Generate multiple morphing videos from image pairs"""
        results = []
        
        for i, (start_img, end_img, description) in enumerate(image_pairs):
            prompt = base_prompt_template.format(description=description)
            print(f"\nGenerating morphing video {i+1}: {description}")
            
            try:
                task_id, seed = self.generate_first_last_frame_video(
                    positive_prompt=prompt,
                    start_image_path=start_img,
                    end_image_path=end_img
                )
                
                # Wait for completion
                while True:
                    status = self.get_status(task_id)
                    if status == "completed":
                        files = self.download_video(task_id)
                        results.append({
                            'description': description,
                            'files': files,
                            'start_image': start_img,
                            'end_image': end_img
                        })
                        break
                    elif status == "failed":
                        print(f"Morphing video {i+1} failed")
                        break
                    time.sleep(15)
                    
            except Exception as e:
                print(f"Morphing video {i+1} error: {e}")
        
        return results

def main():
    """Main function - Execute Wan2.2 First-Last Frame to Video generation"""
    client = ComfyUIWan22FirstLastFrameClient()
    
    try:
        print("Wan2.2 First-Last Frame to Video generation client started...")
        
        # Single transformation video generation example
        print("\n=== Single Transformation Video Generation ===")
        
        # You can provide local file paths or use existing file names
        start_image_path = None  # Set to your start image path, e.g., "start.jpg"
        end_image_path = None    # Set to your end image path, e.g., "end.jpg"
        
        task_id, seed = client.generate_first_last_frame_video(
            positive_prompt=DEFAULT_POSITIVE_PROMPT,
            negative_prompt=DEFAULT_NEGATIVE_PROMPT,
            start_image_path=start_image_path,
            start_image_name=DEFAULT_START_IMAGE,
            end_image_path=end_image_path,
            end_image_name=DEFAULT_END_IMAGE,
            width=640,
            height=640,
            length=81,
            fps=16,
            steps=4,
            cfg=1,
            shift=5.0
        )
        
        print(f"Task ID: {task_id}")
        print(f"Seed: {seed}")

        # Wait for task completion
        while True:
            status = client.get_status(task_id)
            print(f"Current status: {status}")
            
            if status == "completed":
                print("First-Last Frame video generation completed!")
                break
            elif status == "failed":
                print("Generation failed!")
                return
            
            time.sleep(15)

        # Download video files
        downloaded_files = client.download_video(task_id)
        if downloaded_files:
            print(f"Successfully downloaded {len(downloaded_files)} files!")
            for file in downloaded_files:
                print(f"File path: {file}")
        else:
            print("Download failed")

        # Transformation sequence example
        print("\n=== Transformation Sequence Example ===")
        # Uncomment to test different transformation lengths
        # if start_image_path and end_image_path:
        #     for preset in ["short", "medium", "long"]:
        #         print(f"Generating {preset} transformation...")
        #         task_id, seed = client.generate_transformation_sequence(
        #             start_image_path, end_image_path, 
        #             "Smooth transformation between two states", preset
        #         )
        #         # Wait and download logic here...

        # Morphing video example
        print("\n=== Morphing Video Example ===")
        # image_pairs = [
        #     ("portrait1.jpg", "portrait2.jpg", "person transforms into another person"),
        #     ("cat.jpg", "dog.jpg", "cat slowly morphs into a dog"),
        #     ("day.jpg", "night.jpg", "day scene transitions to night scene")
        # ]
        # 
        # prompt_template = "Smooth and seamless transformation where {description}. " \
        #                  "The change happens gradually with flowing motion, maintaining " \
        #                  "visual continuity throughout the metamorphosis."
        # 
        # morphing_results = client.generate_morphing_video(image_pairs, prompt_template)
        # print(f"Generated {len(morphing_results)} morphing videos")

        # Batch generation example
        print("\n=== Batch Generation Example ===")
        batch_configs = [
            {
                'positive_prompt': "A flower blooming from bud to full bloom, time-lapse style transformation",
                'start_image_name': DEFAULT_START_IMAGE,
                'end_image_name': DEFAULT_END_IMAGE,
                'length': 49,
                'fps': 12
            },
            {
                'positive_prompt': "Sunset to sunrise transformation, smooth color transition in the sky",
                'start_image_name': DEFAULT_START_IMAGE,
                'end_image_name': DEFAULT_END_IMAGE,
                'length': 81,
                'fps': 16
            }
        ]
        
        # Uncomment to run batch generation
        # batch_results = client.generate_batch(batch_configs, steps=4, cfg=1)
        # print(f"Batch generation completed, generated {len(batch_results)} videos")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


```

</details>


## 🎯 应用场景

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">影视制作</h4>
<p style="margin: 0; color: #1e40af;">精确控制场景转换和镜头过渡</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">创意动画</h4>
<p style="margin: 0; color: #065f46;">艺术创作和概念设计可视化</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">📱</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">社交媒体</h4>
<p style="margin: 0; color: #9a3412;">短视频内容和营销素材制作</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🎮</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">游戏开发</h4>
<p style="margin: 0; color: #5b21b6;">游戏动画和过场动画制作</p>
</div>

</div>

## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>首尾帧图像保持风格一致性</li>
  <li>选择合适的分辨率平衡质量与性能</li>
  <li>根据显存情况选择合适的模型版本</li>
  <li>提示词要准确描述过渡过程</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>确保 High/Low Noise 模型与 LoRA 匹配</li>
  <li>Lightning LoRA 会牺牲部分动态效果</li>
  <li>长视频生成需要更多计算资源</li>
  <li>首尾帧差异过大可能影响过渡效果</li>
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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">20GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">24GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">系统内存</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">32GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">64GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">存储空间</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">50GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">100GB+ SSD</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">推荐 GPU</td>
      <td style="padding: 12px;">RTX 4090</td>
      <td style="padding: 12px;">RTX 4090 / A100</td>
    </tr>
  </tbody>
</table>
</div>

### 📐 支持分辨率

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">512×512</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">640×640</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">768×768</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">1024×1024</span>
  </div>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎬 <strong>Wan2.2-Fun-Inp 首尾帧视频生成</strong> | 精确控制每一帧的创意表达
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Alibaba PAI 团队 | Apache 2.0 开源协议 | 让创意在首尾之间自由流淌
  </p>
</div>