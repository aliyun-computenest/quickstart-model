<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">📹 Wan2.2-Fun-Camera-Control Video Generation</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI Native Workflow - Professional Camera Motion Control for Video Generation</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📹 Camera Motion Control</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 Cinematic Quality</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 Combined Motion</span>
  </div>
</div>

## 📋 Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Wan2.2-Fun-Camera-Control** is a next-generation video generation and camera control model developed by the Alibaba PAI team. By introducing innovative Camera Control Codes mechanisms combined with deep learning and multi-modal conditional inputs, it can generate high-quality videos that conform to preset camera motion conditions. The model is released under the **Apache 2.0 license** and supports commercial use.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>📹 Camera Motion Control</strong><br>
    <p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Supports Pan Up/Down, Pan Left/Right, Zoom In/Out and other motion modes</p>
  </div>

  <div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎬 High-Quality Video Generation</strong><br>
    <p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Based on Wan2.2 architecture, outputs cinematic-quality videos</p>
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>🎯 Combined Motion Control</strong><br>
    <p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Supports combination control of multiple camera motions</p>
  </div>

  <div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>⚙️ Precise Parameter Control</strong><br>
    <p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Adjustable motion speed, intensity and other fine parameters</p>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 Related Resources</strong><br>
  • <strong>Model Repository</strong>: <a href="https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control-Camera" target="_blank" style="color: #2563eb;">🤗 Wan2.2-Fun-A14B-Control-Camera</a><br>
  • <strong>Code Repository</strong>: <a href="https://github.com/aigc-apps/VideoX-Fun" target="_blank" style="color: #2563eb;">VideoX-Fun</a>
</div>

</div>

## 🚀 Wan2.2 Fun Camera Control Workflow Example

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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">84%</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 536s</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 513s</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">fp8_scaled + 4-step LoRA</td>
      <td style="padding: 12px;">640×640</td>
      <td style="padding: 12px;">89%</td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 108s</span></td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 71s</span></td>
    </tr>
  </tbody>
</table>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Version Switching Instructions</strong><br>
  Since the 4-step LoRA provides better user experience for first-time workflow users, the accelerated version is enabled by default. To switch to the standard version, select the corresponding workflow and use <strong>Ctrl+B</strong> to enable it.
</div>

</div>

### 📥 Step 1: Download Workflow and Materials

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Download the following video or JSON file and drag it into ComfyUI to load the corresponding workflow. The workflow will prompt to download models.

<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_camera/wan2.2_14B_fun_camera.mp4"></video>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_fun_camera.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 Download JSON Workflow File
  </a>
</div>

### 📁 Sample Material Download

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Input Starting Image</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_camera/input.jpg" alt="Input Starting Image" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 13px;">This image will serve as the starting frame for video generation</p>
</div>

</div>

### 🔗 Step 2: Download Model Files

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

All model files can be found in the <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged" target="_blank" style="color: #2563eb;">Wan_2.2_ComfyUI_Repackaged</a> repository.

#### 📂 Model File Structure

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors</code></pre>
</div>

#### 🔽 Model Download Links

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Model Type</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">File Name</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">🧠 Diffusion Models</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">
        <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors" target="_blank" style="color: #2563eb;">wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors</a><br>
        <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors" target="_blank" style="color: #2563eb;">wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors</a>
      </td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">High-noise and low-noise camera control models</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">⚡ Wan2.2-Lightning LoRA</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">
        <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors" target="_blank" style="color: #2563eb;">wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors</a><br>
        <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors" target="_blank" style="color: #2563eb;">wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors</a>
      </td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Acceleration LoRA (optional)</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">🎨 VAE</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">
        <a href="https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors" target="_blank" style="color: #2563eb;">wan_2.1_vae.safetensors</a>
      </td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Variational autoencoder</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">📝 Text Encoder</td>
      <td style="padding: 12px; font-family: monospace; font-size: 12px;">
        <a href="https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors" target="_blank" style="color: #2563eb;">umt5_xxl_fp8_e4m3fn_scaled.safetensors</a>
      </td>
      <td style="padding: 12px;">Text encoder</td>
    </tr>
  </tbody>
</table>
</div>

</div>

### 🔧 Step 3: Workflow Configuration Operations

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_2.2_14b_fun_camera.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8fd9faf8734e1f53f4838d25bb7eb822" alt="Wan2.2 Fun Camera Control Workflow Steps" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Reminder</strong><br>
  This workflow uses the LoRA accelerated version. Please ensure that the corresponding Diffusion Model and LoRA files are consistent, with high noise and low noise models and LoRAs used correspondingly.
</div>

#### 📋 Detailed Configuration Steps

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🔧 High Noise Model Configuration</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>:<br><code>wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>:<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🔧 Low Noise Model Configuration</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>:<br><code>wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors</code></li>
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

#### 📁 Input Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ Starting Frame Upload</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Upload the starting frame image in the <strong>Load Image</strong> node</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📝 Modify Prompts</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Modify prompts, supports Chinese and English input</p>
</div>

</div>

#### 📹 Camera Control Parameter Configuration

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎬 WanCameraEmbedding Node Configuration</strong><br>
  Set various camera control parameters in this node:
</div>

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Parameter Name</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Available Values</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Camera Motion</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; font-size: 12px;">Zoom In, Zoom Out, Pan Up, Pan Down, Pan Left, Pan Right, Static</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Select camera motion type</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Width/Height</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">640×640 (default)</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Set video resolution</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Length</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">81 (default)</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Set video frame count</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Speed</td>
      <td style="padding: 12px;">1.0 (default)</td>
      <td style="padding: 12px;">Set video speed</td>
    </tr>
  </tbody>
</table>
</div>

#### 🚀 Execute Generation

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ Click the Run button or use shortcut Ctrl(Cmd) + Enter to execute video generation</strong>
  </div>
</div>

</div>

## 📹 Camera Motion Types Explained

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🔍</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Zoom In</h4>
<p style="margin: 0; color: #1e40af;">Camera moves forward, gradually enlarging the frame</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🔎</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Zoom Out</h4>
<p style="margin: 0; color: #065f46;">Camera moves backward, gradually reducing the frame</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">⬆️</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Pan Up</h4>
<p style="margin: 0; color: #9a3412;">Camera moves upward, revealing upper content</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">⬇️</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">Pan Down</h4>
<p style="margin: 0; color: #5b21b6;">Camera moves downward, revealing lower content</p>
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #d97706;">⬅️</div>
<h4 style="margin: 0 0 8px 0; color: #d97706;">Pan Left</h4>
<p style="margin: 0; color: #9a3412;">Camera moves left, revealing left-side content</p>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #dc2626;">➡️</div>
<h4 style="margin: 0 0 8px 0; color: #dc2626;">Pan Right</h4>
<p style="margin: 0; color: #991b1b;">Camera moves right, revealing right-side content</p>
</div>

</div>

## 🎯 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Film Production</h4>
<p style="margin: 0; color: #1e40af;">Professional camera movements for cinematic visual effects</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">📱</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Short Video Creation</h4>
<p style="margin: 0; color: #065f46;">Dynamic visual presentation for social media content</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏢</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Product Showcase</h4>
<p style="margin: 0; color: #9a3412;">Professional camera movements for product promotional videos</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">Artistic Creation</h4>
<p style="margin: 0; color: #5b21b6;">Dynamic display and expression of artistic works</p>
</div>

</div>

## 💡 Usage Tips and Recommendations

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Best Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>Choose appropriate camera motion to match content theme</li>
  <li>Adjust motion speed for optimal visual effects</li>
  <li>Select appropriate resolution based on VRAM capacity</li>
  <li>Keep prompts coordinated with camera motion</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ Important Notes</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Ensure High/Low Noise models match with LoRA</li>
  <li>Too fast camera motion may cause frame instability</li>
  <li>Complex scenes recommend using slower motion speeds</li>
  <li>Long-duration generation requires more compute resources</li>
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

### 📹 Camera Control Precision

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🎯 Motion Precision</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>Pan Control</strong>: Pixel-level precision</li>
  <li><strong>Zoom Control</strong>: Smooth progressive</li>
  <li><strong>Speed Control</strong>: 0.1-2.0x speed</li>
</ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">⚡ Performance Optimization</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>Lightning LoRA</strong>: 5x speed improvement</li>
  <li><strong>FP8 Quantization</strong>: VRAM optimization</li>
  <li><strong>Smart Caching</strong>: Reduce redundant computation</li>
</ul>
</div>

</div>

### 🎬 Advanced Camera Features

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🎯 Combined Motion</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Support combination control of multiple camera motions</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⏱️ Temporal Control</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Precise control of motion start and end times</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>📐 Motion Trajectory</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Customize camera motion trajectory paths</p>
</div>

</div>

</div>

### 🎨 Creative Applications

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🎬 Cinematic Shots</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Create professional film-style camera movements</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>📱 Social Media</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Engaging camera movements for viral content</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🏢 Commercial Use</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Professional product demonstrations and marketing</p>
</div>

</div>

</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    📹 <strong>Wan2.2-Fun-Camera-Control Video Generation</strong> | Professional Camera Motion for Video Creation
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Alibaba PAI Team | Apache 2.0 Open Source License | Making Every Shot Cinematic
  </p>
</div>