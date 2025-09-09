<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 ComfyUI 混元视频生成</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 文生视频与图生视频的完整解决方案</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">📝 文生视频</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🖼️ 图生视频</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">⚡ 高质量输出</span>
  </div>
</div>

## 📋 混元视频模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://github.com/user-attachments/assets/442afb73-3092-454f-bc46-02361c285930"></video>
</div>

混元视频（Hunyuan Video）系列是[腾讯](https://huggingface.co/tencent)研发并开源的视频生成模型，该模型以混合架构为核心，支持[文本生成视频](https://github.com/Tencent/HunyuanVideo)和[图生成视频](https://github.com/Tencent/HunyuanVideo-I2V)，参数规模达 13B。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 相关资源</strong><br>
  • <strong>文生视频</strong>：<a href="https://github.com/Tencent/HunyuanVideo" target="_blank" style="color: #2563eb;">GitHub - HunyuanVideo</a><br>
  • <strong>模型仓库</strong>：<a href="https://huggingface.co/tencent" target="_blank" style="color: #2563eb;">🤗 Tencent HuggingFace</a>
</div>

### 🏗️ 技术特点

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🧠</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">核心架构</h4>
<p style="margin: 0; color: #1e40af;">采用类似Sora的DiT（Diffusion Transformer）架构，有效融合文本、图像和动作信息</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">3D VAE</h4>
<p style="margin: 0; color: #065f46;">将视频压缩到紧凑的潜空间，使图生视频的生成更加高效</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">卓越对齐</h4>
<p style="margin: 0; color: #9a3412;">使用MLLM文本编码器，实现图像-视频-文本的精准对齐</p>
</div>

</div>

### ✨ 主要优势

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<strong>🎯 高质量生成</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">提高生成视频帧之间的一致性、质量和对齐度，通过统一的全注意力机制实现多视角镜头切换</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🌐 多语言支持</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">支持中英文输入，能够更好地遵循文本指令，捕捉细节，并进行复杂推理</p>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⚡ 高效生成</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">支持生成5秒高质量短视频，确保主体一致性和流畅的动作表现</p>
</div>

</div>

</div>

## ⚠️ 环境要求

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 使用前请确认</strong><br>
  • 确保 ComfyUI 已更新到最新版本<br>
  • 工作流图片的 Metadata 中包含完整的工作流 JSON<br>
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

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 自动下载提示</strong><br>
  工作流图片的 Metadata 中已包含对应模型下载信息，直接拖入 ComfyUI 会提示完成对应的模型下载。如果自动下载无法完成，所有模型可在 <a href="https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files" target="_blank" style="color: #2563eb;">这里</a> 手动下载。
</div>

## 📝 混元文生视频工作流

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

混元文生视频开源于 2024 年 12 月，支持通过自然语言描述生成 5 秒的短视频，支持中英文输入。

### 📥 步骤一：下载工作流

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/t2v/kitchen.webp" alt="ComfyUI 工作流 - 混元文生视频" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载，拖入 ComfyUI 加载工作流</p>
</div>

### 🔧 步骤二：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cf9db23e82c1c31702966878d7d6326" alt="ComfyUI 混元视频 T2V 工作流" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 文本编码器</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">确保 <strong>DualCLIPLoader</strong> 中加载了：</p>
<ul style="margin: 8px 0 0 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li>clip_name1: clip_l.safetensors</li>
  <li>clip_name2: llava_llama3_fp8_scaled.safetensors</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🧠 扩散模型</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">确保 <strong>Load Diffusion Model</strong> 加载了 <code>hunyuan_video_t2v_720p_bf16.safetensors</code></p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🎨 VAE 模型</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">确保 <strong>Load VAE</strong> 中加载了 <code>hunyuan_video_vae_bf16.safetensors</code></p>
</div>

</div>

#### 🚀 执行生成

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ 点击 Queue 按钮或使用快捷键 Ctrl(Cmd) + Enter 运行工作流</strong>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 生成提示</strong><br>
  <code>EmptyHunyuanLatentVideo</code> 节点的 <code>length</code> 设置为 1 时，该模型可以生成静态图像。
</div>

</div>

## 🖼️ 混元图生视频工作流

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

混元图生视频模型开源于2025年3月6日，基于 HunyuanVideo 框架，支持将静态图像转化为流畅的高质量视频，同时开放了 LoRA 训练代码，支持定制特殊视频效果。

### 🆚 版本对比

目前混元图生视频模型分为两个版本：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">v1 "concat"</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video.webp" alt="HunyuanVideo v1" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">视频的运动流畅性较好，但比较少遵循图像引导</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">v2 "replace"</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video_v2.webp" alt="HunyuanVideo v2" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">图像的引导性较好，但相对于 V1 版本似乎不那么有活力</p>
</div>

</div>

### 🎯 v1 "concat" 图生视频工作流

#### 📥 步骤一：下载工作流和素材

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v1_robot.webp" alt="ComfyUI 工作流 - 混元图生视频v1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载工作流</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 起始帧素材</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/hunyuan-video/i2v/robot-ballet.png" alt="起始帧" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">点击下载起始帧图片</p>
</div>

#### 🔧 步骤二：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66d1fd271cc2a45a4fbcd92850074912" alt="ComfyUI 混元视频I2V v1 工作流" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 文本编码器</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">确保 <strong>DualCLIPLoader</strong> 中加载了：</p>
<ul style="margin: 8px 0 0 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li>clip_name1: clip_l.safetensors</li>
  <li>clip_name2: llava_llama3_fp8_scaled.safetensors</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">👁️ 视觉编码器</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">确保 <strong>Load CLIP Vision</strong> 加载了 <code>llava_llama3_vision.safetensors</code></p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🧠 扩散模型</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">确保 <strong>Load Diffusion Model</strong> 加载了 <code>hunyuan_video_image_to_video_720p_bf16.safetensors</code></p>
</div>

</div>

### ⚡ v2 "replace" 图生视频工作流

#### 📥 步骤一：下载工作流和素材

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v2_fennec_gril.webp" alt="ComfyUI 工作流 - 混元图生视频v2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载工作流</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 起始帧素材</h4>
<img src="https://comfyanonymous.github.io/ComfyUI_examples/flux/flux_dev_example.png" alt="起始帧" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">点击下载起始帧图片</p>
</div>

#### 🔧 步骤二：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f26ddd8edc837fbf9d2bb4f6459a82ee" alt="ComfyUI 混元视频I2V v2 工作流" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

v2 版本的配置与 v1 版本基本相同，主要区别在于扩散模型：

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; margin: 16px 0;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🧠 扩散模型差异</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">确保 <strong>Load Diffusion Model</strong> 加载了 <code>hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors</code></p>
</div>

</div>

## 🎨 创意示例与提示词

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

以下是一些示例图片和对应的提示词，你可以基于这些内容进行修改，创作出属于你自己的视频。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🤖 未来机器人</h4>
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=16d6b0ea15e14c74e8d2e5bfacfe4bf8" alt="未来机器人" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #1e40af;">Futuristic robot dancing ballet, dynamic motion, fast motion, fast shot, moving scene</code>
</div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">⚔️ 武士战斗</h4>
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f8a76a691a7a9ebda088941350538375" alt="武士" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #059669;">Samurai waving sword and hitting the camera. camera angle movement, zoom in, fast scene, super fast, dynamic</code>
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🚗 飞行汽车</h4>
<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aa2ce4f30c4d367170a8a696e62a7c7e" alt="飞行汽车" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #ea580c;">flying car fastly moving and flying through the city</code>
</div>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 12px 0;">🏎️ 赛博朋克赛车</h4>
<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=875b086bd33ac131bda4fe6c718b9bc7" alt="赛博朋克赛车" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<div style="background: #f8fafc; padding: 12px; border-radius: 4px; margin-top: 12px;">
<code style="font-size: 12px; color: #7c3aed;">cyberpunk car race in night city, dynamic, super fast, fast shot</code>
</div>
</div>

</div>

</div>

## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>使用清晰、具体的动作描述词</li>
  <li>图生视频时选择主体明确的起始图像</li>
  <li>合理使用动态关键词如"fast motion"、"dynamic"</li>
  <li>根据需求选择合适的版本（v1流畅性好，v2引导性强）</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>确保有足够的显存运行模型（推荐16GB+）</li>
  <li>生成时间较长，请耐心等待</li>
  <li>复杂场景可能需要多次尝试优化提示词</li>
  <li>首次运行需要下载大量模型文件</li>
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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB</td>
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
      <td style="padding: 12px;">RTX 4080</td>
      <td style="padding: 12px;">RTX 4090 / A100</td>
    </tr>
  </tbody>
</table>
</div>

### 📹 输出规格

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">720p 分辨率</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">5秒视频</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">中英文支持</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">高帧率流畅</span>
  </div>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎬 <strong>ComfyUI 混元视频生成</strong> | 文生视频与图生视频的完整解决方案
  </p>
</div>