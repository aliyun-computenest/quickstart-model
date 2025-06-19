## Model Introduction

Wan2.1-VACE-1.3B is a lightweight model specifically designed for video content editing and processing. VACE (Video Adaptive Content Editing) technology focuses on intelligent editing of existing videos, including style conversion, content modification, scene enhancement, and other functions. This model maintains temporal consistency in videos while enabling precise editing of video content based on text instructions.

### Core Features
- **Parameter Scale**: 1.3B
- **Video Editing Specialized**: Specifically optimized for video editing tasks
- **Temporal Consistency**: Maintains coherence and consistency between video frames
- **Multiple Editing Functions**: Supports style conversion, content modification, scene enhancement, etc.
- **Fast Processing**: Lightweight architecture with fast processing speed
- **Memory Friendly**: Low VRAM requirements, suitable for resource-constrained environments
- **Multi-language Support**: Supports Chinese and English editing instructions

### Technical Specifications
- **Model Type**: Video Editing
- **Parameter Scale**: 1.3B
- **Quantization**: FP8 quantized version
- **Deployment Architecture**: ECS single-machine deployment/ACS cluster deployment
- **Supported Resolution**: 480P
- **Input Format**: Common video formats like MP4, AVI, MOV
- **Output Format**: MP4 (H.264 encoding)

### Editing Capabilities
- **Style Conversion**: Convert videos to different artistic styles
- **Color Adjustment**: Adjust video tone, saturation, brightness
- **Scene Modification**: Change video background or add new elements
- **Object Editing**: Modify or replace specific objects in videos
- **Effect Addition**: Add various visual effects to videos
- **Quality Enhancement**: Improve video clarity and quality

## Deployment Methods

### Deployment Architecture (Recommended)

#### Deployment Configuration
- **Deployment Architecture**: ECS single-machine deployment or ACS deployment

## Usage Guide

### ComfyUI Usage

1. **Access Interface**: Click the access link at the service instance. ![img_3.png](img_3.png)
2. Use workflow vace.json
3. Input prompts for the video or image you want to generate, click generate

### API Calls
Click the button in the upper right corner, open the bottom panel, and get the token: ![img_1.png](img_1.png)
For COMFYUI_SERVER acquisition, refer to: ![img_3.png](img_3.png)

<details style="border: 2px solid #0066cc; border-radius: 8px; padding: 15px; margin: 10px 0; background-color: #f8f9fa;">
  <summary style="font-weight: bold; font-size: 18px; color: #0066cc; cursor: pointer;">
    📋 Click to expand API call Python code
  </summary>

```python
import requests, json, uuid, time, random, os

# Configuration parameters
COMFYUI_SERVER, COMFYUI_TOKEN = "Enter your server address", "Enter your token"
UNET_MODEL = "wan21_vace_1_3_b.safetensors"
CLIP_MODEL = "umt5_xxl_fp8_e4m3fn.safetensors"
VAE_MODEL = "wan21_vace_vae.safetensors"

# Preset parameters
IMAGE_PATH = "example.png"
PROMPT = "A girl secretly takes a bite of an apple"
NEG_PROMPT = "vivid colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression artifacts, ugly, incomplete"

class VACEClient:
   def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
      self.base_url, self.token, self.client_id = f"http://{server}", token, str(uuid.uuid4())
      self.headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})}

   def upload_image(self, image_path):
      """Upload image to ComfyUI"""
      if not os.path.exists(image_path):
         raise Exception(f"Image file does not exist: {image_path}")

      try:
         with open(image_path, 'rb') as f:
            files = {'image': (os.path.basename(image_path), f, 'image/png')}
            headers = {}
            if self.token:
               headers["Authorization"] = f"Bearer {self.token}"

            response = requests.post(f"{self.base_url}/upload/image", files=files, headers=headers)
            print(f"Upload response: {response.text}")

            if response.status_code != 200:
               raise Exception(f"Upload failed, status code: {response.status_code}")

            result = response.json()
            if 'name' not in result:
               raise Exception(f"No filename in upload response: {result}")

            return result['name']
      except Exception as e:
         raise Exception(f"Image upload failed: {e}")

   def generate_vace(self, image_path, prompt, neg_prompt, steps=20, cfg=4, frames=49, width=480, height=480):
      """VACE video editing"""
      print("📤 Uploading image...")
      image_name = self.upload_image(image_path)
      print(f"✅ Image uploaded successfully: {image_name}")

      workflow = {
         "11": {"inputs": {"unet_name": UNET_MODEL, "weight_dtype": "fp8_e4m3fn_fast"}, "class_type": "UNETLoader"},
         "13": {"inputs": {"clip_name": CLIP_MODEL, "type": "wan", "device": "default"}, "class_type": "CLIPLoader"},
         "14": {"inputs": {"vae_name": VAE_MODEL}, "class_type": "VAELoader"},
         "15": {"inputs": {"text": prompt, "clip": ["13", 0]}, "class_type": "CLIPTextEncode"},
         "16": {"inputs": {"text": neg_prompt, "clip": ["13", 0]}, "class_type": "CLIPTextEncode"},
         "17": {"inputs": {"width": width, "height": height, "length": ["21", 0], "batch_size": 1, "strength": 1.0, "positive": ["15", 0], "negative": ["16", 0], "vae": ["14", 0]}, "class_type": "WanVaceToVideo"},
         "18": {"inputs": {"image": image_name, "upload": "image"}, "class_type": "LoadImage"},
         "21": {"inputs": {"value": frames}, "class_type": "INTConstant"},
         "22": {"inputs": {"width": width, "height": height, "upscale_method": "nearest-exact", "keep_proportion": "crop", "pad_color": "0, 0, 0", "crop_position": "center", "divisible_by": 2, "device": "gpu", "image": ["18", 0]}, "class_type": "ImageResizeKJv2"},
         "23": {"inputs": {"images": ["22", 0]}, "class_type": "PreviewImage"},
         "24": {"inputs": {"seed": random.randint(1, 1000000000000000), "steps": steps, "cfg": cfg, "sampler_name": "uni_pc", "scheduler": "simple", "denoise": 1, "model": ["27", 0], "positive": ["17", 0], "negative": ["17", 1], "latent_image": ["17", 2]}, "class_type": "KSampler"},
         "27": {"inputs": {"shift": 8.0, "model": ["11", 0]}, "class_type": "ModelSamplingSD3"},
         "30": {"inputs": {"trim_amount": ["17", 3], "samples": ["24", 0]}, "class_type": "TrimVideoLatent"},
         "31": {"inputs": {"samples": ["30", 0], "vae": ["14", 0]}, "class_type": "VAEDecode"},
         "32": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "VACE_video", "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19, "save_metadata": True, "trim_to_audio": False, "pingpong": False, "save_output": True, "images": ["31", 0]}, "class_type": "VHS_VideoCombine"}
      }

      print("📤 Submitting VACE workflow...")
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

   def download_video(self, task_id, output_path="vace_output.mp4"):
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
   client = VACEClient()
   try:
      print(f"🎬 Starting VACE video editing task...")
      print(f"📷 Input image: {IMAGE_PATH}")
      print(f"📝 Edit prompt: {PROMPT}")

      if not os.path.exists(IMAGE_PATH):
         print(f"❌ Image file does not exist: {IMAGE_PATH}")
         print("Please ensure there is an example.png file in the current directory")
         return

      task_id = client.generate_vace(IMAGE_PATH, PROMPT, NEG_PROMPT, 20, 4, 49, 480, 480)
      print(f"🆔 Task ID: {task_id}")

      while True:
         status = client.get_status(task_id)
         print(f"📊 Current status: {status}")
         if status == "completed": print("✅ Video ready!"); break
         elif status == "failed": print("❌ Generation failed!"); exit(1)
         time.sleep(10)

      output_file = client.download_video(task_id, "vace_output.mp4")
      print("🎉 Video downloaded successfully!" if output_file else "❌ Failed to download video")
      if output_file: print(f"📁 Saved as: {output_file}")

   except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__": main()
```
</details>

## Related Resources

- [VACE Technical Paper](https://arxiv.org/abs/vace-video-editing)
- [ComfyUI Video Editing Guide](https://comfyui-wiki.com/zh/video/editing)
- [Video Editing Best Practices](https://docs.comfy.org/video/best_practices)
- [VACE Plugin Documentation](https://github.com/kijai/ComfyUI-VACEWrapper)