<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎮 Wan2.2-Fun-Control 视频控制生成</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 多模态控制条件的精准视频生成</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 多模态控制</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 影视级质量</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🌐 多语言支持</span>
  </div>
</div>

## 📋 模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Wan2.2-Fun-Control** 是 Alibaba PAI 团队推出的新一代视频生成与控制模型，通过引入创新性的控制代码（Control Codes）机制，结合深度学习和多模态条件输入，能够生成高质量且符合预设控制条件的视频。该模型采用 **Apache 2.0 许可协议**发布，支持商业使用。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>🎯 多模态控制</strong><br>
    <p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">支持 Canny、Depth、OpenPose、MLSD 等多种控制条件</p>
  </div>

  <div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎬 高质量视频生成</strong><br>
    <p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">基于 Wan2.2 架构，输出影视级质量视频</p>
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>🌐 多语言支持</strong><br>
    <p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">支持中英文等多语言提示词输入</p>
  </div>

  <div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>🎮 轨迹控制</strong><br>
    <p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">支持精确的运动轨迹控制功能</p>
  </div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 相关资源</strong><br>
  • <strong>模型仓库</strong>：<a href="https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control" target="_blank" style="color: #2563eb;">🤗 Wan2.2-Fun-A14B-Control</a><br>
  • <strong>代码仓库</strong>：<a href="https://github.com/aigc-apps/VideoX-Fun" target="_blank" style="color: #2563eb;">VideoX-Fun</a>
</div>

</div>

## 🎥 ComfyOrg Wan2.2 Fun Control 直播回放

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

针对 ComfyUI Wan2.2 的使用，已进行了专门的直播演示，可以通过以下回放了解详细的使用方法和控制技巧。

<div style="text-align: center; margin: 20px 0;">
  <iframe style="width: 100%; aspect-ratio: 16/9; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="//player.bilibili.com/player.html?isOutside=true&aid=115027747082114&bvid=BV1DVbrzdEFR&cid=31697013072&p=1&autoplay=0" title="ComfyUI Wan2.2 Fun Control 使用教程" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

</div>

## 🚀 Wan2.2 Fun Control 工作流示例

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

### 🔧 工作流版本说明

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

提供两个版本的工作流供选择：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">⚡ Lightning 加速版</h4>
<p style="margin: 0 0 8px 0; color: #1e40af; font-size: 14px;">使用 <a href="https://huggingface.co/lightx2v/Wan2.2-Lightning" target="_blank" style="color: #2563eb;">Wan2.2-Lightning</a> 4步 LoRA</p>
<div style="background: #dcfce7; color: #059669; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block; margin-right: 8px;">✅ 速度更快</div>
<div style="background: #fed7aa; color: #ea580c; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block;">⚠️ 动态损失</div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎯 标准质量版</h4>
<p style="margin: 0 0 8px 0; color: #065f46; font-size: 14px;">使用 fp8_scaled 版本，无加速 LoRA</p>
<div style="background: #dcfce7; color: #059669; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block; margin-right: 8px;">✅ 质量更高</div>
<div style="background: #fed7aa; color: #ea580c; padding: 4px 12px; border-radius: 12px; font-size: 12px; display: inline-block;">⏱️ 耗时更长</div>
</div>

</div>

#### 📊 性能对比测试

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🧪 测试环境</strong>：RTX 4090D 24GB 显存，640×640 分辨率，81 帧长度
</div>

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">模型类型</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">分辨率</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">显存占用</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">首次生成</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">第二次生成</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">fp8_scaled</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">640×640</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">83%</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 524秒</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">≈ 520秒</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">fp8_scaled + 4步LoRA</td>
      <td style="padding: 12px;">640×640</td>
      <td style="padding: 12px;">89%</td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 138秒</span></td>
      <td style="padding: 12px;"><span style="background: #dcfce7; color: #059669; padding: 2px 8px; border-radius: 4px; font-size: 12px;">≈ 79秒</span></td>
    </tr>
  </tbody>
</table>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 版本切换说明</strong><br>
  由于 4 步 LoRA 对初次使用工作流的用户体验较好，默认启用加速版本。如需切换到标准版本，框选对应工作流后使用 <strong>Ctrl+B</strong> 即可启用。
</div>

</div>

### 📥 步骤一：工作流及素材下载

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

下载以下视频或 JSON 文件并拖入 ComfyUI 中以加载对应的工作流。

<div style="text-align: center; margin: 20px 0;">
  <video controls style="width: 100%; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/wan2.2_14B_fun_inp.mp4"></video>
</div>

<div style="text-align: center; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_fun_control.json" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
    📄 下载 JSON 格式工作流
  </a>
</div>

### 📁 示例素材下载

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 输入起始图片</h4>
<div style="text-align: center; margin: 12px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/input.jpg" alt="输入起始图片" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🎬 控制视频</h4>
<div style="text-align: center; margin: 12px 0;">
  <video controls style="width: 100%; max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/control_video.mp4"></video>
</div>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 13px;">此视频已经过预处理，可直接用于控制视频生成</p>
</div>

</div>

</div>

### 🔗 步骤二：模型文件



#### 📂 模型文件结构

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors
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
  <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1c5d26bea52f7f790ac6059e7a195c8d" alt="Wan2.2 Fun Control 工作流步骤" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 重要提醒</strong><br>
  此工作流使用了 LoRA 加速版本，请确保对应的 Diffusion Model 和 LoRA 文件保持一致，high noise 和 low noise 的模型和 LoRA 需要对应使用。
</div>

#### 📋 详细配置步骤

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 12px 0;">🔧 High Noise 模型配置</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>：<br><code>wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors</code></li>
  <li><strong>LoraLoaderModelOnly</strong>：<br><code>wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🔧 Low Noise 模型配置</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>：<br><code>wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors</code></li>
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

#### 📁 输入配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ 起始帧上传</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">在 <strong>Load Image</strong> 节点上传起始帧图片</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎬 控制视频上传</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">在第二个 <strong>Load Video</strong> 节点上传控制视频的 pose 视频</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🔧 预处理节点禁用</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">由于提供的视频已预处理，需要禁用对应的预处理节点（选中后使用 <strong>Ctrl+B</strong>）</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">📝 提示词修改</h4>
<p style="margin: 0; color: #5b21b6; font-size: 14px;">修改 Prompt，支持中英文输入</p>
</div>

</div>

#### ⚙️ 参数调整

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎬 Wan22FunControlToVideo 节点配置</strong><br>
  • 修改对应视频的尺寸参数<br>
  • 默认设置了 640×640 的分辨率，避免低显存用户使用时过于耗时<br>
  • 可根据需要调整为更高分辨率
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

# Configuration Parameters - Wan2.2 Fun Control Specific
COMFYUI_SERVER = "127.0.0.1:8188"  # Local server
COMFYUI_TOKEN = ""  # Usually no token needed for local

# Model Configuration
HIGH_NOISE_UNET = "wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors"
LOW_NOISE_UNET = "wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors"
CLIP_MODEL = "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
VAE_MODEL = "wan_2.1_vae.safetensors"
HIGH_NOISE_LORA = "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"
LOW_NOISE_LORA = "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"

# Default Parameters
DEFAULT_POSITIVE_PROMPT = "On a sunny summer day, there are marshmallow - like clouds, and the sunlight is bright and warm. A girl with white curly double - ponytails is wearing unique sunglasses, distinctive clothes and shoes. Her posture is natural and full of dynamic tension. The background is the scene of the Leaning Tower of Pisa in Italy, emphasizing the realistic contrast of details in reality. The whole picture is in a realistic 3D style, rich in details and with a relaxed atmosphere. She is dancing slowly, waving her hands."

DEFAULT_NEGATIVE_PROMPT = "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"

DEFAULT_REF_IMAGE = "fun_control.jpg"
DEFAULT_CONTROL_VIDEO = "control_video.mp4"

class ComfyUIWan22FunControlClient:
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

    def upload_video(self, video_path):
        """Upload video to ComfyUI server"""
        try:
            with open(video_path, 'rb') as f:
                files = {'video': f}
                response = requests.post(f"{self.base_url}/upload/video", files=files)
                if response.status_code == 200:
                    result = response.json()
                    return result.get('name', os.path.basename(video_path))
                else:
                    raise Exception(f"Failed to upload video: {response.text}")
        except Exception as e:
            print(f"Video upload error: {e}")
            return None

    def generate_fun_control_video(self, positive_prompt, negative_prompt=None,
                                  ref_image_path=None, ref_image_name=None,
                                  control_video_path=None, control_video_name=None,
                                  width=640, height=640, length=81, fps=16,
                                  steps=4, cfg=1, seed=None,
                                  canny_low_threshold=0.1, canny_high_threshold=0.6,
                                  shift=8.0, lora_strength=1.0):
        """Generate Fun Control video using Wan2.2 based on original JSON workflow"""
        print("Starting Wan2.2 Fun Control video generation...")
        
        # Use default negative prompt if not provided
        if negative_prompt is None:
            negative_prompt = DEFAULT_NEGATIVE_PROMPT
            
        # Generate random seed if not provided
        if seed is None:
            seed = random.randint(1, 1000000000000000)

        # Handle reference image
        if ref_image_path and not ref_image_name:
            ref_image_name = self.upload_image(ref_image_path)
            if not ref_image_name:
                raise Exception("Failed to upload reference image")
        elif not ref_image_name:
            ref_image_name = DEFAULT_REF_IMAGE

        # Handle control video
        if control_video_path and not control_video_name:
            control_video_name = self.upload_video(control_video_path)
            if not control_video_name:
                raise Exception("Failed to upload control video")
        elif not control_video_name:
            control_video_name = DEFAULT_CONTROL_VIDEO

        # Workflow based on your provided JSON
        workflow = {
            "162": {
                "inputs": {
                    "text": negative_prompt,
                    "clip": ["167", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {"title": "CLIP Text Encode (Negative Prompt)"}
            },
            "163": {
                "inputs": {
                    "fps": fps,
                    "images": ["164", 0]
                },
                "class_type": "CreateVideo",
                "_meta": {"title": "Create Video"}
            },
            "164": {
                "inputs": {
                    "samples": ["175", 0],
                    "vae": ["168", 0]
                },
                "class_type": "VAEDecode",
                "_meta": {"title": "VAE Decode"}
            },
            "165": {
                "inputs": {
                    "unet_name": HIGH_NOISE_UNET,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader (High Noise)"}
            },
            "166": {
                "inputs": {
                    "unet_name": LOW_NOISE_UNET,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {"title": "UNet Loader (Low Noise)"}
            },
            "167": {
                "inputs": {
                    "clip_name": CLIP_MODEL,
                    "type": "wan",
                    "device": "default"
                },
                "class_type": "CLIPLoader",
                "_meta": {"title": "CLIP Loader"}
            },
            "168": {
                "inputs": {
                    "vae_name": VAE_MODEL
                },
                "class_type": "VAELoader",
                "_meta": {"title": "VAE Loader"}
            },
            "169": {
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
                    "model": ["176", 0],
                    "positive": ["180", 0],
                    "negative": ["180", 1],
                    "latent_image": ["180", 2]
                },
                "class_type": "KSamplerAdvanced",
                "_meta": {"title": "K Sampler Advanced (High Noise)"}
            },
            "170": {
                "inputs": {
                    "filename_prefix": "wan22_fun_control/video",
                    "format": "auto",
                    "codec": "auto",
                    "video": ["163", 0]
                },
                "class_type": "SaveVideo",
                "_meta": {"title": "Save Video"}
            },
            "171": {
                "inputs": {
                    "video": ["174", 0]
                },
                "class_type": "GetVideoComponents",
                "_meta": {"title": "Get Video Components"}
            },
            "172": {
                "inputs": {
                    "images": ["173", 0]
                },
                "class_type": "PreviewImage",
                "_meta": {"title": "Preview Image"}
            },
            "173": {
                "inputs": {
                    "low_threshold": canny_low_threshold,
                    "high_threshold": canny_high_threshold,
                    "image": ["171", 0]
                },
                "class_type": "Canny",
                "_meta": {"title": "Canny Edge Detection"}
            },
            "174": {
                "inputs": {
                    "file": control_video_name,
                    "video-preview": ""
                },
                "class_type": "LoadVideo",
                "_meta": {"title": "Load Video"}
            },
            "175": {
                "inputs": {
                    "add_noise": "disable",
                    "noise_seed": 0,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "start_at_step": 2,
                    "end_at_step": 4,
                    "return_with_leftover_noise": "disable",
                    "model": ["177", 0],
                    "positive": ["180", 0],
                    "negative": ["180", 1],
                    "latent_image": ["169", 0]
                },
                "class_type": "KSamplerAdvanced",
                "_meta": {"title": "K Sampler Advanced (Low Noise)"}
            },
            "176": {
                "inputs": {
                    "shift": shift,
                    "model": ["181", 0]
                },
                "class_type": "ModelSamplingSD3",
                "_meta": {"title": "Model Sampling SD3 (High Noise)"}
            },
            "177": {
                "inputs": {
                    "shift": shift,
                    "model": ["182", 0]
                },
                "class_type": "ModelSamplingSD3",
                "_meta": {"title": "Model Sampling SD3 (Low Noise)"}
            },
            "178": {
                "inputs": {
                    "image": ref_image_name
                },
                "class_type": "LoadImage",
                "_meta": {"title": "Load Reference Image"}
            },
            "179": {
                "inputs": {
                    "text": positive_prompt,
                    "clip": ["167", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {"title": "CLIP Text Encode (Positive Prompt)"}
            },
            "180": {
                "inputs": {
                    "width": width,
                    "height": height,
                    "length": length,
                    "batch_size": 1,
                    "positive": ["179", 0],
                    "negative": ["162", 0],
                    "vae": ["168", 0],
                    "ref_image": ["178", 0],
                    "control_video": ["173", 0]
                },
                "class_type": "Wan22FunControlToVideo",
                "_meta": {"title": "Wan22 Fun Control To Video"}
            },
            "181": {
                "inputs": {
                    "lora_name": HIGH_NOISE_LORA,
                    "strength_model": lora_strength,
                    "model": ["165", 0]
                },
                "class_type": "LoraLoaderModelOnly",
                "_meta": {"title": "LoRA Loader (High Noise)"}
            },
            "182": {
                "inputs": {
                    "lora_name": LOW_NOISE_LORA,
                    "strength_model": lora_strength,
                    "model": ["166", 0]
                },
                "class_type": "LoraLoaderModelOnly",
                "_meta": {"title": "LoRA Loader (Low Noise)"}
            }
        }

        print("Submitting Wan2.2 Fun Control video generation workflow...")
        print(f"Positive Prompt: {positive_prompt}")
        print(f"Reference Image: {ref_image_name}")
        print(f"Control Video: {control_video_name}")
        print(f"Video Dimensions: {width}x{height}")
        print(f"Video Length: {length} frames")
        print(f"FPS: {fps}")
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

    def download_video(self, task_id, output_dir="outputs"):
        """Download generated video and preview files"""
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

    def generate_batch(self, prompt_configs, **kwargs):
        """Batch generate videos with different configurations"""
        results = []
        
        for i, config in enumerate(prompt_configs):
            print(f"\nStarting Fun Control video generation task {i+1}/{len(prompt_configs)}...")
            
            try:
                task_id, seed = self.generate_fun_control_video(**config, **kwargs)
                
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
                    
                    time.sleep(15)  # Video generation takes longer
                    
            except Exception as e:
                print(f"Task {i+1} error: {e}")
        
        return results

def main():
    """Main function - Execute Wan2.2 Fun Control video generation"""
    client = ComfyUIWan22FunControlClient()
    
    try:
        print("Wan2.2 Fun Control video generation client started...")
        
        # Single video generation example
        print("\n=== Single Fun Control Video Generation ===")
        
        # You can provide local file paths or use existing file names
        ref_image_path = None  # Set to your image path, e.g., "reference.jpg"
        control_video_path = None  # Set to your video path, e.g., "control.mp4"
        
        task_id, seed = client.generate_fun_control_video(
            positive_prompt=DEFAULT_POSITIVE_PROMPT,
            negative_prompt=DEFAULT_NEGATIVE_PROMPT,
            ref_image_path=ref_image_path,
            ref_image_name=DEFAULT_REF_IMAGE,
            control_video_path=control_video_path,
            control_video_name=DEFAULT_CONTROL_VIDEO,
            width=640,
            height=640,
            length=81,
            fps=16,
            steps=4,
            cfg=1
        )
        
        print(f"Task ID: {task_id}")
        print(f"Seed: {seed}")

        # Wait for task completion (video generation takes longer)
        while True:
            status = client.get_status(task_id)
            print(f"Current status: {status}")
            
            if status == "completed":
                print("Fun Control video generation completed!")
                break
            elif status == "failed":
                print("Generation failed!")
                return
            
            time.sleep(15)

        # Download video and preview files
        downloaded_files = client.download_video(task_id)
        if downloaded_files:
            print(f"Successfully downloaded {len(downloaded_files)} files!")
            for file in downloaded_files:
                print(f"File path: {file}")
        else:
            print("Download failed")

        # Batch generation example
        print("\n=== Batch Generation Example ===")
        batch_configs = [
            {
                'positive_prompt': "A dancer performing ballet in a beautiful garden with flowers",
                'ref_image_name': DEFAULT_REF_IMAGE,
                'control_video_name': DEFAULT_CONTROL_VIDEO,
                'width': 640,
                'height': 640,
                'length': 49
            },
            {
                'positive_prompt': "A person walking through a bustling city street at sunset",
                'ref_image_name': DEFAULT_REF_IMAGE,
                'control_video_name': DEFAULT_CONTROL_VIDEO,
                'width': 640,
                'height': 640,
                'length': 65
            }
        ]
        
        # Uncomment to run batch generation
        # batch_results = client.generate_batch(batch_configs, fps=16, steps=4)
        # print(f"Batch generation completed, generated {len(batch_results)} videos")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


```

</details>


## 🎯 控制类型详解

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">✏️</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Canny（线稿）</h4>
<p style="margin: 0; color: #1e40af;">边缘检测控制，适用于轮廓和线条控制</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🏔️</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Depth（深度）</h4>
<p style="margin: 0; color: #065f46;">深度信息控制，保持场景的空间结构</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🤸</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">OpenPose（人体姿势）</h4>
<p style="margin: 0; color: #9a3412;">人体骨骼点控制，精确控制人物动作</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">📐</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">MLSD（几何边缘）</h4>
<p style="margin: 0; color: #5b21b6;">几何线条检测，适用于建筑和结构控制</p>
</div>

</div>

## 💡 补充说明与扩展

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🔧 预处理器扩展

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📦 ComfyUI-comfyui_controlnet_aux</strong><br>
  由于 ComfyUI 自带的节点中，预处理器节点只有 Canny 的预处理器，可以使用 <a href="https://github.com/Fannovel16/comfyui_controlnet_aux" target="_blank" style="color: #2563eb;">ComfyUI-comfyui_controlnet_aux</a> 来实现其他类型的图像预处理。
</div>

### 🎨 支持的预处理类型

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Canny Edge</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Depth Map</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">OpenPose</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">MLSD Lines</span>
  </div>
  <div style="background: #fef3c7; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Normal Map</span>
  </div>
  <div style="background: #fef2f2; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #dc2626; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Segmentation</span>
  </div>
</div>

</div>

## 🎯 应用场景

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">动画制作</h4>
<p style="margin: 0; color: #1e40af;">精确控制角色动作和场景变化</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">艺术创作</h4>
<p style="margin: 0; color: #065f46;">将静态艺术作品转换为动态表现</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏃</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">运动分析</h4>
<p style="margin: 0; color: #9a3412;">体育动作分析和训练视频制作</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🏗️</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">建筑可视化</h4>
<p style="margin: 0; color: #5b21b6;">建筑设计的动态展示和漫游</p>
</div>

</div>

## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>选择合适的控制类型匹配内容需求</li>
  <li>确保控制视频质量清晰稳定</li>
  <li>根据显存情况选择合适的分辨率</li>
  <li>提示词要与控制内容保持一致</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>确保 High/Low Noise 模型与 LoRA 匹配</li>
  <li>预处理视频时注意禁用对应节点</li>
  <li>控制视频帧率要与目标视频匹配</li>
  <li>复杂控制可能需要更多计算资源</li>
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

### 🎬 支持的控制精度

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🎯 精确控制</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>OpenPose</strong>: 关节点级别精度</li>
  <li><strong>Depth</strong>: 像素级深度控制</li>
  <li><strong>Canny</strong>: 边缘轮廓控制</li>
</ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">⚡ 性能优化</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>Lightning LoRA</strong>: 4倍速度提升</li>
  <li><strong>FP8 量化</strong>: 显存优化</li>
  <li><strong>批处理</strong>: 多视频并行</li>
</ul>
</div>

</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎮 <strong>Wan2.2-Fun-Control 视频控制生成</strong> | 多模态控制条件的精准视频创作
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Alibaba PAI 团队 | Apache 2.0 开源协议 | 让每一帧都在精确控制之下
  </p>
</div>