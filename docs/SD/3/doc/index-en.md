## Model Introduction

Stable Diffusion 3 Medium is the medium-parameter version of the third-generation diffusion model released by Stability AI, representing a significant advancement in open-source image generation technology. This model significantly improves image quality, text understanding capabilities, and generation diversity while maintaining relatively low hardware requirements, making it the perfect balanced choice between SD1.5 and high-end models.

### Core Features
- **Advanced Architecture**: Based on Multimodal Diffusion Transformer (MMDiT) architecture
- **Enhanced Text Understanding**: Integrated T5-XXL and dual CLIP text encoders
- **Balanced Performance**: 2 billion parameters, achieving optimal balance between quality and efficiency
- **Multi-Aspect Ratio Support**: Native support for various resolutions and aspect ratios
- **Improved Human Anatomy**: Significantly reduced hand and body structure errors
- **Better Text Rendering**: Improved quality of text generation in images
- **Style Diversity**: Supports various styles from realistic to artistic

### Technical Specifications
- **Model Type**: Text-to-Image Generation
- **Architecture**: Multimodal Diffusion Transformer (MMDiT)
- **Parameter Scale**: Approximately 2 billion parameters
- **Text Encoders**: T5-XXL + CLIP-L + CLIP-G
- **VAE**: Improved variational autoencoder
- **Native Resolution**: 1024×1024
- **Supported Resolutions**: 512×512 to 2048×2048
- **Recommended Steps**: 20-50 steps
- **CFG Range**: 4.5-9.0

## Configuration Instructions

#### System Requirements
- **ECS VRAM**: 8GB or more recommended

#### Model Files
- **Main Model**: `sd3_medium_incl_clips_t5xxlfp16.safetensors` (approximately 10GB)
- **Text Encoders**: Integrated in the main model
    - T5-XXL (FP16)
    - CLIP-L
    - CLIP-G
- **VAE**: Built-in improved VAE

## Usage Guide

### Web UI Usage

#### Basic Operations
1. **Model Selection**: Select SD3 Medium model in the model selector
2. **Prompt Input**:
    - **Positive Prompt**: Detailed description of desired image, supports more complex descriptions
    - **Negative Prompt**: SD3 responds weakly to negative prompts, can be simplified
3. **Parameter Settings**:
    - **Steps**: Recommended 20-30 steps
    - **CFG Scale**: Recommended 4.5-7.0 (lower than SD1.5)
    - **Sampler**: Recommended DPM++ 2M or Euler
    - **Resolution**: 1024×1024 (native) or other supported sizes
4. **Advanced Settings**:
    - **Seed**: Controls randomness
    - **Batch Settings**: Adjust according to VRAM capacity
    - **Multi-Aspect Ratio**: Utilize native multi-resolution support

## Parameter Description

### Core Parameters
- **steps**: Inference steps
    - 15-20 steps: Fast generation, acceptable quality
    - 20-30 steps: Balanced quality and speed (recommended)
    - 30-50 steps: Highest quality, slower speed
- **cfg_scale**: CFG guidance strength
    - 4.0-5.0: Natural results, less overfitting
    - 5.0-7.0: Balanced text following and naturalness (recommended)
    - 7.0-9.0: Strong text following, may be over-saturated
- **sampler**: Sampler selection
    - **DPM++ 2M**: High quality, recommended
    - **Euler**: Fast and stable
    - **DPM++ SDE**: High quality but slower
    - **DDIM**: Classic choice, stable results

### Resolution Settings
SD3 natively supports various resolutions:
- **1024×1024**: Standard square
- **1152×896**: Landscape 4:3.6
- **896×1152**: Portrait 3.6:4
- **1216×832**: Widescreen landscape
- **832×1216**: Tall screen portrait
- **1344×768**: Ultra-widescreen
- **768×1344**: Ultra-tall screen

### SD3-Specific Parameters
- **Lower CFG**: SD3 works best in the 4.5-7.0 range
- **Fewer Steps**: 20-25 steps are usually sufficient for good results
- **Native Multi-Resolution**: Can generate large images without high-resolution fix

## Prompt Techniques

### SD3 Prompt Characteristics
1. **Better Long Text Understanding**: Supports more detailed and complex descriptions
2. **Improved Concept Combination**: Better understanding of multiple concept combinations
3. **Precise Attribute Control**: More precise control over colors, materials, lighting, etc.
4. **Reduced Negative Dependency**: Less dependency on negative prompts

### High-Quality Prompt Structure
```
[Detailed subject description] + [Environment/Background] + [Style/Technique] + [Lighting/Atmosphere] + [Quality terms]
```

### Prompt Examples

#### Realistic Photography Style
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

#### Artistic Creation Style
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

#### Character Portraits
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

## API Calls
<details>
<summary>Click to expand API call Python code</summary>

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

## Best Practices

### Prompt Optimization
1. **Detailed Description**: SD3 can better understand detailed descriptions
2. **Natural Language**: Use natural sentence structures rather than keyword stacking
3. **Specific Attributes**: Clearly specify colors, materials, lighting, and other attributes
4. **Style Guidance**: Clearly specify artistic or technical styles
5. **Reduce Negatives**: Focus on positive descriptions, reduce negative prompt usage

### Parameter Tuning Strategy
1. **Starting Settings**: 25 steps + CFG 6.0 + DPM++ 2M
2. **Quick Preview**: 20 steps + CFG 5.0 for rapid testing
3. **High Quality**: 30 steps + CFG 6.5 for best results
4. **Style Experimentation**: Adjust CFG within 4.5-7.0 range for testing

## Comparison with Other Models

### vs Stable Diffusion 1.5
- **Quality Improvement**: Significantly higher image quality and detail
- **Text Understanding**: More accurate complex text understanding
- **Anatomical Correctness**: Fewer human body structure errors
- **Resource Requirements**: Requires more VRAM and computational resources

### vs Flux1-Dev
- **Parameter Scale**: SD3 Medium (2B) vs Flux1-Dev (12B)
- **Generation Speed**: SD3 is relatively faster
- **Quality Level**: Flux has higher quality in some aspects
- **Hardware Requirements**: SD3 has relatively lower hardware requirements

### vs SDXL
- **Architectural Advancement**: SD3 uses newer MMDiT architecture
- **Text Encoding**: SD3 integrates T5-XXL for stronger text understanding
- **Multi-Resolution**: SD3 natively supports more resolutions
- **Parameter Efficiency**: SD3 performs better with similar parameters

## Common Issues and Solutions

### Generation Quality Issues
1. **CFG Too High**: Lower CFG to 4.5-7.0 range
2. **Insufficient Steps**: Increase to 25-30 steps
3. **Overly Simple Prompts**: Use more detailed descriptions

### Performance Issues
1. **Insufficient VRAM**: Lower resolution or use medvram mode
2. **Slow Loading**: SD3 model is large, requires patience
3. **Slow Generation**: Use fewer steps or faster samplers

### Compatibility Issues
1. **WebUI Version**: Ensure using latest version that supports SD3
2. **Extension Compatibility**: Some extensions may not be compatible with SD3
3. **Parameter Range**: Note SD3's recommended parameter ranges

## Related Resources

- [Stable Diffusion 3 Official Paper](https://stability.ai/research/stable-diffusion-3)
- [SD3 Technical Report](https://stability.ai/news/stable-diffusion-3-research-paper)
- [Hugging Face SD3 Model Page](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
- [WebUI SD3 Support Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/SD3)
- [SD3 Prompt Engineering Guide](https://stability.ai/news/stable-diffusion-3-prompt-guide)