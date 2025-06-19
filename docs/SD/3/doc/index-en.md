# 🎨 Stable Diffusion 3 Medium Complete Guide

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
  <h2 style="margin: 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🚀 Next-Generation AI Image Generation</h2>
  <p style="font-size: 1.2em; margin: 10px 0 0 0; opacity: 0.9;">The Perfect Balance of Stability AI's Third-Generation Diffusion Model</p>
</div>

## 🌟 Model Introduction

**Stable Diffusion 3 Medium** is the medium-parameter version of the third-generation diffusion model released by Stability AI, representing a significant advancement in open-source image generation technology. This model significantly improves image quality, text understanding capabilities, and generation diversity while maintaining relatively low hardware requirements, making it the perfect balanced choice between SD1.5 and high-end models.

### ✨ Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 12px; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">🏗️ Advanced Architecture</h4>
  <p style="margin-bottom: 0;">Based on Multimodal Diffusion Transformer (MMDiT) architecture</p>
</div>

<div style="background: linear-gradient(135deg, #f093fb, #f5576c); padding: 20px; border-radius: 12px; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">🧠 Enhanced Text Understanding</h4>
  <p style="margin-bottom: 0;">Integrated T5-XXL and dual CLIP text encoders</p>
</div>

<div style="background: linear-gradient(135deg, #4facfe, #00f2fe); padding: 20px; border-radius: 12px; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">⚖️ Balanced Performance</h4>
  <p style="margin-bottom: 0;">2 billion parameters, achieving optimal balance between quality and efficiency</p>
</div>

<div style="background: linear-gradient(135deg, #43e97b, #38f9d7); padding: 20px; border-radius: 12px; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">📐 Multi-Aspect Ratio Support</h4>
  <p style="margin-bottom: 0;">Native support for various resolutions and aspect ratios</p>
</div>

<div style="background: linear-gradient(135deg, #fa709a, #fee140); padding: 20px; border-radius: 12px; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">👤 Improved Human Anatomy</h4>
  <p style="margin-bottom: 0;">Significantly reduced hand and body structure errors</p>
</div>

<div style="background: linear-gradient(135deg, #a8edea, #fed6e3); padding: 20px; border-radius: 12px; color: #333; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0;">🎨 Style Diversity</h4>
  <p style="margin-bottom: 0;">Supports various styles from realistic to artistic</p>
</div>

</div>

### 📊 Technical Specifications

<div style="background: #f8f9fa; border-radius: 12px; padding: 25px; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">

| Specification | Details |
|---------------|---------|
| **Model Type** | Text-to-Image Generation |
| **Architecture** | Multimodal Diffusion Transformer (MMDiT) |
| **Parameter Scale** | Approximately 2 billion parameters |
| **Text Encoders** | T5-XXL + CLIP-L + CLIP-G |
| **VAE** | Improved variational autoencoder |
| **Native Resolution** | 1024×1024 |
| **Supported Resolutions** | 512×512 to 2048×2048 |
| **Recommended Steps** | 20-50 steps |
| **CFG Range** | 4.5-9.0 |

</div>

---

## ⚙️ Configuration Instructions

### 💻 System Requirements

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 25px; border-radius: 12px; border-left: 5px solid #2196f3; margin: 20px 0;">
  <h4 style="color: #1976d2; margin-top: 0;">🖥️ Hardware Configuration</h4>
  <ul style="margin-bottom: 0;">
    <li><strong>ECS VRAM</strong>: 8GB or more recommended</li>
    <li><strong>System RAM</strong>: 16GB or more recommended</li>
    <li><strong>Storage Space</strong>: At least 15GB available space</li>
  </ul>
</div>

### 📁 Model Files

<div style="background: #fff; border-radius: 12px; padding: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin: 20px 0;">

| File Type | Filename | Size | Description |
|-----------|----------|------|-------------|
| **Main Model** | `sd3_medium_incl_clips_t5xxlfp16.safetensors` | ~10GB | Complete model with all components |
| **Text Encoders** | Integrated in main model | - | T5-XXL (FP16) + CLIP-L + CLIP-G |
| **VAE** | Built-in improved VAE | - | Enhanced variational autoencoder |

</div>

---

## 🎯 Usage Guide

### 🌐 Web UI Usage

<div style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); padding: 25px; border-radius: 12px; border-left: 5px solid #ff9800; margin: 20px 0;">

#### 🔧 Basic Operations

**1. Model Selection**
- Select SD3 Medium model in the model selector

**2. Prompt Input**
- **Positive Prompt**: Detailed description of desired image, supports more complex descriptions
- **Negative Prompt**: SD3 responds weakly to negative prompts, can be simplified

**3. Parameter Settings**
- **Steps**: Recommended 20-30 steps
- **CFG Scale**: Recommended 4.5-7.0 (lower than SD1.5)
- **Sampler**: Recommended DPM++ 2M or Euler
- **Resolution**: 1024×1024 (native) or other supported sizes

**4. Advanced Settings**
- **Seed**: Controls randomness
- **Batch Settings**: Adjust according to VRAM capacity
- **Multi-Aspect Ratio**: Utilize native multi-resolution support

</div>

---

## 📋 Parameter Description

### 🎛️ Core Parameters

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 5px solid #4caf50;">
  <h4 style="color: #2e7d32; margin-top: 0;">⏱️ steps (Inference steps)</h4>
  <ul style="margin-bottom: 0;">
    <li><strong>15-20 steps</strong>: Fast generation, acceptable quality</li>
    <li><strong>20-30 steps</strong>: Balanced quality and speed (recommended)</li>
    <li><strong>30-50 steps</strong>: Highest quality, slower speed</li>
  </ul>
</div>

<div style="background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3;">
  <h4 style="color: #1976d2; margin-top: 0;">🎚️ cfg_scale (CFG guidance strength)</h4>
  <ul style="margin-bottom: 0;">
    <li><strong>4.0-5.0</strong>: Natural results, less overfitting</li>
    <li><strong>5.0-7.0</strong>: Balanced text following and naturalness (recommended)</li>
    <li><strong>7.0-9.0</strong>: Strong text following, may be over-saturated</li>
  </ul>
</div>

<div style="background: #fce4ec; padding: 20px; border-radius: 10px; border-left: 5px solid #e91e63;">
  <h4 style="color: #c2185b; margin-top: 0;">🔄 sampler (Sampler selection)</h4>
  <ul style="margin-bottom: 0;">
    <li><strong>DPM++ 2M</strong>: High quality, recommended</li>
    <li><strong>Euler</strong>: Fast and stable</li>
    <li><strong>DPM++ SDE</strong>: High quality but slower</li>
    <li><strong>DDIM</strong>: Classic choice, stable results</li>
  </ul>
</div>

</div>

### 📐 Resolution Settings

<div style="background: #f3e5f5; padding: 20px; border-radius: 12px; margin: 20px 0;">

SD3 natively supports various resolutions:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px;">

<div style="background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <strong>1024×1024</strong><br>
  <small>Standard square</small>
</div>

<div style="background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <strong>1152×896</strong><br>
  <small>Landscape 4:3.6</small>
</div>

<div style="background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <strong>896×1152</strong><br>
  <small>Portrait 3.6:4</small>
</div>

<div style="background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <strong>1344×768</strong><br>
  <small>Ultra-widescreen</small>
</div>

</div>

</div>

### 🎯 SD3-Specific Parameters

<div style="background: linear-gradient(135deg, #fff8e1, #ffecb3); padding: 20px; border-radius: 12px; margin: 20px 0;">

- **Lower CFG**: SD3 works best in the 4.5-7.0 range
- **Fewer Steps**: 20-25 steps are usually sufficient for good results
- **Native Multi-Resolution**: Can generate large images without high-resolution fix

</div>

---

## 💡 Prompt Techniques

### 🧠 SD3 Prompt Characteristics

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #e8f5e8; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
  <strong>Better Long Text Understanding</strong><br>
  <small>Supports more detailed and complex descriptions</small>
</div>

<div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
  <strong>Improved Concept Combination</strong><br>
  <small>Better understanding of multiple concept combinations</small>
</div>

<div style="background: #fce4ec; padding: 15px; border-radius: 8px; border-left: 4px solid #e91e63;">
  <strong>Precise Attribute Control</strong><br>
  <small>More precise control over colors, materials, lighting, etc.</small>
</div>

<div style="background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
  <strong>Reduced Negative Dependency</strong><br>
  <small>Less dependency on negative prompts</small>
</div>

</div>

### 🏗️ High-Quality Prompt Structure

<div style="background: #263238; color: #fff; padding: 20px; border-radius: 12px; margin: 20px 0; font-family: 'Courier New', monospace;">

```
[Detailed subject description] + [Environment/Background] + [Style/Technique] + [Lighting/Atmosphere] + [Quality terms]
```

</div>

### 🎨 Prompt Examples

<details style="border: 2px solid #4caf50; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #e8f5e8, #c8e6c9);">
<summary style="font-weight: bold; font-size: 18px; color: #2e7d32; cursor: pointer;">
📸 Realistic Photography Style
</summary>

```python
photography_prompts = [
    """A professional headshot of a confident businesswoman in her 30s, 
    wearing a navy blue blazer, sitting at a modern office desk, 
    natural window lighting, shallow depth of field, 
    shot with 85mm lens, high resolution, sharp focus""",
    
    """Street photography of a bustling Tokyo intersection at night, 
    neon signs, people crossing, motion blur on vehicles, 
    rain-soaked streets reflecting lights, urban atmosphere, 
    documentary style, Leica camera aesthetic"""
]
```

</details>

<details style="border: 2px solid #ff9800; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #fff3e0, #ffe0b2);">
<summary style="font-weight: bold; font-size: 18px; color: #f57c00; cursor: pointer;">
🎨 Artistic Creation Style
</summary>

```python
art_prompts = [
    """An impressionist painting of a French countryside vineyard in autumn, 
    golden sunlight filtering through grape vines, warm color palette, 
    loose brushstrokes, en plein air style, reminiscent of Monet's work""",
    
    """Digital concept art of a floating island city in the clouds, 
    waterfalls cascading into the sky, flying ships, 
    fantasy architecture, dramatic lighting, 
    highly detailed, matte painting style"""
]
```

</details>

<details style="border: 2px solid #e91e63; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #fce4ec, #f8bbd9);">
<summary style="font-weight: bold; font-size: 18px; color: #c2185b; cursor: pointer;">
👤 Character Portraits
</summary>

```python
portrait_prompts = [
    """A detailed portrait of a young artist in her studio, 
    paint-stained apron, holding a palette and brush, 
    surrounded by canvases, natural lighting from large windows, 
    thoughtful expression, realistic oil painting style""",
    
    """Fantasy character portrait of an elven archer, 
    intricate leather armor, silver hair braided with leaves, 
    piercing green eyes, forest background, 
    detailed fantasy art, RPG character design"""
]
```

</details>

---

## 🔌 API Calls

<details style="border: 2px solid #2196f3; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #e3f2fd, #bbdefb);">
<summary style="font-weight: bold; font-size: 18px; color: #1976d2; cursor: pointer;">
📋 Click to expand API call Python code
</summary>

```python
import requests
import base64

# Configuration
base_url = "http://127.0.0.1:7680"
username = "admin"
apikey = "${APIKEY}"
auth = (username, apikey)

# 1. Switch model
model_data = {
    "sd_model_checkpoint": "sd3_medium_incl_clips_t5xxlfp16.safetensors"
}

print("Switching model...")
model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data, auth=auth)
print("Model switch completed")

# 2. Generate image
prompt = "a beautiful cat"
data = {
    "prompt": prompt,
    "steps": 20,
    "width": 512,
    "height": 512
}

print("Generating image...")
response = requests.post(f"{base_url}/sdapi/v1/txt2img", json=data, auth=auth)
result = response.json()

# 3. Save image
if "images" in result:
    image_data = base64.b64decode(result["images"][0])
    with open("output.png", "wb") as f:
        f.write(image_data)
    print("Image saved as output.png")
else:
    print("Error:", result)
```

</details>

---

## 🏆 Best Practices

### 🎯 Prompt Optimization

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); padding: 25px; border-radius: 12px; margin: 20px 0;">

1. **Detailed Description**: SD3 can better understand detailed descriptions
2. **Natural Language**: Use natural sentence structures rather than keyword stacking
3. **Specific Attributes**: Clearly specify colors, materials, lighting, and other attributes
4. **Style Guidance**: Clearly specify artistic or technical styles
5. **Reduce Negatives**: Focus on positive descriptions, reduce negative prompt usage

</div>

### ⚙️ Parameter Tuning Strategy

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #e3f2fd; padding: 20px; border-radius: 10px; text-align: center;">
  <h4 style="color: #1976d2; margin-top: 0;">🚀 Starting Settings</h4>
  <p style="margin-bottom: 0;">25 steps + CFG 6.0 + DPM++ 2M</p>
</div>

<div style="background: #fff3e0; padding: 20px; border-radius: 10px; text-align: center;">
  <h4 style="color: #f57c00; margin-top: 0;">⚡ Quick Preview</h4>
  <p style="margin-bottom: 0;">20 steps + CFG 5.0 for rapid testing</p>
</div>

<div style="background: #e8f5e8; padding: 20px; border-radius: 10px; text-align: center;">
  <h4 style="color: #2e7d32; margin-top: 0;">💎 High Quality</h4>
  <p style="margin-bottom: 0;">30 steps + CFG 6.5 for best results</p>
</div>

<div style="background: #fce4ec; padding: 20px; border-radius: 10px; text-align: center;">
  <h4 style="color: #c2185b; margin-top: 0;">🎨 Style Experimentation</h4>
  <p style="margin-bottom: 0;">Adjust CFG within 4.5-7.0 range for testing</p>
</div>

</div>

---

## 📊 Comparison with Other Models

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 25px; border-radius: 12px;">
  <h3 style="margin-top: 0;">🆚 vs Stable Diffusion 1.5</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Quality Improvement</strong>: Significantly higher image quality and detail</li>
    <li><strong>Text Understanding</strong>: More accurate complex text understanding</li>
    <li><strong>Anatomical Correctness</strong>: Fewer human body structure errors</li>
    <li><strong>Resource Requirements</strong>: Requires more VRAM and computational resources</li>
  </ul>
</div>

<div style="background: linear-gradient(135deg, #f093fb, #f5576c); color: white; padding: 25px; border-radius: 12px;">
  <h3 style="margin-top: 0;">🆚 vs Flux1-Dev</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Parameter Scale</strong>: SD3 Medium (2B) vs Flux1-Dev (12B)</li>
    <li><strong>Generation Speed</strong>: SD3 is relatively faster</li>
    <li><strong>Quality Level</strong>: Flux has higher quality in some aspects</li>
    <li><strong>Hardware Requirements</strong>: SD3 has relatively lower hardware requirements</li>
  </ul>
</div>

<div style="background: linear-gradient(135deg, #4facfe, #00f2fe); color: white; padding: 25px; border-radius: 12px;">
  <h3 style="margin-top: 0;">🆚 vs SDXL</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Architectural Advancement</strong>: SD3 uses newer MMDiT architecture</li>
    <li><strong>Text Encoding</strong>: SD3 integrates T5-XXL for stronger text understanding</li>
    <li><strong>Multi-Resolution</strong>: SD3 natively supports more resolutions</li>
    <li><strong>Parameter Efficiency</strong>: SD3 performs better with similar parameters</li>
  </ul>
</div>

</div>

---

## 🔧 Common Issues and Solutions

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: #ffebee; padding: 20px; border-radius: 12px; border-left: 5px solid #f44336;">
  <h4 style="color: #d32f2f; margin-top: 0;">🎨 Generation Quality Issues</h4>
  <ol style="margin-bottom: 0;">
    <li><strong>CFG Too High</strong>: Lower CFG to 4.5-7.0 range</li>
    <li><strong>Insufficient Steps</strong>: Increase to 25-30 steps</li>
    <li><strong>Overly Simple Prompts</strong>: Use more detailed descriptions</li>
  </ol>
</div>

<div style="background: #fff3e0; padding: 20px; border-radius: 12px; border-left: 5px solid #ff9800;">
  <h4 style="color: #f57c00; margin-top: 0;">⚡ Performance Issues</h4>
  <ol style="margin-bottom: 0;">
    <li><strong>Insufficient VRAM</strong>: Lower resolution or use medvram mode</li>
    <li><strong>Slow Loading</strong>: SD3 model is large, requires patience</li>
    <li><strong>Slow Generation</strong>: Use fewer steps or faster samplers</li>
  </ol>
</div>

<div style="background: #e8f5e8; padding: 20px; border-radius: 12px; border-left: 5px solid #4caf50;">
  <h4 style="color: #2e7d32; margin-top: 0;">🔧 Compatibility Issues</h4>
  <ol style="margin-bottom: 0;">
    <li><strong>WebUI Version</strong>: Ensure using latest version that supports SD3</li>
    <li><strong>Extension Compatibility</strong>: Some extensions may not be compatible with SD3</li>
    <li><strong>Parameter Range</strong>: Note SD3's recommended parameter ranges</li>
  </ol>
</div>

</div>

---

## 📚 Related Resources

<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); padding: 25px; border-radius: 12px; margin: 20px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">

<div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0; color: #1976d2;">📄 Official Documentation</h4>
  <ul style="margin-bottom: 0; list-style: none; padding: 0;">
    <li>• <a href="https://stability.ai/research/stable-diffusion-3" style="color: #1976d2; text-decoration: none;">Stable Diffusion 3 Official Paper</a></li>
    <li>• <a href="https://stability.ai/news/stable-diffusion-3-research-paper" style="color: #1976d2; text-decoration: none;">SD3 Technical Report</a></li>
  </ul>
</div>

<div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0; color: #f57c00;">🤗 Model Resources</h4>
  <ul style="margin-bottom: 0; list-style: none; padding: 0;">
    <li>• <a href="https://huggingface.co/stabilityai/stable-diffusion-3-medium" style="color: #f57c00; text-decoration: none;">Hugging Face SD3 Model Page</a></li>
    <li>• <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/SD3" style="color: #f57c00; text-decoration: none;">WebUI SD3 Support Documentation</a></li>
  </ul>
</div>

<div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h4 style="margin-top: 0; color: #2e7d32;">📖 Guides & Tutorials</h4>
  <ul style="margin-bottom: 0; list-style: none; padding: 0;">
    <li>• <a href="https://stability.ai/news/stable-diffusion-3-prompt-guide" style="color: #2e7d32; text-decoration: none;">SD3 Prompt Engineering Guide</a></li>
  </ul>
</div>

</div>

</div>

---

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 12px; color: white; text-align: center; margin-top: 40px;">
  <p style="margin: 0; font-size: 1.1em;">🎉 Happy creating with Stable Diffusion 3 Medium! 🎨</p>
</div>