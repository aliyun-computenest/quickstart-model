## Model Introduction

Wan2.1-T2V-1.3B is the lightweight version of the WanVideo 2.1 series text-to-video generation model, specifically designed for resource-constrained environments. This model significantly reduces hardware requirements while maintaining good video generation quality, enabling more users to experience text-to-video technology on consumer-grade devices.

### Core Features
- **Lightweight Design**: Only 1.3B parameters, significantly reducing resource requirements compared to the 14B version
- **Efficient Generation**: Optimized inference speed, suitable for real-time and batch generation
- **Low VRAM Requirements**: Runs with only 6GB VRAM, compatible with more devices
- **Multi-language Support**: Supports Chinese and English text prompts
- **Flexible Deployment**: Supports both single-machine and cluster deployment
- **Open Source Friendly**: Fully open source, supports secondary development and customization

### Technical Specifications
- **Maximum Frames**: 81 frames
- **Recommended Frame Rate**: 16fps
- **Recommended Steps**: 15-25 steps

### Comparison with 14B Version
- **Parameter Scale**: 1.3B vs 14B (approximately 10x difference)
- **VRAM Requirements**: 6GB+ vs 12GB+
- **Inference Speed**: Faster generation speed
- **Generation Quality**: Slightly lower but still maintains good standards
- **Use Cases**: More suitable for rapid prototyping and batch generation

## Deployment Architecture

### Method 1: ACS Cluster Deployment (Recommended)

#### System Configuration
- **VRAM**: GPU
- **Memory**: 96GB

### Method 2: ECS Deployment
- **VRAM**: A10 etc.
- **Memory**: 30GB

## Usage Guide

### ComfyUI Usage

1. **Access Interface**: Click the access link at the service instance. ![img_3.png](img_3.png)
2. Select workflow
3. Model selection
3. **Set Parameters**:
    - Input text description (supports Chinese and English)
    - Set video resolution and frame count
    - Adjust generation parameters (steps, CFG, etc.)
3. **Quick Generation**: Click "Generate" button
4. **Download Results**: Download video file after generation is complete

### ComfyUI API Call Example
Click the button in the upper right corner, open the bottom panel, and get the token: ![img_1.png](img_1.png)
For COMFYUI_SERVER acquisition, refer to: ![img_3.png](img_3.png)
<details>
<summary>Click to expand API call Python code</summary>

```python
import requests, json, uuid, time, random

# Configuration parameters
COMFYUI_SERVER, COMFYUI_TOKEN = "Enter your server address", "Enter your token"
T5_MODEL, VIDEO_MODEL, VAE_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors", "wan2.1/Wan2_1-T2V-1_3B_fp8_e4m3fn.safetensors", "wan2.1/Wan2_1_VAE_bf16.safetensors"

class ComfyUIClient:
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url, self.token, self.client_id = f"http://{server}", token, str(uuid.uuid4())
        self.headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})}

    def generate(self, prompt, neg_prompt="", steps=15, cfg=6, width=832, height=480, frames=81):
        workflow = {
            "1": {"inputs": {"model_name": T5_MODEL, "precision": "bf16"}, "class_type": "LoadWanVideoT5TextEncoder"},
            "2": {"inputs": {"positive_prompt": prompt, "negative_prompt": neg_prompt, "force_offload": True, "t5": ["1", 0]}, "class_type": "WanVideoTextEncode"},
            "3": {"inputs": {"model": VIDEO_MODEL, "base_precision": "bf16", "quantization": "fp8_e4m3fn", "load_device": "offload_device"}, "class_type": "WanVideoModelLoader"},
            "4": {"inputs": {"width": width, "height": height, "num_frames": frames}, "class_type": "WanVideoEmptyEmbeds"},
            "5": {"inputs": {"model_name": VAE_MODEL, "precision": "bf16"}, "class_type": "WanVideoVAELoader"},
            "6": {"inputs": {"steps": steps, "cfg": cfg, "shift": 5, "seed": random.randint(1, 1000000), "force_offload": True, "scheduler": "dpm++", "riflex_freq_index": 0, "model": ["3", 0], "text_embeds": ["2", 0], "image_embeds": ["4", 0]}, "class_type": "WanVideoSampler"},
            "7": {"inputs": {"enable_vae_tiling": True, "tile_x": 272, "tile_y": 272, "tile_stride_x": 144, "tile_stride_y": 128, "vae": ["5", 0], "samples": ["6", 0]}, "class_type": "WanVideoDecode"},
            "8": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "generated_video", "format": "video/h264-mp4", "save_output": True, "pingpong": False, "images": ["7", 0]}, "class_type": "VHS_VideoCombine"}
        }
        response = requests.post(f"{self.base_url}/prompt", headers=self.headers, json={"prompt": workflow, "client_id": self.client_id})
        print(f"API Response: {response.text}")
        result = response.json()
        if "error" in result: raise Exception(f"Workflow error: {result['error']}")
        if "prompt_id" not in result: raise Exception(f"No prompt_id in response: {result}")
        return result["prompt_id"]

    def get_status(self, task_id):
        try:
            queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])): return "processing"
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])): return "pending"
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            return "completed" if history_response.status_code == 200 and task_id in history_response.json() else "processing"
        except: return "processing"

    def download_video(self, task_id, output_path="generated_video.mp4"):
        try:
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            if task_id in history:
                for output in history[task_id]['outputs'].values():
                    if 'gifs' in output:
                        filename = output['gifs'][0]['filename']
                        video_response = requests.get(f"{self.base_url}/view?filename={filename}", headers=self.headers)
                        with open(output_path, "wb") as f: f.write(video_response.content)
                        return output_path
        except Exception as e: print(f"Download error: {e}")
        return None

def main():
    client = ComfyUIClient()
    try:
        print("🎬 Starting text-to-video task...")
        task_id = client.generate("A beautiful anime girl with long black hair dancing gracefully", "low quality, blurry, distorted", 15, 6, 832, 480, 81)
        print(f"🆔 Task ID: {task_id}")
        
        while True:
            status = client.get_status(task_id)
            print(f"📊 Current status: {status}")
            if status == "completed": print("✅ Video ready!"); break
            elif status == "failed": print("❌ Generation failed!"); exit(1)
            time.sleep(10)
            
        output_file = client.download_video(task_id, "generated_video.mp4")
        print("🎉 Video downloaded successfully!" if output_file else "❌ Failed to download video")
        if output_file: print(f"📁 Saved as: {output_file}")
        
    except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__": main()
```
</details>

## Performance Comparison and Selection Guide

### Comparison with 14B Version

| Feature | T2V-1.3B | T2V-14B |
|---------|----------|---------|
| Parameter Scale | 1.3B | 14B |
| VRAM Requirements | 6GB+ | 12GB+ |
| Generation Speed | Fast | Medium |
| Video Quality | Good | Excellent |
| Detail Richness | Medium | High |
| Text Understanding | Good | Excellent |
| Use Cases | Fast generation, batch processing | High-quality creation |

## Best Practices

### Prompt Optimization
1. **Concise and Clear**: Lightweight version responds better to concise prompts
2. **Highlight Keywords**: Use core keywords to describe main content
3. **Avoid Over-complexity**: Reduce overly complex scene descriptions
4. **Style Specification**: Clearly specify video style and atmosphere

## Troubleshooting

### Common Issues
1. **Insufficient VRAM**: Lower resolution or enable lowvram mode
2. **Poor Generation Quality**: Increase steps or adjust CFG
3. **Too Slow**: Check quantization settings and offload configuration
4. **Model Loading Failed**: Confirm model file path and permissions

## Related Resources

- [WanVideo 2.1 Official Documentation](https://github.com/WanVideo/Wan2.1)
- [Lightweight Model Download](https://huggingface.co/WanVideo/Wan2.1-T2V-1.3B)
- [ComfyUI WanVideo Plugin](https://github.com/kijai/ComfyUI-WanVideoWrapper)
