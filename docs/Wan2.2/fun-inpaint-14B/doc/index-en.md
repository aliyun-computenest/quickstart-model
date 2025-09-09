<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 Wan2.2-Fun-Inp First & Last Frame Video Generation</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI Native Workflow - Precise Control of Video First and Last Frames</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 Frame Control</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 Cinematic Quality</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📐 Multi-Resolution</span>
  </div>
</div>

## 📋 Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Wan2.2-Fun-Inp** is a first and last frame controlled video generation model developed by the Alibaba PAI team. It supports inputting **first and last frame images** to generate intermediate transition videos, providing creators with enhanced creative control. The model is released under the **Apache 2.0 license** and supports commercial use.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>🎯 First & Last Frame Control</strong><br>
    <p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Support input of first and last frame images to generate intermediate transition videos</p>
  </div>

  <div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎬 High-Quality Video Generation</strong><br>
    <p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Based on Wan2.2 architecture, outputs cinematic-quality videos</p>
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>📐 Multi-Resolution Support</strong><br>
    <p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Supports 512×512, 768×768, 1024×1024 and other resolutions</p>
  </div>

  <div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>⚡ 14B High-Performance Version</strong><br>
    <p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Model size reaches 32GB+, better results but requires high VRAM</p>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 Related Resources</strong><br>
  • <strong>Model Repository</strong>: <a href="https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP" target="_blank" style="color: #2563eb;">🤗 Wan2.2-Fun-Inp-14B</a><br>
  • <strong>Code Repository</strong>: <a href="https://github.com/aigc-apps/VideoX-Fun" target="_blank" style="color: #2563eb;">VideoX-Fun</a>
</div>

</div>

## 🎥 ComfyOrg Wan2.2 Fun InP Live Stream Replay

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

A dedicated live demonstration has been conducted for ComfyUI Wan2.2 usage. You can learn detailed usage methods and techniques through the following replay.

<div style="text-align: center; margin: 20px 0;">
  <iframe style="width: 100%; aspect-ratio: 16/9; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="//player.bilibili.com/player.html?isOutside=true&aid=115027747082114&bvid=BV1DVbrzdEFR&cid=31697013072&p=1&autoplay=0" title="ComfyUI Wan2.2 Fun InP Tutorial" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

</div>

## 🚀 Wan2.2 Fun Inp Workflow Example

### ⚠️ Environment Requirements

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 Pre-usage Checklist</strong><br>
  • Ensure ComfyUI is updated to the latest version<br>
  • Recommend using the latest development version (nightly) for full functionality<br>
  • The workflow in this guide can be found in ComfyUI's workflow templates<br>
  • If nodes are missing when loading the workflow, check ComfyUI version or node import status
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📥 Download Links</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><a href="https://www.comfy.org/download" target="_blank" style="color: #059669;">ComfyUI Download</a></li>
  <li><a href="/installation/update_comfyui" target="_blank" style="color: #059669;">ComfyUI Update Tutorial</a></li>
  <li><a href="/interface/features/template" target="_blank" style="color: #059669;">Workflow Templates</a></li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🔧 Common Issues</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Missing nodes: Version too old or import failed</li>
  <li>Incomplete features: Using stable version instead of dev version</li>
  <li>Loading failure: Node import exception during startup</li>
</ul>
</div>

</div>

### 🔧 Workflow Version Description

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Two workflow versions are provided for selection:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">⚡ Lightning Accelerated Version</h4>
<p style="margin: 0 0 8px 0; color: #1e40af; font-size: 14px;">Uses <a href="https://huggingface.co/lightx2v/Wan2.2-Lightning" target="_blank" style="color: #2563eb;">Wan2.2-Lightning</a> 4-step LoRA</p>
<div style="background: #dcfce7; color: #059669; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block; margin-right: 8px;">✅ Faster Speed</div>
<div style="background: #fed7aa; color: #ea580c; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block;">⚠️ Dynamic Loss</div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎯 Standard Quality Version</h4>
<p style="margin: 0 0 8px 0; color: #065f46; font-size: 14px;">Uses fp8_scaled version without acceleration LoRA</p>
<div style="background: #dcfce7; color: #059669; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block; margin-right: 8px;">✅ Higher Quality</div>
<div style="background: #fed7aa; color: #ea580c; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block;">⏱️ Longer Time</div>
</div>

</div>

#### 📊 Performance Comparison Test

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🧪 Test Environment</strong>: RTX 4090D 24GB VRAM, 640×640 resolution, 81 frames length
</div>

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Model Type</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Resolution</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">VRAM Usage</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">First Generation</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Second Generation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">fp8_scaled</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">640×640</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">83%</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 524s</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 520s</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">fp8_scaled + 4-step LoRA</td>
      <td style="padding: 12px;">640×640</td>
      <td style="padding: 12px;">89%</td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 138s</span></td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 79s</span></td>
    </tr>
  </tbody>
</table>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Version Switching Instructions</strong><br>
  Due to the significant speed improvement of the accelerated LoRA version and its friendliness to low-VRAM users, the accelerated version is enabled by default. To switch to the standard version, select the corresponding workflow and use <strong>Ctrl+B</strong> to enable it.
</div>

</div>

### 📥 Step 1: Download Workflow Files

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/wan2.2_14B_fun_inp.mp4"></video>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_fun_inpaint.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 Download JSON Workflow File
  </a>
</div>

### 📁 Sample Material Download

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ First Frame Image</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/start_image.png" alt="First Frame Material" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🖼️ Last Frame Image</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/end_image.png" alt="Last Frame Material" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
</div>

</div>

</div>

### 🔗 Step 2: Model Files

#### 📂 Model File Structure

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


### 🔧 Step 3: Workflow Configuration Operations

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3d87de35d3eaa2f9599c35e9963c6c18" alt="Workflow Configuration Steps" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Reminder</strong><br>
  This workflow uses the LoRA accelerated version. Please ensure that the corresponding Diffusion Model and LoRA files are consistent (high-noise with high-noise, low-noise with low-noise).
</div>

#### 📋 Detailed Configuration Steps

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🔧 High Noise Model Configuration</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>:<br><code>wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>:<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🔧 Low Noise Model Configuration</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>:<br><code>wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>:<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors</code></li>
</ul>
</div>

</div>

#### 🎯 Base Model Configuration

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Node Name</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Model File</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Load CLIP</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">umt5_xxl_fp8_e4m3fn_scaled.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Text encoder</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Load VAE</td>
      <td style="padding: 12px; font-family: monospace; font-size: 12px;">wan_2.1_vae.safetensors</td>
      <td style="padding: 12px;">Variational autoencoder</td>
    </tr>
  </tbody>
</table>
</div>

#### 📁 Input Configuration

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ First & Last Frame Image Upload</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Upload first and last frame image materials to corresponding Load Image nodes</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📝 Prompt Input</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Enter prompts describing video content in the Prompt group</p>
</div>

</div>

#### ⚙️ Parameter Adjustment

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎬 WanFunInpaintToVideo Node Configuration</strong><br>
  • <strong>width & height</strong>: Adjust video dimensions, default is 640×640<br>
  • <strong>length</strong>: Set total video frames, current workflow fps is 16<br>
  • <strong>Calculation Example</strong>: To generate a 5-second video, set 5 × 16 = 80 frames
</div>

#### 🚀 Execute Generation

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ Click the Run button or use shortcut Ctrl(Cmd) + Enter to execute video generation</strong>
  </div>
</div>

</div>

## API
<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
📋 ComfyUI API Python
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


## 🎯 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Film Production</h4>
<p style="margin: 0; color: #1e40af;">Precise control of scene transitions and shot transitions</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Creative Animation</h4>
<p style="margin: 0; color: #065f46;">Artistic creation and concept design visualization</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">📱</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Social Media</h4>
<p style="margin: 0; color: #9a3412;">Short video content and marketing material production</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🎮</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">Game Development</h4>
<p style="margin: 0; color: #5b21b6;">Game animation and cutscene production</p>
</div>

</div>

## 💡 Usage Tips and Recommendations

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Best Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>Maintain style consistency between first and last frame images</li>
  <li>Choose appropriate resolution to balance quality and performance</li>
  <li>Select suitable model version based on VRAM capacity</li>
  <li>Prompts should accurately describe the transition process</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ Important Notes</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Ensure High/Low Noise models match with LoRA</li>
  <li>Lightning LoRA sacrifices some dynamic effects</li>
  <li>Long video generation requires more compute resources</li>
  <li>Excessive differences between first and last frames may affect transition</li>
</ul>
</div>

</div>

## 🔧 Technical Specifications

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 💻 System Requirements

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Component</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Minimum</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Recommended</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">GPU VRAM</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">20GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">24GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">System RAM</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">32GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">64GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Storage Space</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">50GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">100GB+ SSD</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Recommended GPU</td>
      <td style="padding: 12px;">RTX 4090</td>
      <td style="padding: 12px;">RTX 4090 / A100</td>
    </tr>
  </tbody>
</table>
</div>

### 📐 Supported Resolutions

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

### 🚀 Performance Optimization Tips

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">⚡ Speed Optimization</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>Use Lightning LoRA</strong>: 4 steps vs 20 steps</li>
  <li><strong>Lower Resolution</strong>: Start with 640×640 for testing</li>
  <li><strong>Batch Processing</strong>: Process multiple videos efficiently</li>
  <li><strong>GPU Optimization</strong>: Use latest CUDA drivers</li>
</ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🎯 Quality Optimization</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>Standard Workflow</strong>: 20 steps for best results</li>
  <li><strong>Higher Resolution</strong>: Use 1024×1024 for final output</li>
  <li><strong>Consistent Frames</strong>: Ensure style consistency</li>
  <li><strong>Clear Prompts</strong>: Detailed transition descriptions</li>
</ul>
</div>

</div>

</div>

## 🎬 Advanced Features

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🎯 Frame Interpolation Control

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎬 Precise Transition Control</strong><br>
  The model excels at creating smooth transitions between first and last frames, maintaining visual coherence while allowing for creative transformations. This makes it ideal for storytelling and narrative video creation.
</div>

### 🎨 Creative Applications

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>🌟 Morphing Effects</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Create seamless object or character transformations</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🌅 Time-lapse Simulation</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Generate time progression effects and environmental changes</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🎭 Emotion Transitions</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Capture subtle facial expression and mood changes</p>
</div>

</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎬 <strong>Wan2.2-Fun-Inp First & Last Frame Video Generation</strong> | Precise Control of Every Frame's Creative Expression
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Alibaba PAI Team | Apache 2.0 Open Source License | Let Creativity Flow Freely Between First and Last Frames
  </p>
</div>