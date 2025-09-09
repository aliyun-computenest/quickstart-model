<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎯 ComfyUI Hunyuan3D-2 3D 资产生成</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI 原生工作流 - 从图像到高质量 3D 模型的完整生成流程</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎨 多视角生成</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 高保真纹理</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">⚡ 轻量化部署</span>
  </div>
</div>

## 📋 混元3D 2.0 模型概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

  <div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-2.gif" alt="Hunyuan 3D 2 Demo 2" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

[混元3D 2.0](https://github.com/Tencent/Hunyuan3D-2) 是腾讯推出的开源 3D 资产生成模型，可以通过文本、图像或草图生成带有高分辨率纹理贴图的高保真 3D 模型。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 相关资源</strong><br>
  • <strong>项目仓库</strong>：<a href="https://github.com/Tencent/Hunyuan3D-2" target="_blank" style="color: #2563eb;">GitHub - Hunyuan3D-2</a><br>
  • <strong>模型仓库</strong>：<a href="https://huggingface.co/tencent" target="_blank" style="color: #2563eb;">🤗 Tencent HuggingFace</a>
</div>

### 🏗️ 两阶段生成架构

混元3D 2.0 采用两阶段生成，有效分离了形状和纹理生成的复杂性：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎯 几何生成模型（Hunyuan3D-DiT）</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">基于流扩散的 Transformer 架构，生成无纹理的几何模型，可精准匹配输入条件</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎨 纹理生成模型（Hunyuan3D-Paint）</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">结合几何条件和多视图扩散技术，为模型添加高分辨率纹理，支持 PBR 材质</p>
</div>

</div>

### ✨ 主要优势

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<strong>🎯 高精度生成</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">几何结构锐利，纹理色彩丰富，支持 PBR 材质生成，实现接近真实的光影效果</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🛠️ 多样化使用方式</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">提供代码调用、Blender 插件、Gradio 应用及官网在线体验，适合不同用户需求</p>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⚡ 轻量化与兼容性</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Mini 模型仅需 5GB 显存，标准版本形状生成需 6GB 显存，完整流程仅需 12GB 显存</p>
</div>

</div>

### 🆕 最新更新

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📅 2025年3月18日更新</strong><br>
  混元3D 2.0 新增多视角形状生成模型（Hunyuan3D-2mv），支持从不同视角输入生成更精细的几何结构。
</div>

</div>

## 🚀 工作流示例概览

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

本示例包含三个完整的工作流，涵盖不同的使用场景：

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Hunyuan3D-2mv</h4>
<p style="margin: 0; color: #1e40af;">多视角输入生成高精度 3D 模型</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">⚡</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Hunyuan3D-2mv-turbo</h4>
<p style="margin: 0; color: #065f46;">快速多视角生成，分步蒸馏优化</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🖼️</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Hunyuan3D-2</h4>
<p style="margin: 0; color: #9a3412;">单视图输入的标准 3D 生成</p>
</div>

</div>

</div>

### ⚠️ 环境要求

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 使用前请确认</strong><br>
  • 确保 ComfyUI 已更新到最新版本，原生支持 Hunyuan3D-2mv<br>
  • 目前暂未支持纹理和材质的生成功能<br>
  • 工作流图片的 Metadata 中包含完整的工作流 JSON<br>
  • 生成的 .glb 格式模型将输出至 <code>ComfyUI/output/mesh</code> 文件夹
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">


<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🔧 常见问题</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>节点缺失：版本过旧或导入失败</li>
  <li>功能不全：使用稳定版而非开发版</li>
  <li>加载失败：启动时节点导入异常</li>
</ul>
</div>

</div>

## 🎯 工作流一：Hunyuan3D-2mv 多视角生成

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Hunyuan3D-2mv 工作流支持使用多视角图片生成 3D 模型。多个视角的图片并非必须，也可以仅输入 `front` 视角的图片来生成 3D 模型。

### 📥 步骤一：下载工作流和素材

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/hunyuan-3d-multiview-elf.webp" alt="Hunyuan3D-2mv workflow" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载，拖入 ComfyUI 加载工作流</p>
</div>

### 📁 多视角输入素材

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Front View</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/front.png" alt="Front view" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🖼️ Left View</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/left.png" alt="Left view" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #7c3aed; margin: 0 0 12px 0;">🖼️ Back View</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/back.png" alt="Back view" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 素材处理提示</strong><br>
  示例中的输入图片已预处理去除背景。实际使用中，可借助 <a href="https://github.com/cubiq/ComfyUI_essentials" target="_blank" style="color: #2563eb;">ComfyUI_essentials</a> 等自定义节点自动去除背景。
</div>

### 🔗 步骤二：模型下载

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── hunyuan3d-dit-v2-mv.safetensors  // 重命名后的文件</code></pre>
</div>

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">模型名称</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">下载链接</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">重命名为</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; font-weight: 500;">hunyuan3d-dit-v2-mv</td>
      <td style="padding: 12px;">
        <a href="https://huggingface.co/tencent/Hunyuan3D-2mv/resolve/main/hunyuan3d-dit-v2-mv/model.fp16.safetensors?download=true" target="_blank" style="color: #2563eb;">model.fp16.safetensors</a>
      </td>
      <td style="padding: 12px; font-family: monospace; font-size: 12px;">hunyuan3d-dit-v2-mv.safetensors</td>
    </tr>
  </tbody>
</table>
</div>

### 🔧 步骤三：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17e6ac738f0e0133536bceb6e3ea1b56" alt="ComfyUI hunyuan3d_2mv" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 模型加载</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">确保 <strong>Image Only Checkpoint Loader</strong> 节点加载了重命名后的 <code>hunyuan3d-dit-v2-mv.safetensors</code> 模型</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 图片加载</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">在各个 <strong>Load Image</strong> 节点中加载对应视角的图片</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 执行生成</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">点击 <strong>Queue</strong> 按钮或使用快捷键 <strong>Ctrl+Enter</strong> 运行工作流</p>
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 扩展视角</strong><br>
  如需增加更多视角，请确保 <code>Hunyuan3Dv2ConditioningMultiView</code> 节点和对应的 <code>Load Image</code> 节点都加载了相应视角的图片。
</div>

</div>

## ⚡ 工作流二：Hunyuan3D-2mv-turbo 快速生成

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Hunyuan3D-2mv-turbo 是 Hunyuan3D-2mv 的分步蒸馏（Step Distillation）版本，可以更快地生成 3D 模型。在此版本中，设置 `cfg` 为 1.0 并添加 `flux guidance` 节点来控制 `distilled cfg` 的生成。

### 📁 多视角输入素材

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Front View</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/front.png" alt="Front view" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<h4 style="color: #ea580c; margin: 0 0 12px 0;">🖼️ Right View</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/right.png" alt="Right view" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>

</div>


### 🔧 步骤二：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33bb861fd695fd4b10a53345f004d2cc" alt="ComfyUI hunyuan3d_2mv_turbo" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 模型加载</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">确保 <strong>Image Only Checkpoint Loader</strong> 节点加载了 <code>hunyuan3d-dit-v2-mv-turbo.safetensors</code> 模型</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 图片加载</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">在各个 <strong>Load Image</strong> 节点中加载对应视角的图片</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 执行生成</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">点击 <strong>Queue</strong> 按钮或使用快捷键 <strong>Ctrl+Enter</strong> 运行工作流</p>
</div>

</div>

</div>

## 🖼️ 工作流三：Hunyuan3D-2 单视图生成

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Hunyuan3D-2 工作流使用单视图输入生成 3D 模型。在此工作流中，使用 `Hunyuan3Dv2Conditioning` 节点替换 `Hunyuan3Dv2ConditioningMultiView` 节点。

### 📥 步骤一：下载工作流和素材

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d-non-multiview-train.webp" alt="Hunyuan3D-2 workflow" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">点击图片下载，拖入 ComfyUI 加载工作流</p>
</div>

### 📁 单视图输入素材

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ 输入图像</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan_3d_v2_non_multiview_train.png" alt="Single view input" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>


### 🔧 步骤二：工作流配置

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33c158fcfb133560674aa56bfdb5087d" alt="ComfyUI hunyuan3d_2" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 配置步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 模型加载</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">确保 <strong>Image Only Checkpoint Loader</strong> 节点加载了 <code>hunyuan3d-dit-v2.safetensors</code> 模型</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 图片加载</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">在 <strong>Load Image</strong> 节点中加载输入图片</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 执行生成</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">点击 <strong>Queue</strong> 按钮或使用快捷键 <strong>Ctrl+Enter</strong> 运行工作流</p>
</div>

</div>

</div>

## 🛠️ 社区资源

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

以下是 Hunyuan3D-2 相关的 ComfyUI 社区资源：

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🔧 ComfyUI-Hunyuan3DWrapper</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">
  <a href="https://github.com/kijai/ComfyUI-Hunyuan3DWrapper" target="_blank" style="color: #2563eb;">GitHub 仓库</a> - 完整的 Hunyuan3D 包装器
</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>📦 预处理模型</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">
  <a href="https://huggingface.co/Kijai/Hunyuan3D-2_safetensors/tree/main" target="_blank" style="color: #059669;">Kijai/Hunyuan3D-2_safetensors</a> - 预处理的 safetensors 格式模型
</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🎯 ComfyUI-3D-Pack</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">
  <a href="https://github.com/MrForExample/ComfyUI-3D-Pack" target="_blank" style="color: #ea580c;">GitHub 仓库</a> - 综合 3D 生成工具包
</p>
</div>

</div>

</div>


## 💡 使用技巧与建议

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 最佳实践</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>使用去背景的高质量输入图像</li>
  <li>多视角输入时确保视角一致性</li>
  <li>根据显存情况选择合适的模型版本</li>
  <li>优先使用 turbo 版本进行快速预览</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ 注意事项</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>确保 ComfyUI 版本为最新开发版</li>
  <li>输入图像需要清晰的主体轮廓</li>
  <li>多视角图像应保持主体一致性</li>
  <li>生成过程需要足够的显存支持</li>
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
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">模型版本</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">显存要求</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">推荐配置</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Hunyuan3D-2mini</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">5GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">RTX 3060 12GB</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Hunyuan3D-2 (形状生成)</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">6GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">RTX 4060 Ti 16GB</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Hunyuan3D-2 (完整流程)</td>
      <td style="padding: 12px;">12GB</td>
      <td style="padding: 12px;">RTX 4070 Ti / RTX 4080</td>
    </tr>
  </tbody>
</table>
</div>

### 📐 支持的输出格式

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">.glb 格式</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">PBR 材质</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">高分辨率纹理</span>
  </div>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎯 <strong>ComfyUI Hunyuan3D-2 3D 资产生成</strong> | 从图像到高质量 3D 模型的完整解决方案
  </p>
</div>