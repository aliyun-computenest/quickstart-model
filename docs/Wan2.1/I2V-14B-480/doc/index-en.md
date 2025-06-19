# 🎬 Wan2.1-I2V-14B Model Guide

> Transform static images into dynamic videos with AI-powered generation!

---

## 🚀 Model Introduction

**Wan2.1-I2V-14B** is a powerful image-to-video generation model that can generate high-quality video content based on input images and text prompts. The model maintains the main characteristics of the input image while adding dynamic effects and scene changes according to text descriptions.

### ✨ Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
<h4>🧠 Parameter Scale</h4>
14B parameters providing powerful image understanding and video generation capabilities
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
<h4>🖼️ Image-Driven</h4>
Generates coherent video sequences based on input images
</div>

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
<h4>🌍 Multi-language Support</h4>
Supports Chinese and English text prompts
</div>

<div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
<h4>🎯 Image Consistency</h4>
Maintains main features and style of the input image
</div>

</div>

### 🔧 Technical Specifications

<div style="background: linear-gradient(145deg, #f0f8ff, #e6f3ff); border: 2px solid #2196F3; border-radius: 15px; padding: 25px; margin: 20px 0; box-shadow: 0 8px 16px rgba(33, 150, 243, 0.2);">

| Specification | Value |
|---------------|-------|
| 🤖 **Model Type** | Image-to-Video Generation |
| ⚡ **Quantization** | FP8 quantized version |
| 📺 **Supported Resolution** | 480p |
| 🎞️ **Maximum Frames** | 81 frames |
| 🎬 **Recommended Frame Rate** | 16fps |
| 📁 **Input Format** | JPEG, PNG, WebP, etc. |

</div>

---

## 📖 Usage Instructions

### 🌐 Web UI Usage

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 15px; padding: 25px; margin: 20px 0;">

#### Step 1: Access Interface
Click the access link at the service instance
![img_3.png](img_3.png)

#### Step 2: Select Workflow
Select `wanx-21.json` workflow and open it, choose the image-to-video function option

#### Step 3: Upload Image
- Select sample image in LoadImage node
- Or upload custom image from local computer

#### Step 4: Set Text Description
- Fill in description words in TextEncode node
- **Top**: Describe desired actions and scene changes
- **Bottom**: Content you don't want to generate

#### Step 5: Configure Parameters
Set resolution and frame count in ImageClip Encode

#### Step 6: Execute Workflow
Click execute button to start generation

</div>

### 🔌 API Integration

#### 🔑 Authentication Setup

<div style="background-color: #fff3cd; border: 2px solid #ffeaa7; border-radius: 12px; padding: 20px; margin: 20px 0;">

**🎫 Get Token:** Click the button in the upper right corner, open the bottom panel
![img_1.png](img_1.png)

**🌐 Get Server Address:** For COMFYUI_SERVER acquisition, refer to:
![img_3.png](img_3.png)

</div>

#### 💻 Python Implementation

<details style="border: 3px solid #2196F3; border-radius: 15px; padding: 25px; margin: 25px 0; background: linear-gradient(145deg, #f0f8ff, #e3f2fd); box-shadow: 0 10px 20px rgba(33, 150, 243, 0.3);">
<summary style="font-weight: bold; font-size: 22px; color: white; cursor: pointer; padding: 20px; background: linear-gradient(135deg, #2196F3, #1976D2); border-radius: 12px; margin: -25px -25px 25px -25px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; justify-content: center;">
🐍 Click to Expand Complete Python Code
</summary>

```python
import requests, json, uuid, time, random, os

# Configuration parameters
COMFYUI_SERVER, COMFYUI_TOKEN = "Enter your server address", "Enter your token"
T5_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors"
VIDEO_MODEL = "Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors"
VAE_MODEL = "wan2.1/Wan2_1_VAE_bf16.safetensors"
CLIP_MODEL = "wan2.1/open-clip-xlm-roberta-large-vit-huge-14_visual_fp16.safetensors"

# Preset parameters
IMAGE_PATH = "girl.png"
PROMPT = "A beautiful anime girl with long flowing hair, graceful movements, smooth animation, cinematic lighting, high quality"
NEG_PROMPT = "bad quality video, low quality, blurry, distorted, choppy animation, static, bad anatomy"

class ComfyUIClient:
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

   def generate_i2v(self, image_path, prompt, neg_prompt, steps=10, cfg=6, width=512, height=512, frames=81):
      """Image-to-Video - Fixed clip_vision input"""
      print("📤 Uploading image...")
      image_name = self.upload_image(image_path)
      print(f"✅ Image uploaded successfully: {image_name}")

      workflow = {
         "42": {"inputs": {"image": image_name, "upload": "image"}, "class_type": "LoadImage"},
         "43": {"inputs": {"model_name": VAE_MODEL, "precision": "bf16"}, "class_type": "WanVideoVAELoader"},
         "44": {"inputs": {"model_name": CLIP_MODEL, "precision": "fp16", "load_device": "offload_device"}, "class_type": "LoadWanVideoClipTextEncoder"},
         "45": {"inputs": {"model_name": T5_MODEL, "precision": "bf16", "load_device": "offload_device", "quantization": "disabled"}, "class_type": "LoadWanVideoT5TextEncoder"},
         "46": {"inputs": {"blocks_to_swap": 10, "offload_img_emb": False, "offload_txt_emb": False, "use_non_blocking": True, "vace_blocks_to_swap": 0}, "class_type": "WanVideoBlockSwap"},
         "47": {"inputs": {"backend": "inductor", "fullgraph": False, "mode": "default", "dynamic": False, "dynamo_cache_size_limit": 64, "compile_transformer_blocks_only": True, "dynamo_recompile_limit": 128}, "class_type": "WanVideoTorchCompileSettings"},
         "48": {"inputs": {"model": VIDEO_MODEL, "base_precision": "bf16", "quantization": "fp8_e4m3fn", "load_device": "offload_device", "attention_mode": "sageattn", "block_swap_args": ["46", 0]}, "class_type": "WanVideoModelLoader"},
         "49": {"inputs": {"positive_prompt": prompt, "negative_prompt": neg_prompt, "force_offload": True, "t5": ["45", 0]}, "class_type": "WanVideoTextEncode"},
         "50": {
            "inputs": {
               "generation_width": width,
               "generation_height": height,
               "num_frames": frames,
               "force_offload": True,
               "noise_aug_strength": 0,
               "latent_strength": 1,
               "clip_embed_strength": 1,
               "adjust_resolution": True,
               "image": ["42", 0],
               "vae": ["43", 0],
               "clip_vision": ["44", 0]
            },
            "class_type": "WanVideoImageClipEncode"
         },
         "52": {"inputs": {"steps": steps, "cfg": cfg, "shift": 5, "seed": random.randint(1, 1000000), "force_offload": True, "scheduler": "dpm++", "riflex_freq_index": 0, "denoise_strength": 1, "batched_cfg": False, "rope_function": "comfy", "model": ["48", 0], "text_embeds": ["49", 0], "image_embeds": ["50", 0]}, "class_type": "WanVideoSampler"},
         "53": {"inputs": {"enable_vae_tiling": True, "tile_x": 272, "tile_y": 272, "tile_stride_x": 144, "tile_stride_y": 128, "vae": ["43", 0], "samples": ["52", 0]}, "class_type": "WanVideoDecode"},
         "54": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "WanVideo2_1", "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19, "save_metadata": True, "trim_to_audio": False, "pingpong": False, "save_output": True, "images": ["53", 0]}, "class_type": "VHS_VideoCombine"}
      }

      print("📤 Submitting workflow...")
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

   def download_video(self, task_id, output_path="i2v_output.mp4"):
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
      print(f"🎬 Starting image-to-video task...")
      print(f"📷 Input image: {IMAGE_PATH}")
      print(f"📝 Prompt: {PROMPT}")

      if not os.path.exists(IMAGE_PATH):
         print(f"❌ Image file does not exist: {IMAGE_PATH}")
         print("Please ensure there is a girl.png file in the current directory")
         return

      task_id = client.generate_i2v(IMAGE_PATH, PROMPT, NEG_PROMPT, 10, 6, 512, 512, 81)
      print(f"🆔 Task ID: {task_id}")

      while True:
         status = client.get_status(task_id)
         print(f"📊 Current status: {status}")
         if status == "completed": print("✅ Video ready!"); break
         elif status == "failed": print("❌ Generation failed!"); exit(1)
         time.sleep(10)

      output_file = client.download_video(task_id, "i2v_output.mp4")
      print("🎉 Video downloaded successfully!" if output_file else "❌ Failed to download video")
      if output_file: print(f"📁 Saved as: {output_file}")

   except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__": main()
```

</details>

#### 🔗 ComfyUI API Endpoints

<div style="background: linear-gradient(145deg, #f8f9fa, #e9ecef); border-radius: 12px; padding: 20px; margin: 20px 0; border: 2px solid #dee2e6;">

| Endpoint | Method | Function | Description |
|----------|--------|----------|-------------|
| 🔍 `/queue` | GET | Get queue status | View current task queue |
| 🚀 `/prompt` | POST | Submit workflow | Execute generation task |
| 📊 `/history/{prompt_id}` | GET | Get execution history | View task execution results |
| 📤 `/upload/image` | POST | Upload image | Upload input image file |
| 📥 `/view` | GET | Download output file | Get generated result files |

</div>

---

## ⚙️ Parameter Configuration

### 🎛️ Generation Parameters

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; box-shadow: 0 8px 16px rgba(255, 154, 158, 0.3);">

**🔢 Steps**  
Inference steps (recommended 20-30)

**🎯 CFG**  
CFG guidance strength (recommended 6-8)

**📊 Shift**  
Noise schedule offset (recommended 5)

</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; box-shadow: 0 8px 16px rgba(168, 237, 234, 0.3);">

**🎲 Seed**  
Random seed (controls randomness)

**🎨 Denoise Strength**  
Denoising strength (0.6-0.9)

</div>

</div>

### 🖼️ Image Requirements

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 15px; margin: 20px 0;">

> **💡 Pro Tip:** High-quality input images are the key to excellent video generation!

- **📐 Resolution**: Recommended 512×512 or higher
- **📄 Format**: JPEG, PNG, WebP, etc.
- **🎯 Content**: Clear main subject, avoid overly complex backgrounds
- **✨ Quality**: High-quality images yield better video effects

</div>

---

## 💡 Prompt Engineering

### ✅ Positive Prompt Examples

<div style="background-color: #d4edda; border: 2px solid #c3e6cb; border-radius: 12px; padding: 20px; margin: 20px 0;">

- 🚶 **"The person in the image is walking slowly through a garden"**
- 🐱 **"The cat in the photo is playing with a ball of yarn"**
- 🚗 **"The car in the image is driving down a winding mountain road"**
- 💃 **"The dancer in the picture is performing elegant ballet movements"**

</div>

### ❌ Negative Prompt Examples

<div style="background-color: #f8d7da; border: 2px solid #f5c6cb; border-radius: 12px; padding: 20px; margin: 20px 0;">

- 🚫 **"static, motionless, frozen, distorted, blurry"**
- ⚠️ **"unnatural movement, jerky motion, inconsistent"**
- 📉 **"low quality, artifacts, noise, compression"**

</div>

---

## 🏆 Best Practices

### 📸 Input Image Selection

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 20px; border-radius: 12px; border-left: 5px solid #2196F3;">
<strong>🔍 Clarity</strong><br>
Choose high-definition images
</div>

<div style="background: linear-gradient(135deg, #f3e5f5, #e1bee7); padding: 20px; border-radius: 12px; border-left: 5px solid #9c27b0;">
<strong>🎯 Clear Subject</strong><br>
Ensure main objects are clearly visible
</div>

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); padding: 20px; border-radius: 12px; border-left: 5px solid #4caf50;">
<strong>🖼️ Composition</strong><br>
Avoid overly complex backgrounds
</div>

<div style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); padding: 20px; border-radius: 12px; border-left: 5px solid #ff9800;">
<strong>💡 Lighting</strong><br>
Images with even lighting work better
</div>

</div>

### ✍️ Prompt Writing Guidelines

<div style="background: linear-gradient(145deg, #f0f8ff, #e6f3ff); border: 2px solid #2196F3; border-radius: 15px; padding: 25px; margin: 20px 0;">

1. **📝 Specific Description**: Describe desired actions and scenes in detail
2. **🔄 Maintain Consistency**: Ensure descriptions match image content
3. **⚖️ Reasonable Actions**: Describe actions that follow physical laws
4. **🎨 Unified Style**: Maintain descriptions consistent with original image style

</div>

### 🔧 Parameter Tuning Guide

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; margin: 20px 0;">

**🎨 Denoising Strength**
- `0.6-0.7`: Preserve more original image features
- `0.8-0.9`: Allow more changes and dynamic effects

**🎯 CFG Value**
- `6-7`: Balanced guidance strength
- `8-10`: Stronger text guidance

**⏱️ Steps**
- `20-25`: Fast generation
- `25-30`: Higher quality

</div>

---

## ⚠️ Important Considerations

<div style="background-color: #fff3cd; border: 2px solid #ffeaa7; border-radius: 12px; padding: 25px; margin: 25px 0;">

1. **💾 Memory Management**: Image-to-video requires more VRAM than text-to-video
2. **🔧 Image Preprocessing**: Ensure input image size is appropriate
3. **🎯 Consistency Preservation**: Denoising strength should not be too high
4. **🎭 Action Reasonableness**: Described actions should match object characteristics
5. **⚡ Batch Processing**: Recommend processing one task at a time

</div>

---

## 🎯 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 25px 0;">

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255, 154, 158, 0.3);">
<h3>👤 Character Animation</h3>
Bring static character photos to life
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(168, 237, 234, 0.3);">
<h3>🛍️ Product Showcase</h3>
Add dynamic effects to product images
</div>

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255, 236, 210, 0.3);">
<h3>🎨 Artistic Creation</h3>
Convert paintings into dynamic videos
</div>

<div style="background: linear-gradient(135deg, #a8e6cf 0%, #dcedc1 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(168, 230, 207, 0.3);">
<h3>📚 Educational Demo</h3>
Make teaching images have dynamic effects
</div>

</div>

---

## 📚 Resources & Documentation

<div style="background: linear-gradient(145deg, #f8f9fa, #e9ecef); border-radius: 12px; padding: 25px; margin: 25px 0; border: 2px solid #dee2e6;">

- 📖 [ComfyUI Official Documentation](https://comfyui-wiki.com/zh/interface/node-options)
- 🎥 [WanVideo Plugin Documentation](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md)

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin: 40px 0; box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);">

## 🎉 Start Your Creative Journey!

**Transform your static images into captivating videos with Wan2.1-I2V-14B!**

*Unleash the power of AI-driven video generation*

</div>
