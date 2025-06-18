## Model Introduction

Stable Diffusion 1.5 is a classic text-to-image generation model developed by Stability AI. As a milestone work in the open-source AI image generation field, it remains one of the most popular and widely used models today. This model is renowned for its lightweight nature, high efficiency, and rich ecosystem, making it the preferred choice for AI image generation beginners.

### Core Features
- **Lightweight and Efficient**: Runs with only 6GB VRAM, low hardware requirements
- **Rich Ecosystem**: Large community and extensive ecosystem of extensions
- **Diverse Styles**: Supports realistic, anime, artistic, and various other styles
- **Stable and Reliable**: Verified through extensive real-world applications with stable generation results
- **Easy to Customize**: Supports fine-tuning techniques like LoRA and Textual Inversion
- **Fast Generation**: Quick inference speed, suitable for batch generation and real-time applications
- **Open Source and Free**: Completely open source with commercial use support

### Technical Specifications
- **Model Type**: Text-to-Image Generation or Image-to-Image Generation
- **Parameter Scale**: Approximately 860M parameters
- **Text Encoder**: CLIP ViT-L/14
- **VAE**: 512×512 native resolution VAE
- **Recommended Steps**: 20-50 steps

## Configuration Instructions

#### System Requirements
- **ECS GPU Memory**: 6GB or more

#### Model Files
- **Main Model**: `v1-5-pruned-emaonly.safetensors`
- **VAE**: Optional higher quality VAE such as `vae-ft-mse-840000-ema-pruned.safetensors`
- **Text Encoder**: Built into the main model

## Usage Guide

### Web UI Usage

#### Basic Operations
1. **Model Selection**: Select SD1.5 model in the upper left model selector ![img.png](img.png)
2. **Prompt Input**:
    - **Positive Prompt**: Detailed description of the desired image content
    - **Negative Prompt**: Description of unwanted elements (SD1.5 responds well to negative prompts)
3. **Parameter Settings**:
    - **Steps**: Recommended 20-30 steps
    - **CFG Scale**: Recommended 7-12
    - **Sampler**: Recommended DPM++ 2M Karras or Euler a
    - **Resolution**: 512×512 (native) or other supported sizes
4. **Advanced Settings**:
    - **Seed**: Controls randomness, -1 for random
    - **Batch**: Set generation quantity
    - **High-resolution Fix**: Generate larger size images

#### Recommended Parameter Combinations
- **Fast Generation**: 20 steps + CFG 7 + Euler a + 512×512
- **High Quality**: 30 steps + CFG 9-11 + DPM++ 2M Karras + 768×768
- **Artistic Style**: 25 steps + CFG 8-10 + DDIM + 512×768

### API Calls

Need to replace BASE_URL and APIKEY. ![img_4.png](img_4.png)
If using public network calls, select the public IP:port

<details>
<summary>Click to expand API call Python code</summary>

```python
import requests
import base64

# Configuration
base_url = "<Deployment service Output URL>"
username = "admin"
apikey = "${APIKEY}"
auth = (username, apikey)

# 1. Switch model
model_data = {
    "sd_model_checkpoint": "v1-5-pruned-emaonly.safetensors"
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

If APIKEY is not enabled, refer to the following code to modify the request:
```python
model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data)
```

### Related Resources

- [Stable Diffusion Official Documentation](https://stability.ai/stable-diffusion)
- [Automatic1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Civitai Model Community](https://civitai.com/)
- [Prompt Engineering Guide](https://prompthero.com/stable-diffusion-prompts)
- [LoRA Training Tutorial](https://github.com/cloneofsimo/lora)