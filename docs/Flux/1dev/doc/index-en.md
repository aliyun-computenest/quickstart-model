<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎨 Flux1-Dev Model Usage Guide</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Advanced Text-to-Image Generation Model by Black Forest Labs</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Flux1-Dev** represents the pinnacle of open-source image generation technology, built on Flow Matching techniques with significant improvements in image quality, text understanding capabilities, and generation speed.

</div>

## 🚀 Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🏗️ Advanced Architecture</h4>
<p style="margin: 0; color: #065f46;">Diffusion Transformer architecture based on Flow Matching technology</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎯 Exceptional Quality</h4>
<p style="margin: 0; color: #1e40af;">Generated image quality approaches commercial-grade model standards</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🧠 Powerful Text Understanding</h4>
<p style="margin: 0; color: #5b21b6;">Integrated full FP16 CLIP-L and T5 text encoders</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">📐 High Resolution Support</h4>
<p style="margin: 0; color: #9a3412;">Native support for 1024×1024 and higher resolutions</p>
</div>

<div style="background: #ecfdf5; border-left: 4px solid #10b981; padding: 16px; border-radius: 4px;">
<h4 style="color: #10b981; margin: 0 0 8px 0;">⚡ Fast Generation</h4>
<p style="margin: 0; color: #047857;">Optimized inference speed with few-step generation support</p>
</div>

<div style="background: #fdf2f8; border-left: 4px solid #ec4899; padding: 16px; border-radius: 4px;">
<h4 style="color: #ec4899; margin: 0 0 8px 0;">🎨 Diverse Styles</h4>
<p style="margin: 0; color: #be185d;">Supports photorealistic, artistic, concept design, and various styles</p>
</div>

</div>

## 📊 Technical Specifications

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Specification</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Model Type</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Text-to-Image Generation</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Text Encoder</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">T5-XXL + CLIP-L</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">VAE</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Dedicated flux-ae Variational Autoencoder</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Native Resolution</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">1024×1024</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Supported Resolutions</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">512×512 to 2048×2048</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">Recommended Steps</td>
      <td style="padding: 12px;">4-50 steps (8 steps for optimal balance)</td>
    </tr>
  </tbody>
</table>
</div>

## 🏆 Model Advantages

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

**Core Advantages**

- **🖼️ Image Quality**: Rich details, natural colors, reasonable composition
- **📝 Text Following**: Precise understanding of complex text descriptions
- **🎭 Style Diversity**: From photorealistic to abstract art
- **🎯 Consistency**: Stable and controllable generation results
- **⚡ Efficiency**: Faster inference speed compared to similar-level models

</div>

---

# ⚙️ Configuration Guide

## 📁 Model Files

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🌐 WebUI Environment</h3>

**Main Model**
- `flux.1_dev_8x8_e4m3fn.safetensors`

**VAE**
- `flux-ae.safetensors`

**Text Encoders**
- `t5xxl_fp16.safetensors`
- `clip_l.safetensors`
- `clip_g.safetensors`
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🎛️ ComfyUI Environment</h3>

**Main Model**
- `Flux1-dev.safetensors`

**VAE**
- `flux-ae.safetensors`

**Text Encoders**
- `t5xxl_fp16.safetensors`
- `clip_l.safetensors`
</div>

</div>

---

# 📖 Usage Guide

## 🎛️ ComfyUI Usage

### 🖱️ Interface Operations

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Step 1: Select Workflow**
- Choose the workflow in the workflow selector
  ![img.png](text2img.png)

**Step 2: Input Prompts**
- Enter your desired content description
  ![img.png](text2img2.png)

**Step 3: Creative Examples**
- You can input interesting content, such as "Guan Yu fighting Snow White"

**Step 4: Parameter Settings**
- Set image resolution and quantity
- To speed up generation, set batch_size to 1
  ![img.png](text2img3.png)

**Step 5: Wait for Generation**
- Patiently wait for image generation to complete

</div>

### 🔌 ComfyUI API Integration

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

**Get Token**
- Click the top-right button to open the bottom panel and get the token
  ![img_1.png](img_3.png)

**Get Server Address**
- Refer to COMFYUI_SERVER acquisition guide
  ![img_2.png](img_2.png)

</div>

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
📋 Click to Expand ComfyUI API Python Code
</summary>

```python
import requests, json, uuid, time, random, os

COMFYUI_SERVER, COMFYUI_TOKEN = "#Fill in your server address here", "Fill in your token here"  
UNET_MODEL, VAE_MODEL, CLIP1_MODEL, CLIP2_MODEL = "flux1-dev.safetensors", "ae.safetensors", "t5xxl_fp16.safetensors", "clip_l.safetensors"
PROMPT = "A beautiful anime girl with long flowing hair, wearing elegant dress, standing in a magical garden with glowing flowers, soft lighting, high quality, detailed"

class FluxClient:
    def __init__(self):
        self.base_url, self.client_id = f"http://{COMFYUI_SERVER}", str(uuid.uuid4())
        self.headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {COMFYUI_TOKEN}"} if COMFYUI_TOKEN else {})}

    def generate(self, prompt, aspect="1:1 square 1024x1024", steps=35, guidance=3.5, batch=1):
        workflow = {"6": {"inputs": {"text": prompt, "clip": ["11", 0]}, "class_type": "CLIPTextEncode"}, "8": {"inputs": {"samples": ["13", 0], "vae": ["10", 0]}, "class_type": "VAEDecode"}, "9": {"inputs": {"filename_prefix": "Flux", "images": ["8", 0]}, "class_type": "SaveImage"}, "10": {"inputs": {"vae_name": VAE_MODEL}, "class_type": "VAELoader"}, "11": {"inputs": {"clip_name1": CLIP1_MODEL, "clip_name2": CLIP2_MODEL, "type": "flux", "device": "default"}, "class_type": "DualCLIPLoader"}, "12": {"inputs": {"unet_name": UNET_MODEL, "weight_dtype": "fp8_e4m3fn"}, "class_type": "UNETLoader"}, "13": {"inputs": {"noise": ["25", 0], "guider": ["22", 0], "sampler": ["16", 0], "sigmas": ["17", 0], "latent_image": ["85", 4]}, "class_type": "SamplerCustomAdvanced"}, "16": {"inputs": {"sampler_name": "dpmpp_2m"}, "class_type": "KSamplerSelect"}, "17": {"inputs": {"scheduler": "sgm_uniform", "steps": steps, "denoise": 1, "model": ["61", 0]}, "class_type": "BasicScheduler"}, "22": {"inputs": {"model": ["61", 0], "conditioning": ["60", 0]}, "class_type": "BasicGuider"}, "25": {"inputs": {"noise_seed": random.randint(1, 1000000000000000)}, "class_type": "RandomNoise"}, "60": {"inputs": {"guidance": guidance, "conditioning": ["6", 0]}, "class_type": "FluxGuidance"}, "61": {"inputs": {"max_shift": 1.15, "base_shift": 0.5, "width": ["85", 0], "height": ["85", 1], "model": ["12", 0]}, "class_type": "ModelSamplingFlux"}, "85": {"inputs": {"width": 1024, "height": 1024, "aspect_ratio": aspect, "swap_dimensions": "Off", "upscale_factor": 1, "batch_size": batch}, "class_type": "CR SDXL Aspect Ratio"}}
        return requests.post(f"{self.base_url}/prompt", headers=self.headers, json={"prompt": workflow, "client_id": self.client_id}).json()["prompt_id"]

    def status(self, task_id):
        queue = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
        return "processing" if any(item[1] == task_id for item in queue.get("queue_running", [])) else "pending" if any(item[1] == task_id for item in queue.get("queue_pending", [])) else "completed" if task_id in requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers).json() else "processing"

    def download(self, task_id, output_dir="./flux_output/"):
        history = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers).json()
        files = []
        if task_id in history:
            for output in history[task_id]['outputs'].values():
                if 'images' in output:
                    os.makedirs(output_dir, exist_ok=True)
                    for img in output['images']:
                        path = os.path.join(output_dir, img['filename'])
                        with open(path, "wb") as f: f.write(requests.get(f"{self.base_url}/view?filename={img['filename']}", headers=self.headers).content)
                        files.append(path)
        return files

def main():
    client = FluxClient()
    print(f"🎨 Generating: {PROMPT}")
    task_id = client.generate(PROMPT)
    print(f"🆔 Task ID: {task_id}")
    while True:
        status = client.status(task_id)
        print(f"📊 Status: {status}")
        if status == "completed": break
        time.sleep(5)
    files = client.download(task_id)
    print(f"🎉 Complete! Generated {len(files)} images: {files}")

if __name__ == "__main__": main()
```

</details>

---

## 🌐 Web UI Usage

### 🖱️ Interface Operations

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**1. Model Selection**
- Select Flux1-Dev (HyFY-8-Step-Hybrid-v1.0.safetensors) model in the Checkpoint model selector

**2. VAE and CLIP Model Selection**
- Select: `Clip_l.safetensors`, `t5xxl_fp16.safetensors`, `flux-ae.safetensors`
  ![img_1.png](img_1.png)

**3. Prompt Input**
- **Positive Prompt**: Detailed description of the desired image
- **Negative Prompt**: Description of unwanted elements (Flux model is less sensitive to negative prompts)

**4. Parameter Settings**
- **Steps**: Recommended 8-20 steps
- **CFG**: Recommended 1.0-3.5 (lower values work better)
- **Sampler**: Recommended Euler or DPM++ 2M
- **Resolution**: 1024×1024 or other supported dimensions

**5. Generate Image**
- Click the "Generate" button to start generation

**6. Result Processing**
- View, save, or further edit the generated images

</div>

### 🎨 Prompt Examples

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">📸 Photorealistic Style</h4>
<div style="background: #1e293b; border-radius: 4px; padding: 12px; margin-top: 8px;">
<code style="color: #e2e8f0; font-size: 12px; line-height: 1.4;">
"a professional portrait of a young woman, natural lighting, high resolution, detailed skin texture, photorealistic"
</code>
</div>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🎨 Artistic Style</h4>
<div style="background: #1e293b; border-radius: 4px; padding: 12px; margin-top: 8px;">
<code style="color: #e2e8f0; font-size: 12px; line-height: 1.4;">
"an impressionist painting of a garden in spring, soft brushstrokes, vibrant colors, artistic masterpiece"
</code>
</div>
</div>

<div style="background: #ecfeff; border-left: 4px solid #06b6d4; padding: 16px; border-radius: 4px;">
<h4 style="color: #06b6d4; margin: 0 0 8px 0;">🤖 Concept Design</h4>
<div style="background: #1e293b; border-radius: 4px; padding: 12px; margin-top: 8px;">
<code style="color: #e2e8f0; font-size: 12px; line-height: 1.4;">
"futuristic robot design, sleek metallic surface, glowing blue accents, concept art, highly detailed"
</code>
</div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🏔️ Landscape Photography</h4>
<div style="background: #1e293b; border-radius: 4px; padding: 12px; margin-top: 8px;">
<code style="color: #e2e8f0; font-size: 12px; line-height: 1.4;">
"mountain landscape at golden hour, dramatic clouds, professional photography, ultra-wide angle, HDR"
</code>
</div>
</div>

</div>

### 🖼️ UI Interface Usage Example

![img.png](img.png)

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 Click to Expand WebUI API Python Code
</summary>

```python
import base64
import time
import uuid
import requests

# Configuration
base_url = "http://127.0.0.1:7680"
auth = ("admin", "${APIKEY}")
session_hash = str(uuid.uuid4())[:12]

# Set VAE/Text Encoder
print("Setting VAE/Text Encoder...")
requests.post(f"{base_url}/run/predict", json={
    "data": [["flux-ae.safetensors", "t5xxl_fp16.safetensors", "clip_l.safetensors", "clip_g.safetensors"]],
    "event_data": None,
    "fn_index": 9,
    "trigger_id": 1001,
    "session_hash": session_hash
}, auth=auth)
time.sleep(3)

# Switch FLUX model
print("Switching FLUX model...")
requests.post(f"{base_url}/queue/join", json={
    "data": ["HyFY-8-Step-Hybrid-v1.0.safetensors"],
    "event_data": None,
    "fn_index": 8,
    "trigger_id": 1002,
    "session_hash": session_hash
}, auth=auth)
time.sleep(15)

# Generate image
print("Generating image...")
result = requests.post(f"{base_url}/sdapi/v1/txt2img", json={
    "prompt": "a beautiful cat",
    "steps": 8,
    "width": 1024,
    "height": 1024,
    "cfg_scale": 1.0,
    "sampler_name": "Euler"
}, auth=auth).json()

# Save image
if "images" in result:
    with open("output.png", "wb") as f:
        f.write(base64.b64decode(result["images"][0]))
    print("Image saved as output.png")
else:
    print("Error:", result)
```

</details>

---

## 🔄 Other Built-in Models

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

**Model Support Information**

In the current service, **Flux models** are deployed on ECS instances. In addition to the current **Flux-dev model**, **SD1.5** and **SD3** models are also supported and can be dynamically switched in the **WebUI Forge interface**.

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎨 <strong>Start Your AI Art Creation Journey!</strong> | Use Flux1-Dev model to turn imagination into reality
  </p>
</div>