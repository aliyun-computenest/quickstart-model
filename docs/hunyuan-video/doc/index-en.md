<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 ComfyUI Hunyuan Video Generation</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI Native Workflow - Complete Solution for Text-to-Video and Image-to-Video</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📝 Text-to-Video</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🖼️ Image-to-Video</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">⚡ High-Quality Output</span>
  </div>
</div>

## 📋 Hunyuan Video Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://github.com/user-attachments/assets/442afb73-3092-454f-bc46-02361c285930"></video>
</div>

The Hunyuan Video series is a video generation model developed and open-sourced by [Tencent](https://huggingface.co/tencent). Built on a hybrid architecture core, it supports both [text-to-video](https://github.com/Tencent/HunyuanVideo) and [image-to-video](https://github.com/Tencent/HunyuanVideo-I2V) generation with 13B parameters.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 Related Resources</strong><br>
  • <strong>Text-to-Video</strong>: <a href="https://github.com/Tencent/HunyuanVideo" target="_blank" style="color: #2563eb;">GitHub - HunyuanVideo</a><br>
  • <strong>Image-to-Video</strong>: <a href="https://github.com/Tencent/HunyuanVideo-I2V" target="_blank" style="color: #2563eb;">GitHub - HunyuanVideo-I2V</a><br>
  • <strong>Model Repository</strong>: <a href="https://huggingface.co/tencent" target="_blank" style="color: #2563eb;">🤗 Tencent HuggingFace</a>
</div>

### 🏗️ Technical Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🧠</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Core Architecture</h4>
<p style="margin: 0; color: #1e40af;">Adopts Sora-like DiT (Diffusion Transformer) architecture, effectively fusing text, image, and motion information</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">3D VAE</h4>
<p style="margin: 0; color: #065f46;">Compresses videos into compact latent space, making image-to-video generation more efficient</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Excellent Alignment</h4>
<p style="margin: 0; color: #9a3412;">Uses MLLM text encoder for precise image-video-text alignment</p>
</div>

</div>

### ✨ Key Advantages

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<strong>🎯 High-Quality Generation</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Improves consistency, quality, and alignment between generated video frames through unified full attention mechanism for multi-view shot transitions</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🌐 Multi-Language Support</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Supports Chinese and English input, better follows text instructions, captures details, and performs complex reasoning</p>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⚡ Efficient Generation</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Supports generating 5-second high-quality short videos, ensuring subject consistency and smooth motion performance</p>
</div>

</div>

</div>

## ⚠️ Environment Requirements

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 Pre-usage Checklist</strong><br>
  • Ensure ComfyUI is updated to the latest version<br>
  • Workflow image metadata contains complete workflow JSON<br>
  • Workflows in this guide can be found in ComfyUI's workflow templates<br>
  • If nodes are missing when loading workflows, check ComfyUI version or node import status
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

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Automatic Download Tip</strong><br>
  Workflow image metadata contains corresponding model download information. Dragging directly into ComfyUI will prompt to complete model downloads. If automatic download fails, all models can be manually downloaded <a href="https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files" target="_blank" style="color: #2563eb;">here</a>.
</div>

## 📝 Hunyuan Text-to-Video Workflow

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Hunyuan text-to-video was open-sourced in December 2024, supporting generation of 5-second short videos through natural language descriptions, with Chinese and English input support.

### 📥 Step 1: Download Workflow

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/t2v/kitchen.webp" alt="ComfyUI Workflow - Hunyuan Text-to-Video" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download, drag into ComfyUI to load workflow</p>
</div>

### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cf9db23e82c1c31702966878d7d6326" alt="ComfyUI Hunyuan Video T2V Workflow" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Text Encoders</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Ensure <strong>DCLIPLoader</strong> has loaded:</p>
<ul style="margin: 8px 0 0 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li>clip_name1: clip_l.safetensors</li>
  <li>clip_name2: llava_llama3_fp8_scaled.safetensors</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🧠 Diffusion Model</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Ensure <strong>Load Diffusion Model</strong> has loaded <code>hunyuan_video_t2v_720p_bf16.safetensors</code></p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🎨 VAE Model</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Ensure <strong>Load VAE</strong> has loaded <code>hunyuan_video_vae_bf16.safetensors</code></p>
</div>

</div>

#### 🚀 Execute Generation

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ Click Queue button or use shortcut Ctrl(Cmd) + Enter to run workflow</strong>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Generation Tip</strong><br>
  When the <code>length</code> in <code>EmptyHunyuanLatentVideo</code> node is set to 1, the model can generate static images.
</div>

</div>

## 🖼️ Hunyuan Image-to-Video Workflow

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

The Hunyuan image-to-video model was open-sourced on March 6, 2025. Based on the HunyuanVideo framework, it supports converting static images into smooth, high-quality videos, and also provides LoRA training code for customizing special video effects.

### 🆚 Version Comparison

Currently, the Hunyuan image-to-video model has two versions:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">v1 "concat"</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video.webp" alt="HunyuanVideo v1" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Better video motion fluidity, but less adherence to image guidance</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">v2 "replace"</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video_v2.webp" alt="HunyuanVideo v2" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Better image guidance, but seems less dynamic compared to V1 version</p>
</div>

</div>

### 🎯 v1 "concat" Image-to-Video Workflow

#### 📥 Step 1: Download Workflow and Materials

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v1_robot.webp" alt="ComfyUI Workflow - Hunyuan Image-to-Video v1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download workflow</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Starting Frame Material</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/hunyuan-video/i2v/robot-ballet.png" alt="Starting frame" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Click to download starting frame image</p>
</div>

#### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66d1fd271cc2a45a4fbcd92850074912" alt="ComfyUI Hunyuan Video I2V v1 Workflow" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Text Encoders</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Ensure <strong>DualCLIPLoader</strong> has loaded:</p>
<ul style="margin: 8px 0 0 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li>clip_name1: clip_l.safetensors</li>
  <li>clip_name2: llava_llama3_fp8_scaled.safetensors</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">👁️ Vision Encoder</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Ensure <strong>Load CLIP Vision</strong> has loaded <code>llava_llama3_vision.safetensors</code></p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🧠 Diffusion Model</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Ensure <strong>Load Diffusion Model</strong> has loaded <code>hunyuan_video_image_to_video_720p_bf16.safetensors</code></p>
</div>

</div>

### ⚡ v2 "replace" Image-to-Video Workflow

#### 📥 Step 1: Download Workflow and Materials

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v2_fennec_gril.webp" alt="ComfyUI Workflow - Hunyuan Image-to-Video v2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download workflow</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Starting Frame Material</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/flux/flux_dev_example.png" alt="Starting frame" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Click to download starting frame image</p>
</div>

#### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f26ddd8edc837fbf9d2bb4f6459a82ee" alt="ComfyUI Hunyuan Video I2V v2 Workflow" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

The v2 version configuration is basically the same as v1, with the main difference being the diffusion model:

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; margin: 16px 0;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🧠 Diffusion Model Difference</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Ensure <strong>Load Diffusion Model</strong> has loaded <code>hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors</code></p>
</div>

</div>

## 🎨 Creative Examples and Prompts

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Here are some example images and corresponding prompts. You can modify these to create your own unique videos.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🤖 Futuristic Robot</h4>
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=16d6b0ea15e14c74e8d2e5bfacfe4bf8" alt="Futuristic robot" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #1e40af;">Futuristic robot dancing ballet, dynamic motion, fast motion, fast shot, moving scene</code>
</div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">⚔️ Samurai Battle</h4>
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f8a76a691a7a9ebda088941350538375" alt="Samurai" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #059669;">Samurai waving sword and hitting the camera. camera angle movement, zoom in, fast scene, super fast, dynamic</code>
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🚗 Flying Car</h4>
<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aa2ce4f30c4d367170a8a696e62a7c7e" alt="Flying car" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #ea580c;">flying car fastly moving and flying through the city</code>
</div>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 12px 0;">🏎️ Cyberpunk Racing</h4>
<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=875b086bd33ac131bda4fe6c718b9bc7" alt="Cyberpunk racing" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #7c3aed;">cyberpunk car race in night city, dynamic, super fast, fast shot</code>
</div>
</div>

</div>

</div>

## 💡 Usage Tips and Recommendations

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Best Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>Use clear, specific action description words</li>
  <li>Choose starting images with clear subjects for image-to-video</li>
  <li>Properly use dynamic keywords like "fast motion", "dynamic"</li>
  <li>Choose appropriate version based on needs (v1 for fluidity, v2 for guidance)</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ Important Notes</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Ensure sufficient VRAM to run models (recommended 16GB+)</li>
  <li>Generation takes time, please be patient</li>
  <li>Complex scenes may require multiple attempts to optimize prompts</li>
  <li>First run requires downloading large model files</li>
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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB</td>
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
      <td style="padding: 12px;">RTX 4080</td>
      <td style="padding: 12px;">RTX 4090 / A100</td>
    </tr>
  </tbody>
</table>
</div>

### 📹 Output Specifications

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">720p Resolution</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">5-Second Videos</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Chinese & English</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">High Frame Rate</span>
  </div>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎬 <strong>ComfyUI Hunyuan Video Generation</strong> | Complete Solution for Text-to-Video and Image-to-Video
  </p>

</div>