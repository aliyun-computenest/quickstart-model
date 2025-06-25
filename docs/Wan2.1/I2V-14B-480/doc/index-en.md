<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 Wan2.1-I2V-14B Model Guide</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">Transform static images into dynamic videos with AI-powered generation</p>
</div>

## 🚀 Model Introduction

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <p style="line-height: 1.6; margin: 0;">
    <strong>Wan2.1-I2V-14B</strong> is a powerful image-to-video generation model that can generate high-quality video content based on input images and text prompts. The model maintains the main characteristics of the input image while adding dynamic effects and scene changes according to text descriptions.
  </p>
</div>

### ✨ Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <div style="font-size: 2em; margin-bottom: 12px; color: #2563eb;">🧠</div>
  <h4 style="margin: 0 0 8px 0; color: #1e40af;">Parameter Scale</h4>
  <p style="margin: 0; color: #64748b;">14B parameters providing powerful image understanding and video generation capabilities</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <div style="font-size: 2em; margin-bottom: 12px; color: #059669;">🖼️</div>
  <h4 style="margin: 0 0 8px 0; color: #1e40af;">Image-Driven</h4>
  <p style="margin: 0; color: #64748b;">Generates coherent video sequences based on input images</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <div style="font-size: 2em; margin-bottom: 12px; color: #ea580c;">🌍</div>
  <h4 style="margin: 0 0 8px 0; color: #1e40af;">Multi-language Support</h4>
  <p style="margin: 0; color: #64748b;">Supports Chinese and English text prompts</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <div style="font-size: 2em; margin-bottom: 12px; color: #2563eb;">🎯</div>
  <h4 style="margin: 0 0 8px 0; color: #1e40af;">Image Consistency</h4>
  <p style="margin: 0; color: #64748b;">Maintains main features and style of the input image</p>
</div>

</div>

### 🔧 Technical Specifications

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden;">
<thead>
<tr style="background: #eff6ff;">
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Specification</th>
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>🤖 Model Type</strong></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Image-to-Video Generation</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>⚡ Quantization</strong></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">FP8 quantized version</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>📺 Supported Resolution</strong></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">480p</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>🎞️ Maximum Frames</strong></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">81 frames</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>🎬 Recommended Frame Rate</strong></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16fps</td>
</tr>
<tr>
<td style="padding: 12px;"><strong>📁 Input Format</strong></td>
<td style="padding: 12px;">JPEG, PNG, WebP, etc.</td>
</tr>
</tbody>
</table>
</div>

</div>

## 📖 Usage Instructions

### 🌐 Web UI Usage

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

#### Step 1: Access Interface

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <p style="margin: 0 0 12px 0;">Click the access link at the service instance</p>
  <div style="text-align: center; margin: 16px 0;">
    <img src="img_3.png" alt="Access interface" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
    <p style="margin-top: 8px; color: #64748b; font-size: 14px;">Click access link to enter ComfyUI interface</p>
  </div>
</div>

#### Step 2: Select Workflow

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <p style="margin: 0;">Select <code style="background: #eff6ff; color: #1e40af; padding: 2px 6px; border-radius: 4px;">wanx-21.json</code> workflow and open it, choose the image-to-video function option</p>
</div>

#### Step 3: Upload Image

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <ul style="margin: 0; padding-left: 20px;">
    <li style="margin-bottom: 6px;">Select sample image in <strong>LoadImage</strong> node</li>
    <li style="margin-bottom: 0;">Or upload custom image from local computer</li>
  </ul>
</div>

#### Step 4: Set Text Description

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <p style="margin: 0 0 12px 0;">Fill in description words in <strong>TextEncode</strong> node:</p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <div style="background: #f0fdf4; padding: 12px; border-radius: 6px; border-left: 3px solid #059669;">
      <h5 style="margin: 0 0 6px 0; color: #059669;">✅ Top Input</h5>
      <p style="margin: 0; font-size: 14px; color: #64748b;">Describe desired actions and scene changes</p>
    </div>
    <div style="background: #fff7ed; padding: 12px; border-radius: 6px; border-left: 3px solid #ea580c;">
      <h5 style="margin: 0 0 6px 0; color: #ea580c;">❌ Bottom Input</h5>
      <p style="margin: 0; font-size: 14px; color: #64748b;">Content you don't want to generate</p>
    </div>
  </div>
</div>

#### Step 5: Configure Parameters

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <p style="margin: 0;">Set resolution and frame count in <strong>ImageClip Encode</strong></p>
</div>

#### Step 6: Execute Workflow

<div style="background: white; padding: 16px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;">
  <p style="margin: 0;">Click execute button to start generation</p>
</div>

</div>

### 🔌 API Integration

#### 🔑 Authentication Setup

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 12px 0;">🎫 Get Token</h4>
  <p style="margin: 0 0 12px 0;">Click the button in the upper right corner, open the bottom panel</p>
  <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 6px;">
    <img src="img_1.png" alt="Get token interface" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 12px 0;">🌐 Get Server Address</h4>
  <p style="margin: 0 0 12px 0;">For COMFYUI_SERVER acquisition, refer to:</p>
  <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 6px;">
    <img src="img_3.png" alt="Get server address" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  </div>
</div>

</div>

</div>

#### 💻 Python Implementation

<details style="border: 1px solid #e2e8f0; border-radius: 8px; margin: 16px 0; background: #f8fafc;">
<summary style="font-weight: 600; color: #1e40af; cursor: pointer; padding: 16px; background: #eff6ff; margin: 0; border-radius: 8px 8px 0 0;">
  🐍 Click to Expand Complete Python Code
</summary>

<div style="padding: 20px; background: white; margin: 0;">

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">

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

</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <h4 style="color: #059669; margin: 0 0 8px 0;">💡 Code Features</h4>
  <ul style="margin: 0; color: #059669;">
    <li>Complete ComfyUI client implementation</li>
    <li>Support for image upload, workflow submission, status monitoring</li>
    <li>Automatic video file download</li>
    <li>Detailed error handling and logging</li>
  </ul>
</div>

</div>

</details>

#### 🔗 ComfyUI API Endpoints

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden;">
<thead>
<tr style="background: #eff6ff;">
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Endpoint</th>
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Method</th>
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Function</th>
<th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><code>/queue</code></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">GET</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Get queue status</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">View current task queue</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><code>/prompt</code></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">POST</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Submit workflow</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Execute generation task</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><code>/history/{prompt_id}</code></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">GET</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Get execution history</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">View task execution results</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><code>/upload/image</code></td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">POST</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Upload image</td>
<td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Upload input image file</td>
</tr>
<tr>
<td style="padding: 12px;"><code>/view</code></td>
<td style="padding: 12px;">GET</td>
<td style="padding: 12px;">Download output file</td>
<td style="padding: 12px;">Get generated result files</td>
</tr>
</tbody>
</table>
</div>

</div>

## ⚙️ Parameter Configuration

### 🎛️ Generation Parameters

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <h4 style="margin: 0 0 16px 0; color: #1e40af;">🔢 Core Parameters</h4>
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; margin-bottom: 8px;">
    <strong>Steps</strong><br>
    <small style="color: #64748b;">Inference steps (recommended 20-30)</small>
  </div>
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; margin-bottom: 8px;">
    <strong>CFG</strong><br>
    <small style="color: #64748b;">CFG guidance strength (recommended 6-8)</small>
  </div>
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px;">
    <strong>Shift</strong><br>
    <small style="color: #64748b;">Noise schedule offset (recommended 5)</small>
  </div>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
  <h4 style="margin: 0 0 16px 0; color: #1e40af;">🎲 Randomness Control</h4>
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px; margin-bottom: 8px;">
    <strong>Seed</strong><br>
    <small style="color: #64748b;">Random seed (controls randomness)</small>
  </div>
  <div style="background: #eff6ff; padding: 12px; border-radius: 6px;">
    <strong>Denoise Strength</strong><br>
    <small style="color: #64748b;">Denoising strength (0.6-0.9)</small>
  </div>
</div>

</div>

### 🖼️ Image Requirements

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

> **💡 Pro Tip:** High-quality input images are the key to excellent video generation!

**📐 Resolution**: Recommended 512×512 or higher  
**📄 Format**: JPEG, PNG, WebP, etc.  
**🎯 Content**: Clear main subject, avoid overly complex backgrounds  
**✨ Quality**: High-quality images yield better video effects

</div>

## 💡 Prompt Engineering

### ✅ Positive Prompt Examples

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #059669; margin: 0 0 8px 0;">🚶 Character Actions</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"The person in the image is walking slowly through a garden"</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #059669; margin: 0 0 8px 0;">🐱 Animal Behavior</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"The cat in the photo is playing with a ball of yarn"</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #059669; margin: 0 0 8px 0;">🚗 Vehicle Movement</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"The car in the image is driving down a winding mountain road"</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #059669; margin: 0 0 8px 0;">💃 Artistic Performance</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"The dancer in the picture is performing elegant ballet movements"</p>
</div>

</div>

</div>

### ❌ Negative Prompt Examples

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0;">🚫 Static Issues</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"static, motionless, frozen, distorted, blurry"</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0;">⚠️ Motion Problems</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"unnatural movement, jerky motion, inconsistent"</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0;">📉 Quality Issues</h4>
  <p style="margin: 0; font-style: italic; color: #64748b;">"low quality, artifacts, noise, compression"</p>
</div>

</div>

</div>

## 🏆 Best Practices

### 📸 Input Image Selection

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; border-left: 4px solid #2563eb;">
  <h4 style="color: #1e40af; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🔍</span> Clarity Priority
  </h4>
  <p style="margin: 0; color: #64748b;">Choose high-definition images, avoid blurry or noisy pictures</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; border-left: 4px solid #059669;">
  <h4 style="color: #059669; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎯</span> Clear Subject
  </h4>
  <p style="margin: 0; color: #64748b;">Ensure main objects are clearly visible and occupy appropriate proportion</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; border-left: 4px solid #ea580c;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🖼️</span> Reasonable Composition
  </h4>
  <p style="margin: 0; color: #64748b;">Avoid overly complex backgrounds, keep composition clean</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; border-left: 4px solid #2563eb;">
  <h4 style="color: #1e40af; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>💡</span> Good Lighting
  </h4>
  <p style="margin: 0; color: #64748b;">Images with even lighting work better, avoid too dark or overexposed</p>
</div>

</div>

### ✍️ Prompt Writing Guidelines

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #059669;">
  <h4 style="color: #059669; margin: 0 0 12px 0;">📝 Specific Description</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.6;">Describe desired actions and scenes in detail, the more specific the better</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #2563eb;">
  <h4 style="color: #1e40af; margin: 0 0 12px 0;">🔄 Maintain Consistency</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.6;">Ensure descriptions match image content, avoid contradictions</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #ea580c;">
  <h4 style="color: #ea580c; margin: 0 0 12px 0;">⚖️ Reasonable Actions</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.6;">Describe actions that follow physical laws, avoid impossible movements</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #059669;">
  <h4 style="color: #059669; margin: 0 0 12px 0;">🎨 Unified Style</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.6;">Maintain descriptions consistent with original image style</p>
</div>

</div>

</div>

### 🔧 Parameter Tuning Guide

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="margin: 0 0 12px 0; color: #1e40af; display: flex; align-items: center; gap: 8px;">
    <span>🎨</span> Denoising Strength
  </h4>
  <div style="margin-bottom: 8px; color: #64748b;">
    <strong>0.6-0.7:</strong> Preserve more original image features
  </div>
  <div style="color: #64748b;">
    <strong>0.8-0.9:</strong> Allow more changes and dynamic effects
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="margin: 0 0 12px 0; color: #1e40af; display: flex; align-items: center; gap: 8px;">
    <span>🎯</span> CFG Value
  </h4>
  <div style="margin-bottom: 8px; color: #64748b;">
    <strong>6-7:</strong> Balanced guidance strength
  </div>
  <div style="color: #64748b;">
    <strong>8-10:</strong> Stronger text guidance
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="margin: 0 0 12px 0; color: #1e40af; display: flex; align-items: center; gap: 8px;">
    <span>⏱️</span> Steps
  </h4>
  <div style="margin-bottom: 8px; color: #64748b;">
    <strong>20-25:</strong> Fast generation
  </div>
  <div style="color: #64748b;">
    <strong>25-30:</strong> Higher quality
  </div>
</div>

</div>

</div>

## ⚠️ Important Considerations

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>💾</span> Memory Management
  </h4>
  <p style="margin: 0; color: #64748b;">Image-to-video requires more VRAM than text-to-video</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🔧</span> Image Preprocessing
  </h4>
  <p style="margin: 0; color: #64748b;">Ensure input image size is appropriate</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎯</span> Consistency Preservation
  </h4>
  <p style="margin: 0; color: #64748b;">Denoising strength should not be too high</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎭</span> Action Reasonableness
  </h4>
  <p style="margin: 0; color: #64748b;">Described actions should match object characteristics</p>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
  <h4 style="color: #ea580c; margin: 0 0 8px 0; display: flex; align-items: center; gap: 8px;">
    <span>⚡</span> Batch Processing
  </h4>
  <p style="margin: 0; color: #64748b;">Recommend processing one task at a time</p>
</div>

</div>

</div>

## 🎯 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center;">
  <div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">👤</div>
  <h4 style="margin: 0 0 12px 0; color: #1e40af;">Character Animation</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.5;">Bring static character photos to life with dynamic movements</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center;">
  <div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🛍️</div>
  <h4 style="margin: 0 0 12px 0; color: #1e40af;">Product Showcase</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.5;">Add dynamic effects to product images for enhanced marketing</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center;">
  <div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎨</div>
  <h4 style="margin: 0 0 12px 0; color: #1e40af;">Artistic Creation</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.5;">Convert paintings into dynamic videos for enhanced artistic expression</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center;">
  <div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">📚</div>
  <h4 style="margin: 0 0 12px 0; color: #1e40af;">Educational Demo</h4>
  <p style="margin: 0; color: #64748b; line-height: 1.5;">Make teaching images have dynamic effects for improved learning experience</p>
</div>

</div>

## 📚 Resources & Documentation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #2563eb;">
  <h4 style="color: #1e40af; margin: 0 0 12px 0; display: flex; align-items: center; gap: 8px;">
    <span>📖</span> ComfyUI Official Documentation
  </h4>
  <p style="margin: 0 0 12px 0; color: #64748b;">Detailed ComfyUI usage instructions and node descriptions</p>
  <a href="https://comfyui-wiki.com/zh/interface/node-options" style="color: #2563eb; text-decoration: none; font-weight: 500;">Visit Documentation →</a>
</div>

<div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0; border-top: 3px solid #059669;">
  <h4 style="color: #059669; margin: 0 0 12px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎥</span> WanVideo Plugin Documentation
  </h4>
  <p style="margin: 0 0 12px 0; color: #64748b;">Detailed usage instructions for WanVideo plugin</p>
  <a href="https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md" style="color: #059669; text-decoration: none; font-weight: 500;">View GitHub →</a>
</div>

</div>

</div>

---

<div style="text-align: center; padding: 32px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; color: white; margin: 24px 0;">
  <div style="font-size: 3em; margin-bottom: 16px;">🎉</div>
  <h2 style="font-size: 2em; margin: 0 0 16px 0; font-weight: 600;">Start Your Creative Journey!</h2>
  <p style="font-size: 1.1em; margin: 0 0 20px 0; opacity: 0.9; line-height: 1.5;">
    <strong>Transform your static images into captivating videos with Wan2.1-I2V-14B!</strong>
  </p>
  <p style="font-style: italic; opacity: 0.8; margin: 0;">Unleash the power of AI-driven video generation</p>
</div>