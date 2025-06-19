# 🎨 Stable Diffusion 1.5 Complete Guide

<div align="center">

![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-1.5-blue?style=for-the-badge&logo=stability-ai&logoColor=white)
![License](https://img.shields.io/badge/License-Open%20Source-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![GPU](https://img.shields.io/badge/GPU-6GB+-orange?style=for-the-badge&logo=nvidia&logoColor=white)
![Community](https://img.shields.io/badge/Community-Active-purple?style=for-the-badge&logo=discord&logoColor=white)

*The ultimate text-to-image generation model for creators and developers*

</div>

---

## 🌟 Model Introduction

**Stable Diffusion 1.5** is a revolutionary text-to-image generation model developed by **Stability AI**. As a groundbreaking milestone in the open-source AI image generation landscape, it continues to be one of the most beloved and extensively utilized models in the community. This model has earned its reputation through its **lightweight architecture**, **exceptional efficiency**, and **vibrant ecosystem**, making it the go-to choice for both AI newcomers and seasoned professionals.

### ✨ Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; color: white; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🚀 <span>Performance Excellence</span>
</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
💾 <strong>Lightweight & Efficient:</strong> Only 6GB VRAM required
</li>
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
⚡ <strong>Lightning Fast:</strong> Optimized for batch and real-time generation
</li>
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
🎯 <strong>Rock Solid:</strong> Battle-tested across millions of generations
</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; padding: 25px; color: white; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🎨 <span>Creative Powerhouse</span>
</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
🌈 <strong>Style Versatility:</strong> Photorealistic, anime, artistic styles
</li>
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
🔧 <strong>Highly Customizable:</strong> LoRA, Textual Inversion support
</li>
<li style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
🌍 <strong>Thriving Ecosystem:</strong> Massive community & extensions
</li>
</ul>
</div>

</div>

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 15px; padding: 25px; color: white; margin: 20px 0; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
<h4 style="margin-top: 0; display: flex; align-items: center; justify-content: center; gap: 10px;">
🆓 <span>Open Source Freedom</span>
</h4>
<p style="margin: 0; font-size: 18px;">
<strong>100% Open Source</strong> • <strong>Commercial Use Allowed</strong> • <strong>No Restrictions</strong>
</p>
</div>

### 📊 Technical Specifications

<div style="background: #f8f9fa; border-radius: 12px; padding: 25px; margin: 20px 0; border-left: 5px solid #007bff;">

<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr style="background: linear-gradient(135deg, #007bff, #0056b3); color: white;">
<th style="padding: 15px; text-align: left; border-radius: 8px 0 0 0;">🔧 Specification</th>
<th style="padding: 15px; text-align: left; border-radius: 0 8px 0 0;">📋 Details</th>
</tr>
</thead>
<tbody>
<tr style="background: #ffffff;">
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;"><strong>🤖 Model Type</strong></td>
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;">Text-to-Image / Image-to-Image Generation</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;"><strong>📈 Parameters</strong></td>
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;">~860M parameters</td>
</tr>
<tr style="background: #ffffff;">
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;"><strong>🔤 Text Encoder</strong></td>
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;">CLIP ViT-L/14</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;"><strong>🖼️ VAE Resolution</strong></td>
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;">512×512 (Native)</td>
</tr>
<tr style="background: #ffffff;">
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;"><strong>⏱️ Optimal Steps</strong></td>
<td style="padding: 15px; border-bottom: 1px solid #dee2e6;">20-50 steps</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px;"><strong>💰 License</strong></td>
<td style="padding: 15px;">CreativeML Open RAIL-M</td>
</tr>
</tbody>
</table>

</div>

---

## ⚙️ Configuration Setup

### 💻 System Requirements

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); border-radius: 12px; padding: 20px; margin: 20px 0; color: #333;">

<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🖥️ <span>Minimum Hardware Specifications</span>
</h4>

<div style="background: rgba(255,255,255,0.9); border-radius: 8px; padding: 15px; margin: 10px 0;">
<strong>🎮 GPU Memory:</strong> 6GB VRAM or higher<br>
<small style="color: #666;">Recommended: 8GB+ for optimal performance</small>
</div>

</div>

### 📁 Essential Model Files

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #fff; border: 2px solid #28a745; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #28a745; margin-top: 0; display: flex; align-items: center; gap: 10px;">
🎯 <span>Main Model</span>
</h4>
<code style="background: #f8f9fa; padding: 8px; border-radius: 4px; display: block; word-break: break-all;">
v1-5-pruned-emaonly.safetensors
</code>
<p style="margin: 10px 0 0 0; color: #666; font-size: 14px;">Core generation model file</p>
</div>

<div style="background: #fff; border: 2px solid #007bff; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #007bff; margin-top: 0; display: flex; align-items: center; gap: 10px;">
🎨 <span>Enhanced VAE</span>
</h4>
<code style="background: #f8f9fa; padding: 8px; border-radius: 4px; display: block; word-break: break-all; font-size: 12px;">
vae-ft-mse-840000-ema-pruned.safetensors
</code>
<p style="margin: 10px 0 0 0; color: #666; font-size: 14px;">Optional high-quality VAE</p>
</div>

<div style="background: #fff; border: 2px solid #6f42c1; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #6f42c1; margin-top: 0; display: flex; align-items: center; gap: 10px;">
📝 <span>Text Encoder</span>
</h4>
<div style="background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center;">
<em>Built into main model</em>
</div>
<p style="margin: 10px 0 0 0; color: #666; font-size: 14px;">CLIP ViT-L/14 integrated</p>
</div>

</div>

---

## 🚀 Usage Guide

### 🌐 Web UI Interface

#### 📋 Step-by-Step Workflow

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; color: white; margin: 20px 0;">

<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🎯 <span>1. Model Selection</span>
</h4>
<p>Navigate to the upper-left model selector and choose your SD1.5 model</p>

![Model Selection](img.png)

</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #fff; border-left: 5px solid #28a745; border-radius: 8px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #28a745; margin-top: 0;">✍️ 2. Prompt Engineering</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 10px 0;"><strong>✅ Positive Prompt:</strong> Describe your desired image in detail</li>
<li style="margin: 10px 0;"><strong>❌ Negative Prompt:</strong> Specify unwanted elements (SD1.5 excels here!)</li>
</ul>
</div>

<div style="background: #fff; border-left: 5px solid #007bff; border-radius: 8px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #007bff; margin-top: 0;">⚙️ 3. Parameter Tuning</h4>
<table style="width: 100%; font-size: 14px;">
<tr><td><strong>📊 Steps:</strong></td><td>20-30</td></tr>
<tr><td><strong>🎚️ CFG Scale:</strong></td><td>7-12</td></tr>
<tr><td><strong>🔄 Sampler:</strong></td><td>DPM++ 2M Karras</td></tr>
<tr><td><strong>📐 Resolution:</strong></td><td>512×512</td></tr>
</table>
</div>

</div>

<div style="background: #fff; border-left: 5px solid #6f42c1; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h4 style="color: #6f42c1; margin-top: 0;">🔧 4. Advanced Configuration</h4>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
<div><strong>🎲 Seed:</strong> Control randomness (-1 = random)</div>
<div><strong>📦 Batch Size:</strong> Multiple generations</div>
<div><strong>🔍 Hi-Res Fix:</strong> Upscale for larger images</div>
</div>
</div>

#### 🎨 Optimized Parameter Presets

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border-radius: 15px; padding: 20px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0;">⚡ Speed Mode</h4>
<div style="background: rgba(255,255,255,0.2); border-radius: 8px; padding: 15px; margin: 10px 0;">
<div><strong>Steps:</strong> 20 | <strong>CFG:</strong> 7</div>
<div><strong>Sampler:</strong> Euler a</div>
<div><strong>Size:</strong> 512×512</div>
</div>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">Perfect for rapid prototyping</p>
</div>

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 20px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0;">💎 Quality Mode</h4>
<div style="background: rgba(255,255,255,0.2); border-radius: 8px; padding: 15px; margin: 10px 0;">
<div><strong>Steps:</strong> 30 | <strong>CFG:</strong> 9-11</div>
<div><strong>Sampler:</strong> DPM++ 2M Karras</div>
<div><strong>Size:</strong> 768×768</div>
</div>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">Maximum detail and fidelity</p>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; padding: 20px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0;">🎨 Artistic Mode</h4>
<div style="background: rgba(255,255,255,0.2); border-radius: 8px; padding: 15px; margin: 10px 0;">
<div><strong>Steps:</strong> 25 | <strong>CFG:</strong> 8-10</div>
<div><strong>Sampler:</strong> DDIM</div>
<div><strong>Size:</strong> 512×768</div>
</div>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">Enhanced creative expression</p>
</div>

</div>

---

### 🔌 API Integration

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); border-radius: 12px; padding: 20px; margin: 20px 0;">

<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
⚠️ <span>Configuration Requirements</span>
</h4>

<p>Replace <code>BASE_URL</code> and <code>APIKEY</code> with your actual deployment values</p>

![API Configuration](img_4.png)

<div style="background: rgba(255,255,255,0.9); border-radius: 8px; padding: 15px; margin: 10px 0;">
<strong>🌐 Public Network:</strong> Use public IP:port for external access
</div>

</div>

<details style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; margin: 25px 0; color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
<summary style="font-weight: bold; font-size: 20px; cursor: pointer; display: flex; align-items: center; gap: 15px; padding: 10px;">
🐍 <span>Complete Python API Implementation</span>
</summary>

<div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 20px; margin: 20px 0;">

```python
import requests
import base64
import json
from typing import Optional, Dict, Any

class StableDiffusionAPI:
    """
    🎨 Stable Diffusion 1.5 API Client
    A comprehensive wrapper for SD1.5 API interactions
    """
    
    def __init__(self, base_url: str, username: str = "admin", apikey: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.auth = (username, apikey) if apikey else None
        
    def switch_model(self, model_name: str = "v1-5-pruned-emaonly.safetensors") -> bool:
        """🔄 Switch to SD1.5 model"""
        model_data = {"sd_model_checkpoint": model_name}
        
        try:
            print("🔄 Switching to Stable Diffusion 1.5...")
            response = requests.post(
                f"{self.base_url}/sdapi/v1/options", 
                json=model_data, 
                auth=self.auth
            )
            response.raise_for_status()
            print("✅ Model switch completed successfully!")
            return True
        except requests.RequestException as e:
            print(f"❌ Model switch failed: {e}")
            return False
    
    def generate_image(
        self, 
        prompt: str,
        negative_prompt: str = "",
        steps: int = 20,
        cfg_scale: float = 7.0,
        width: int = 512,
        height: int = 512,
        sampler_name: str = "Euler a",
        seed: int = -1
    ) -> Optional[bytes]:
        """🎨 Generate image with SD1.5"""
        
        generation_data = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "width": width,
            "height": height,
            "sampler_name": sampler_name,
            "seed": seed
        }
        
        try:
            print(f"🎨 Generating: '{prompt[:50]}...'")
            response = requests.post(
                f"{self.base_url}/sdapi/v1/txt2img",
                json=generation_data,
                auth=self.auth
            )
            response.raise_for_status()
            result = response.json()
            
            if "images" in result and result["images"]:
                image_data = base64.b64decode(result["images"][0])
                print("✅ Image generated successfully!")
                return image_data
            else:
                print("❌ No image data received")
                return None
                
        except requests.RequestException as e:
            print(f"❌ Generation failed: {e}")
            return None
    
    def save_image(self, image_data: bytes, filename: str = "sd15_output.png") -> bool:
        """💾 Save generated image"""
        try:
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"💾 Image saved as: {filename}")
            return True
        except Exception as e:
            print(f"❌ Save failed: {e}")
            return False

# 🚀 Usage Example
def main():
    # Initialize API client
    api = StableDiffusionAPI(
        base_url="<Your-Deployment-URL>",
        username="admin",
        apikey="${APIKEY}"  # Remove if no API key
    )
    
    # Switch to SD1.5
    if not api.switch_model():
        return
    
    # Generate image
    image_data = api.generate_image(
        prompt="a majestic cat sitting on a throne, royal, detailed, 4k",
        negative_prompt="blurry, low quality, distorted",
        steps=25,
        cfg_scale=8.0,
        width=512,
        height=512
    )
    
    # Save result
    if image_data:
        api.save_image(image_data, "royal_cat.png")

if __name__ == "__main__":
    main()
```

</div>
</details>

<div style="background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 15px; margin: 20px 0;">
<h4 style="color: #856404; margin-top: 0;">💡 No API Key Setup</h4>
<p style="margin: 0; color: #856404;">If authentication is disabled, modify requests like this:</p>
<code style="background: #f8f9fa; padding: 8px; border-radius: 4px; display: block; margin: 10px 0;">
response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data)
</code>
</div>

---

## 📚 Essential Resources & Community

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
📖 <span>Official Documentation</span>
</h4>
<a href="https://stability.ai/stable-diffusion" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px; display: block; text-align: center; margin: 10px 0;">
Visit Stability AI Docs →
</a>
</div>

<div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border-radius: 15px; padding: 25px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🖥️ <span>Web Interface</span>
</h4>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px; display: block; text-align: center; margin: 10px 0;">
Automatic1111 WebUI →
</a>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; padding: 25px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🎨 <span>Model Hub</span>
</h4>
<a href="https://civitai.com/" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px; display: block; text-align: center; margin: 10px 0;">
Civitai Community →
</a>
</div>

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 15px; padding: 25px; color: #333; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
✍️ <span>Prompt Mastery</span>
</h4>
<a href="https://prompthero.com/stable-diffusion-prompts" style="color: #333; text-decoration: none; background: rgba(255,255,255,0.7); padding: 10px; border-radius: 8px; display: block; text-align: center; margin: 10px 0;">
Prompt Engineering Guide →
</a>
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); border-radius: 15px; padding: 25px; color: #333; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin-top: 0; display: flex; align-items: center; gap: 10px;">
🔧 <span>Advanced Training</span>
</h4>
<a href="https://github.com/cloneofsimo/lora" style="color: #333; text-decoration: none; background: rgba(255,255,255,0.7); padding: 10px; border-radius: 8px; display: block; text-align: center; margin: 10px 0;">
LoRA Training Tutorial →
</a>
</div>

</div>

---

<div align="center" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 40px; margin: 40px 0; color: white; box-shadow: 0 15px 35px rgba(0,0,0,0.2);">

<h2 style="margin-top: 0; font-size: 2.5em;">🎉 Ready to Create Magic?</h2>

<p style="font-size: 1.2em; margin: 20px 0; opacity: 0.9;">
Transform your imagination into stunning visuals with Stable Diffusion 1.5
</p>

<div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0; flex-wrap: wrap;">
<div style="background: rgba(255,255,255,0.2); padding: 15px 25px; border-radius: 25px;">
⚡ <strong>Fast</strong>
</div>
<div style="background: rgba(255,255,255,0.2); padding: 15px 25px; border-radius: 25px;">
🆓 <strong>Free</strong>
</div>
<div style="background: rgba(255,255,255,0.2); padding: 15px 25px; border-radius: 25px;">
🌟 <strong>Powerful</strong>
</div>
</div>

<p style="font-style: italic; margin: 0; opacity: 0.8;">
"Where creativity meets artificial intelligence"
</p>

</div>