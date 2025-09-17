<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎯 ComfyUI Hunyuan3D-2 3D Asset Generation</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI Native Workflow - Complete Pipeline from Images to High-Quality 3D Models</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎨 Multi-View Generation</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎬 High-Fidelity Textures</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">⚡ Lightweight Deployment</span>
  </div>
</div>

## 📋 Hunyuan3D 2.0 Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

  <div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-2.gif" alt="Hunyuan 3D 2 Demo 2" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

[Hunyuan3D 2.0](https://github.com/Tencent/Hunyuan3D-2) is an open-source 3D asset generation model launched by Tencent that can generate high-fidelity 3D models with high-resolution texture maps through text, images, or sketches.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔗 Related Resources</strong><br>
  • <strong>Project Repository</strong>: <a href="https://github.com/Tencent/Hunyuan3D-2" target="_blank" style="color: #2563eb;">GitHub - Hunyuan3D-2</a><br>
  • <strong>Model Repository</strong>: <a href="https://huggingface.co/tencent" target="_blank" style="color: #2563eb;">🤗 Tencent HuggingFace</a>
</div>

### 🏗️ Two-Stage Generation Architecture

Hunyuan3D 2.0 adopts a two-stage generation approach that effectively separates the complexity of shape and texture generation:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎯 Geometry Generation Model (Hunyuan3D-DiT)</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Based on flow diffusion Transformer architecture, generates texture-free geometric models that precisely match input conditions</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎨 Texture Generation Model (Hunyuan3D-Paint)</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Combines geometric conditions and multi-view diffusion techniques to add high-resolution textures to models, supporting PBR materials</p>
</div>

</div>

### ✨ Key Advantages

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<strong>🎯 High-Precision Generation</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Sharp geometric structures, rich texture colors, supports PBR material generation, achieving near-realistic lighting effects</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🛠️ Diverse Usage Methods</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Provides code calls, Blender plugins, Gradio applications, and official website online experience, suitable for different user needs</p>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⚡ Lightweight & Compatibility</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Mini model requires only 5GB VRAM, standard version shape generation needs 6GB VRAM, complete pipeline only needs 12GB VRAM</p>
</div>

</div>

### 🆕 Latest Updates

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📅 March 18, 2025 Update</strong><br>
  Hunyuan3D 2.0 adds multi-view shape generation model (Hunyuan3D-2mv), supporting input from different viewpoints to generate more refined geometric structures.
</div>

</div>

## 🚀 Workflow Examples Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

workflow template can be seen in 
![img_1.png](img_1.png)

This example includes three complete workflows covering different usage scenarios:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Hunyuan3D-2mv</h4>
<p style="margin: 0; color: #1e40af;">Multi-view input generates high-precision 3D models</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">⚡</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Hunyuan3D-2mv-turbo</h4>
<p style="margin: 0; color: #065f46;">Fast multi-view generation with step distillation optimization</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🖼️</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Hunyuan3D-2</h4>
<p style="margin: 0; color: #9a3412;">Standard 3D generation from single-view input</p>
</div>

</div>

</div>

### ⚠️ Environment Requirements

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 Pre-usage Checklist</strong><br>
  • Ensure ComfyUI is updated to the latest version with native Hunyuan3D-2mv support<br>
  • Currently does not support texture and material generation features<br>
  • Workflow image metadata contains complete workflow JSON<br>
  • Generated .glb format models will be output to <code>ComfyUI/output/mesh</code> folder
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🔧 Common Issues</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Missing nodes: Version too old or import failed</li>
  <li>Incomplete features: Using stable version instead of dev version</li>
  <li>Loading failure: Node import exception during startup</li>
</ul>
</div>

</div>

## 🎯 Workflow 1: Hunyuan3D-2mv Multi-View Generation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

The Hunyuan3D-2mv workflow supports generating 3D models using multi-view images. Multiple viewpoint images are not mandatory; you can also input only the `front` view image to generate 3D models.

### 📥 Step 1: Download Workflow and Materials

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/hunyuan-3d-multiview-elf.webp" alt="Hunyuan3D-2mv workflow" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download, drag into ComfyUI to load workflow</p>
</div>

### 📁 Multi-View Input Materials

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
  <strong>💡 Material Processing Tips</strong><br>
  The input images in the example have been pre-processed to remove backgrounds. In actual use, you can use custom nodes like <a href="https://github.com/cubiq/ComfyUI_essentials" target="_blank" style="color: #2563eb;">ComfyUI_essentials</a> to automatically remove backgrounds.
</div>



### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17e6ac738f0e0133536bceb6e3ea1b56" alt="ComfyUI hunyuan3d_2mv" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Model Loading</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Ensure the <strong>Image Only Checkpoint Loader</strong> node loads the renamed <code>hunyuan3d-dit-v2-mv.safetensors</code> model</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 Image Loading</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Load corresponding viewpoint images in each <strong>Load Image</strong> node</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 Execute Generation</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Click <strong>Queue</strong> button or use shortcut <strong>Ctrl+Enter</strong> to run workflow</p>
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Extended Views</strong><br>
  To add more viewpoints, ensure both the <code>Hunyuan3Dv2ConditioningMultiView</code> node and corresponding <code>Load Image</code> nodes load images for the respective viewpoints.
</div>

</div>

## ⚡ Workflow 2: Hunyuan3D-2mv-turbo Fast Generation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Hunyuan3D-2mv-turbo is a step distillation version of Hunyuan3D-2mv that can generate 3D models faster. In this version, set `cfg` to 1.0 and add a `flux guidance` node to control `distilled cfg` generation.

### 📁 Multi-View Input Materials

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

### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33bb861fd695fd4b10a53345f004d2cc" alt="ComfyUI hunyuan3d_2mv_turbo" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Model Loading</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Ensure the <strong>Image Only Checkpoint Loader</strong> node loads the <code>hunyuan3d-dit-v2-mv-turbo.safetensors</code> model</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 Image Loading</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Load corresponding viewpoint images in each <strong>Load Image</strong> node</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 Execute Generation</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Click <strong>Queue</strong> button or use shortcut <strong>Ctrl+Enter</strong> to run workflow</p>
</div>

</div>

</div>

## 🖼️ Workflow 3: Hunyuan3D-2 Single-View Generation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

The Hunyuan3D-2 workflow uses single-view input to generate 3D models. In this workflow, the `Hunyuan3Dv2Conditioning` node replaces the `Hunyuan3Dv2ConditioningMultiView` node.

### 📥 Step 1: Download Workflow and Materials

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d-non-multiview-train.webp" alt="Hunyuan3D-2 workflow" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download, drag into ComfyUI to load workflow</p>
</div>

### 📁 Single-View Input Material

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🖼️ Input Image</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan_3d_v2_non_multiview_train.png" alt="Single view input" style="max-width: 300px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</div>


### 🔧 Step 2: Workflow Configuration

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33c158fcfb133560674aa56bfdb5087d" alt="ComfyUI hunyuan3d_2" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Model Loading</h4>
<p style="margin: 0; color: #1e40af; font-size: 14px;">Ensure the <strong>Image Only Checkpoint Loader</strong> node loads the <code>hunyuan3d-dit-v2.safetensors</code> model</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 Image Loading</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Load the input image in the <strong>Load Image</strong> node</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚀 Execute Generation</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Click <strong>Queue</strong> button or use shortcut <strong>Ctrl+Enter</strong> to run workflow</p>
</div>

</div>

</div>

## 🛠️ Community Resources

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Here are Hunyuan3D-2 related ComfyUI community resources:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🔧 ComfyUI-Hunyuan3DWrapper</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">
  <a href="https://github.com/kijai/ComfyUI-Hunyuan3DWrapper" target="_blank" style="color: #2563eb;">GitHub Repository</a> - Complete Hunyuan3D wrapper
</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>📦 Pre-processed Models</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">
  <a href="https://huggingface.co/Kijai/Hunyuan3D-2_safetensors/tree/main" target="_blank" style="color: #059669;">Kijai/Hunyuan3D-2_safetensors</a> - Pre-processed safetensors format models
</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🎯 ComfyUI-3D-Pack</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">
  <a href="https://github.com/MrForExample/ComfyUI-3D-Pack" target="_blank" style="color: #ea580c;">GitHub Repository</a> - Comprehensive 3D generation toolkit
</p>
</div>

</div>

</div>

## 💡 Usage Tips and Recommendations

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Best Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>Use background-removed high-quality input images</li>
  <li>Ensure viewpoint consistency for multi-view inputs</li>
  <li>Choose appropriate model version based on VRAM capacity</li>
  <li>Prioritize turbo version for quick previews</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ Important Notes</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Ensure ComfyUI version is the latest development version</li>
  <li>Input images need clear subject outlines</li>
  <li>Multi-view images should maintain subject consistency</li>
  <li>Generation process requires sufficient VRAM support</li>
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
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Model Version</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">VRAM Requirement</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Recommended Configuration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Hunyuan3D-2mini</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">5GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">RTX 3060 12GB</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Hunyuan3D-2 (Shape Generation)</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">6GB</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">RTX 4060 Ti 16GB</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Hunyuan3D-2 (Complete Pipeline)</td>
      <td style="padding: 12px;">12GB</td>
      <td style="padding: 12px;">RTX 4070 Ti / RTX 4080</td>
    </tr>
  </tbody>
</table>
</div>

### 📐 Supported Output Formats

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">.glb Format</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">PBR Materials</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">High-Resolution Textures</span>
  </div>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎯 <strong>ComfyUI Hunyuan3D-2 3D Asset Generation</strong> | Complete Solution from Images to High-Quality 3D Models
  </p>
</div>