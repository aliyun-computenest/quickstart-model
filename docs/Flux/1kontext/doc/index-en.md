<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎨 ComfyUI Flux Kontext Dev Image Editing</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">ComfyUI Native Workflow - Multimodal Intelligent Image Editing with Character Consistency</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 Character Consistency</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">✂️ Local Editing</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎨 Style Reference</span>
  </div>
</div>


## 📋 FLUX.1 Kontext Dev Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**FLUX.1 Kontext** is a breakthrough multimodal image editing model launched by Black Forest Labs, supporting simultaneous text and image input, capable of intelligently understanding image context and performing precise editing. The development version is an open-source diffusion transformer model with 12 billion parameters, featuring excellent contextual understanding capabilities and character consistency preservation. Even after multiple iterative edits, it ensures that key elements such as character features and compositional layout remain stable.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎯</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Character Consistency</h4>
<p style="margin: 0; color: #1e40af;">Preserves unique elements of images across multiple scenes and environments, such as reference characters or objects</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">✂️</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Local Editing</h4>
<p style="margin: 0; color: #065f46;">Targeted modifications to specific elements in images without affecting other parts</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Style Reference</h4>
<p style="margin: 0; color: #9a3412;">Generates novel scenes based on text prompts while preserving the unique style of reference images</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">⚡</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">Interactive Speed</h4>
<p style="margin: 0; color: #5b21b6;">Minimal latency in image generation and editing, supporting rapid iteration</p>
</div>

</div>

### 🔄 Version Comparison

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Version</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Type</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Features</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">FLUX.1 Kontext [pro]</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Commercial</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Focused on rapid iterative editing</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">API calls</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">FLUX.1 Kontext [max]</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Experimental</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Enhanced prompt following capabilities</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">API calls</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">FLUX.1 Kontext [dev]</td>
      <td style="padding: 12px;">Open Source</td>
      <td style="padding: 12px;">12B parameters, primarily for research</td>
      <td style="padding: 12px;">Local deployment</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Version Selection Guide</strong><br>
  • <strong>Pro/Max versions</strong>: Called via <a href="/tutorials/api-nodes/black-forest-labs/flux-1-kontext" target="_blank" style="color: #2563eb;">API nodes</a>, suitable for commercial applications<br>
  • <strong>Dev version</strong>: Local deployment, suitable for research and experimentation, fully open source
</div>

</div>

## 🛠️ Workflow Type Description

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

This tutorial provides two workflow types that are essentially functionally identical but differ in user experience:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎯 Group Node Version</h4>
<p style="margin: 0 0 8px 0; color: #1e40af; font-size: 14px;">Uses <strong>FLUX.1 Kontext Image Edit</strong> group node</p>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 13px;">
  <li>Clean interface, easy to reuse</li>
  <li>Quick add group node functionality</li>
  <li>Suitable for complex workflow construction</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🔧 Complete Original Version</h4>
<p style="margin: 0 0 8px 0; color: #065f46; font-size: 14px;">Shows complete node connection structure</p>
<ul style="margin: 0; padding-left: 20px; color: #065f46; font-size: 13px;">
  <li>All nodes visible, convenient for learning</li>
  <li>More intuitive parameter adjustment</li>
  <li>Suitable for deep customization</li>
</ul>
</div>

</div>

### 🚀 Quick Add Group Node Feature

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/selcetion_toolbox_edit.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d64e5fc5fd98c5a2072281be90358f70" alt="Quick Add Group Node" style="max-width: 600px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Experimental Feature</strong><br>
  This feature is currently experimental and may be adjusted in future versions.
</div>

</div>

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

## 🔗 Model File 

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

To run the workflow smoothly, you need to download the following model files. You can also load the corresponding workflow directly to get model download links.

#### 📂 Model File Structure

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">
<pre style="margin: 0; color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 14px;"><code>📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux1-dev-kontext_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 text_encoders/
│       ├── clip_l.safetensors
│       └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn_scaled.safetensors</code></pre>
</div>



## 🚀 Flux.1 Kontext Dev Workflow Example

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

This workflow uses the `Load Image(from output)` node to load images that need editing, making it more convenient to obtain edited images for multi-round editing.

### 📥 Step 1: Download Workflow and Input Images

<div style="text-align: center; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/kontext/dev/flux_1_kontext_dev_basic.png" alt="ComfyUI Flux.1 Kontext Dev Workflow" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin: 8px 0 0 0; color: #64748b; font-size: 14px;">Click image to download, drag into ComfyUI to load workflow</p>
</div>

### 📁 Sample Input Image

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; margin: 16px 0; text-align: center;">
<h4 style="color: #059669; margin: 0 0 12px 0;">🐰 Sample Input Image</h4>
<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/kontext/dev/rabbit.jpg" alt="Sample Input Image" style="max-width: 400px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 13px;">Right-click to save image for workflow testing</p>
</div>

### 🔧 Step 2: Workflow Configuration Operations

<div style="text-align: center; margin: 20px 0;">
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=90995e36fa39a53693aeff3b560c60ef" alt="Workflow Step Guide" style="width: 100%; max-width: 1200px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 📋 Detailed Configuration Steps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🔧 Model Loading</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 14px;">
  <li><strong>Load Diffusion Model</strong>:<br><code>flux1-dev-kontext_fp8_scaled.safetensors</code></li>
  <li><strong>DualCLIP Load</strong>:<br><code>clip_l.safetensors</code> and <code>t5xxl_fp16.safetensors</code></li>
  <li><strong>Load VAE</strong>:<br><code>ae.safetensors</code></li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📁 Image Loading</h4>
<p style="margin: 0; color: #065f46; font-size: 14px;">Load the provided input image in the <strong>Load Image(from output)</strong> node</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">📝 Prompt Settings</h4>
<p style="margin: 0; color: #9a3412; font-size: 14px;">Modify prompts in the <strong>CLIP Text Encode</strong> node, <strong>English only supported</strong></p>
</div>

</div>

#### 🚀 Execute Generation

<div style="text-align: center; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 16px 32px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);">
    <strong>⌨️ Click Queue button or use shortcut Ctrl(Cmd) + Enter to run workflow</strong>
  </div>
</div>

</div>

## 💻 Python API 

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 Python API 
</summary>

```python
import requests
import json
import uuid
import time
import random
import os

# Configuration Parameters - Flux Specific
COMFYUI_SERVER = "127.0.0.1:8188"  # Local server
COMFYUI_TOKEN = ""  
UNET_MODEL = "flux1-dev.safetensors"
VAE_MODEL = "flux-ae.safetensors"
CLIP_L_MODEL = "clip_l_bf16.safetensors"
CLIP_T5_MODEL = "t5xxl_fp16.safetensors"

# Default Parameters
DEFAULT_PROMPT = "A beautiful fantasy girl with long curly silver hair and big blue eyes, wearing a white transparent fairy dress with lace and puffed sleeves. Surrounded by iridescent butterflies and giant glass roses, dreamy lighting, ethereal atmosphere, soft glow, magical realism, highly detailed, cinematic, 8K render."
DEFAULT_T5_PROMPT = "A fairy tale scene of a young girl with silver curly hair wearing a delicate white dress, standing among crystal butterflies and glowing glass roses. The scene is filled with soft magical light, like a dream from a fantasy world."

class ComfyUIFluxClient:
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url = f"http://{server}"
        self.token = token
        self.client_id = str(uuid.uuid4())
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def generate_flux_image(self, clip_l_prompt, t5xxl_prompt=None, 
                           steps=20, cfg=1, guidance=3.5, 
                           width=1024, height=1024, seed=None):
        """Generate Flux text-to-image based on original JSON workflow"""
        print("Starting Flux text-to-image generation...")
        
        # Use CLIP-L prompt for T5XXL if not provided
        if t5xxl_prompt is None:
            t5xxl_prompt = clip_l_prompt
            
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
                    "filename_prefix": "flux_output",
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
                    "positive": ["41", 0],
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
            "41": {
                "inputs": {
                    "clip_l": clip_l_prompt,
                    "t5xxl": t5xxl_prompt,
                    "guidance": guidance,
                    "clip": ["40", 0]
                },
                "class_type": "CLIPTextEncodeFlux",
                "_meta": {"title": "CLIP Text Encode Flux"}
            },
            "42": {
                "inputs": {
                    "conditioning": ["41", 0]
                },
                "class_type": "ConditioningZeroOut",
                "_meta": {"title": "Conditioning Zero Out"}
            }
        }

        print("Submitting Flux text-to-image workflow...")
        print(f"CLIP-L Prompt: {clip_l_prompt}")
        print(f"T5XXL Prompt: {t5xxl_prompt}")
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
        
        for i, prompt_data in enumerate(prompts_list):
            print(f"\nStarting task {i+1}/{len(prompts_list)}...")
            
            if isinstance(prompt_data, str):
                # If string, use as CLIP-L prompt
                clip_l = prompt_data
                t5xxl = None
            elif isinstance(prompt_data, dict):
                # If dict, extract CLIP-L and T5XXL prompts
                clip_l = prompt_data.get('clip_l', prompt_data.get('prompt', ''))
                t5xxl = prompt_data.get('t5xxl')
            else:
                print(f"Invalid prompt format: {prompt_data}")
                continue
            
            try:
                task_id, seed = self.generate_flux_image(clip_l, t5xxl, **kwargs)
                
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
                            'prompt': {'clip_l': clip_l, 't5xxl': t5xxl}
                        })
                        break
                    elif status == "failed":
                        print(f"Task {i+1} failed")
                        break
                    
                    time.sleep(5)
                    
            except Exception as e:
                print(f"Task {i+1} error: {e}")
        
        return results

def main():
    """Main function - Execute Flux text-to-image generation"""
    client = ComfyUIFluxClient()
    
    try:
        print("Flux text-to-image client started...")
        
        # Single image generation example
        print("\n=== Single Image Generation ===")
        task_id, seed = client.generate_flux_image(
            clip_l_prompt=DEFAULT_PROMPT,
            t5xxl_prompt=DEFAULT_T5_PROMPT,
            steps=20,
            guidance=3.5,
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

        # Batch generation example (optional)
        print("\n=== Batch Generation Example ===")
        batch_prompts = [
            "A majestic dragon flying over a medieval castle at sunset",
            "A cyberpunk cityscape with neon lights and flying cars",
            {
                'clip_l': "A serene forest with magical creatures",
                't5xxl': "An enchanted woodland scene with fairies and unicorns dancing in moonlight"
            }
        ]
        
        # Uncomment the following lines to execute batch generation
        # batch_results = client.generate_batch(batch_prompts, steps=15, guidance=3.0)
        # print(f"Batch generation completed, generated {len(batch_results)} images")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
</details>

## 💡 Flux Kontext Prompt Techniques

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Mastering correct prompt techniques is key to achieving ideal editing results. Here are verified best practices:

### 🎯 Basic Modification Techniques

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Recommended Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>Simple and Direct</strong>: <code>"Change the car color to red"</code></li>
  <li><strong>Maintain Style</strong>: <code>"Change to daytime while maintaining the same style of the painting"</code></li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">❌ Avoid These</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Using vague vocabulary</li>
  <li>Overly complex single-sentence descriptions</li>
  <li>Lack of specific targeting</li>
</ul>
</div>

</div>

### 🎨 Style Transfer Framework

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎨 Style Transfer Principles</strong><br>
  • <strong>Clearly Name Style</strong>: <code>"Transform to Bauhaus art style"</code><br>
  • <strong>Describe Features</strong>: <code>"Transform to oil painting with visible brushstrokes, thick paint texture"</code><br>
  • <strong>Preserve Composition</strong>: <code>"Change to Bauhaus style while maintaining the original composition"</code>
</div>

### 👤 Character Consistency Maintenance

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>👤 Character Consistency Framework</strong><br>
  • <strong>Specific Description</strong>: <code>"The woman with short black hair"</code> instead of <code>"she"</code><br>
  • <strong>Preserve Features</strong>: <code>"while maintaining the same facial features, hairstyle, and expression"</code><br>
  • <strong>Step-by-step Modification</strong>: Change background first, then actions
</div>

### 📝 Text Editing Techniques

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📝 Text Editing Key Points</strong><br>
  • <strong>Use Quotes</strong>: <code>"Replace 'joy' with 'BFL'"</code><br>
  • <strong>Maintain Format</strong>: <code>"Replace text while maintaining the same font style"</code>
</div>

</div>

## 🚨 Common Problem Solutions

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🎭 Excessive Character Changes

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">❌ Wrong Example</h4>
<code style="background: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Transform the person into a Viking"</code>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Correct Example</h4>
<code style="background: #d1fae5; color: #065f46; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Change the clothes to be a viking warrior while preserving facial features"</code>
</div>

</div>

### 📐 Composition Position Changes

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">❌ Wrong Example</h4>
<code style="background: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Put him on a beach"</code>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Correct Example</h4>
<code style="background: #d1fae5; color: #065f46; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Change the background to a beach while keeping the person in the exact same position, scale, and pose"</code>
</div>

</div>

### 🎨 Inaccurate Style Application

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">❌ Wrong Example</h4>
<code style="background: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Make it a sketch"</code>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Correct Example</h4>
<code style="background: #d1fae5; color: #065f46; padding: 4px 8px; border-radius: 4px; font-size: 13px;">"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"</code>
</div>

</div>

</div>

## 🎯 Core Principles and Best Practices

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🔑 Four Core Principles

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🎯 Be Specific and Clear</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Use precise descriptions, avoid vague vocabulary</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>📝 Step-by-step Editing</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Break complex modifications into multiple simple steps</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🔒 Clearly Preserve</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Specify what should remain unchanged</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>🔤 Verb Selection</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Use "change", "replace" instead of "transform"</p>
</div>

</div>

### 📋 Best Practice Templates

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
<h4 style="color: #d97706; margin: 0 0 8px 0;">🎯 Object Modification Template</h4>
<code style="background: #fef3c7; color: #9a3412; padding: 4px 8px; border-radius: 4px; font-size: 13px; display: block; margin: 8px 0;">"Change [object] to [new state], keep [content to preserve] unchanged"</code>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🎨 Style Transfer Template</h4>
<code style="background: #f3e8ff; color: #5b21b6; padding: 4px 8px; border-radius: 4px; font-size: 13px; display: block; margin: 8px 0;">"Transform to [specific style], while maintaining [composition/character/other] unchanged"</code>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ Background Replacement Template</h4>
<code style="background: #dcfce7; color: #065f46; padding: 4px 8px; border-radius: 4px; font-size: 13px; display: block; margin: 8px 0;">"Change the background to [new background], keep the subject in the exact same position and pose"</code>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📝 Text Editing Template</h4>
<code style="background: #eff6ff; color: #1e40af; padding: 4px 8px; border-radius: 4px; font-size: 13px; display: block; margin: 8px 0;">"Replace '[original text]' with '[new text]', maintain the same font style"</code>
</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Key Reminder</strong><br>
  The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.
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

### 🎯 Editing Capability Range

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Character Consistency</span>
  </div>
  <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #059669; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Local Editing</span>
  </div>
  <div style="background: #fff7ed; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #ea580c; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Style Transfer</span>
  </div>
  <div style="background: #f3e8ff; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #7c3aed; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Background Replacement</span>
  </div>
  <div style="background: #fef3c7; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Text Editing</span>
  </div>
  <div style="background: #fef2f2; padding: 12px; border-radius: 6px; text-align: center;">
    <span style="background: #dc2626; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px;">Multi-round Iteration</span>
  </div>
</div>

### 🌐 Language Support

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🔤 Prompt Language</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Currently supports English prompts only</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>🎯 Editing Precision</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Supports pixel-level precise editing and semantic-level understanding</p>
</div>

</div>

</div>

### ⚡ Performance Benchmarks

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>🏆 Model Parameters</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">12 billion parameter diffusion transformer model with excellent contextual understanding</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>⚡ Generation Speed</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Minimal latency for image generation and editing, supporting rapid iteration workflows</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>🎯 Consistency Accuracy</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Maintains character features and compositional layout even after multiple iterative edits</p>
</div>

</div>

</div>

</div>

## 🎯 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">🎬</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">Content Creation</h4>
<p style="margin: 0; color: #1e40af;">Social media content, marketing materials, and creative storytelling</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">Artistic Design</h4>
<p style="margin: 0; color: #065f46;">Concept art, character design, and visual style exploration</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🏢</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">Commercial Applications</h4>
<p style="margin: 0; color: #9a3412;">Product visualization, advertising campaigns, and brand consistency</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">🔬</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">Research & Development</h4>
<p style="margin: 0; color: #5b21b6;">AI research, model experimentation, and academic studies</p>
</div>

</div>

## 💡 Usage Tips and Recommendations

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Best Practices</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>Use clear, specific editing instructions</li>
  <li>Maintain appropriate input image quality and resolution</li>
  <li>Break complex edits into multiple simple steps</li>
  <li>Specify what elements should remain unchanged</li>
  <li>Use the Load Image(from output) node for iterative editing</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚠️ Important Notes</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Ensure ComfyUI is updated to the latest development version</li>
  <li>English prompts only - no multilingual support currently</li>
  <li>Complex edits may require multiple iterations for best results</li>
  <li>Monitor VRAM usage with large images or long editing sessions</li>
  <li>Save intermediate results for complex multi-step workflows</li>
</ul>
</div>

</div>

## 🚀 Advanced Workflow Techniques

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🔄 Multi-Round Editing Strategy

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<strong>1️⃣ Initial Setup</strong><br>
<p style="margin: 8px 0 0 0; color: #1e40af; font-size: 14px;">Load your base image and establish the primary subject or scene</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<strong>2️⃣ Background Changes</strong><br>
<p style="margin: 8px 0 0 0; color: #065f46; font-size: 14px;">Modify backgrounds first while preserving subject position and scale</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<strong>3️⃣ Style Adjustments</strong><br>
<p style="margin: 8px 0 0 0; color: #9a3412; font-size: 14px;">Apply style changes while maintaining character consistency</p>
</div>

<div style="background: #f3e8ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<strong>4️⃣ Detail Refinement</strong><br>
<p style="margin: 8px 0 0 0; color: #5b21b6; font-size: 14px;">Fine-tune specific elements and add finishing touches</p>
</div>

</div>

### 🎯 Prompt Optimization Strategies

<div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔍 Progressive Refinement</strong><br>
  Start with broad changes and progressively add more specific details in subsequent iterations. This approach helps maintain consistency while achieving complex transformations.
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎨 <strong>ComfyUI Flux Kontext Dev Image Editing</strong> | Perfect Combination of Multimodal Intelligent Image Editing and Character Consistency
  </p>
  <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 12px;">
    © 2025 Black Forest Labs | Open Source License | Making Image Editing Intelligent and Precise
  </p>
</div>