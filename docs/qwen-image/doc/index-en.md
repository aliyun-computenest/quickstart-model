<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎨 Qwen-Image</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Qwen Series Image Generation Foundation Model - Specialized in Complex Text Rendering & Precise Image Editing</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 Text Rendering</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">✨ Image Editing</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🧠 Intelligent Understanding</span>
  </div>
</div>

## 🌟 Model Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

We are thrilled to introduce **Qwen-Image**, an image generation foundation model in the Qwen series that achieves significant breakthroughs in **complex text rendering** and **precise image editing**.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 Core Advantages</strong><br>
  Experiments demonstrate that this model possesses powerful general capabilities in image generation and editing, with particularly outstanding performance in text rendering, especially for Chinese characters.
</div>

</div>

## 🔧 Technical Specifications

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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Text-to-Image Generation (T2I)</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Architecture</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Diffusion Transformer</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Supported Resolutions</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Multiple aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3)</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Maximum Resolution</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">1664×928</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">Inference Steps</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Recommended 50 steps</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">CFG Guidance</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">true_cfg_scale: 4.0</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">License</td>
      <td style="padding: 12px;">Apache 2.0</td>
    </tr>
  </tbody>
</table>
</div>

---

# 🚀 Quick Start
---

# 🎨 ComfyUI Usage Guide

## 🌐 ComfyUI Web Interface Usage

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 Step 1: Access Interface
![img_3.png](img_3.png)
Access the ComfyUI interface through the service instance's access link

### 🔧 Step 2: Load Workflow

Select the Qwen-Image dedicated workflow template and remove the Lora node configuration
[img_4.png](img_4.png)

### ✍️ Step 3: Set Prompts

Fill in the description in the **TextEncode** node:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ Positive Prompt</h4>
<p style="margin: 0; color: #065f46;">Describe the desired image content and style</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">❌ Negative Prompt</h4>
<p style="margin: 0; color: #9a3412;">Content you don't want to generate</p>
</div>

</div>

### ⚙️ Step 4: Configure Parameters

Set image resolution, inference steps, and other parameters

### 🎬 Step 5: Execute Generation

Click the execute button to start image generation

</div>

---

## 🔌 API Integration

## 🔑 Authentication Setup

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🌐 Get Server Address</h4>
<p style="margin: 0 0 12px 0;">Record the ComfyUI server's access address</p>

![img_3.png](img_3.png)
</div>
<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🔐 Get API Token</h4>
<p style="margin: 0 0 12px 0;">Obtain the access token from the top-right corner of ComfyUI interface</p>

![img_1.png](img_1.png)
</div>

</div>

## 💻 Python API Integration Example

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 Click to expand complete Python API integration code
</summary>

```python
import requests
import json
import uuid
import time
import random
import os

# 🔧 Configuration Parameters
COMFYUI_SERVER = "your-server-address"
COMFYUI_TOKEN = "your-api-token"

# 🎯 Qwen-Image Model Files
UNET_MODEL = "qwen_image_fp8_e4m3fn.safetensors"
CLIP_MODEL = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE_MODEL = "qwen_image_vae.safetensors"

class QwenImageClient:
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url = f"http://{server}"
        self.token = token
        self.client_id = str(uuid.uuid4())
        self.headers = {
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {token}"} if token else {})
        }

    def generate_image(self, prompt, negative_prompt="", width=1328, height=1328, steps=20, cfg=2.5, shift=3.1, seed=None):
        """🎨 Generate Image"""
        if seed is None:
            seed = random.randint(1, 1000000000000000)
        
        workflow = {
            "3": {
                "inputs": {
                    "seed": seed,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "denoise": 1,
                    "model": ["66", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["58", 0]
                },
                "class_type": "KSampler",
                "_meta": {
                    "title": "KSampler"
                }
            },
            "6": {
                "inputs": {
                    "text": prompt,
                    "clip": ["38", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {
                    "title": "CLIP Text Encode (Positive Prompt)"
                }
            },
            "7": {
                "inputs": {
                    "text": negative_prompt,
                    "clip": ["38", 0]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {
                    "title": "CLIP Text Encode (Negative Prompt)"
                }
            },
            "8": {
                "inputs": {
                    "samples": ["3", 0],
                    "vae": ["39", 0]
                },
                "class_type": "VAEDecode",
                "_meta": {
                    "title": "VAE Decode"
                }
            },
            "37": {
                "inputs": {
                    "unet_name": UNET_MODEL,
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader",
                "_meta": {
                    "title": "Load Diffusion Model"
                }
            },
            "38": {
                "inputs": {
                    "clip_name": CLIP_MODEL,
                    "type": "qwen_image",
                    "device": "default"
                },
                "class_type": "CLIPLoader",
                "_meta": {
                    "title": "Load CLIP"
                }
            },
            "39": {
                "inputs": {
                    "vae_name": VAE_MODEL
                },
                "class_type": "VAELoader",
                "_meta": {
                    "title": "Load VAE"
                }
            },
            "58": {
                "inputs": {
                    "width": width,
                    "height": height,
                    "batch_size": 1
                },
                "class_type": "EmptySD3LatentImage",
                "_meta": {
                    "title": "EmptySD3LatentImage"
                }
            },
            "60": {
                "inputs": {
                    "filename_prefix": "qwen-image",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage",
                "_meta": {
                    "title": "Save Image"
                }
            },
            "66": {
                "inputs": {
                    "shift": shift,
                    "model": ["37", 0]
                },
                "class_type": "ModelSamplingAuraFlow",
                "_meta": {
                    "title": "ModelSamplingAuraFlow"
                }
            }
        }

        print("📤 Submitting Qwen-Image generation task...")
        response = requests.post(
            f"{self.base_url}/prompt",
            headers=self.headers,
            json={"prompt": workflow, "client_id": self.client_id}
        )
        
        print(f"API Response: {response.text}")
        result = response.json()
        if "error" in result:
            raise Exception(f"Workflow error: {result['error']}")
        if "prompt_id" not in result:
            raise Exception(f"No prompt_id in response: {result}")
        
        return result["prompt_id"]

    def get_status(self, task_id):
        """📊 Get Task Status"""
        try:
            # Check queue status
            queue_response = requests.get(f"{self.base_url}/queue", headers=self.headers)
            queue_data = queue_response.json()
            
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

    def download_image(self, task_id, output_path="qwen_image_output.png"):
        """📥 Download Generated Image"""
        try:
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            
            if task_id in history:
                outputs = history[task_id]['outputs']
                for node_id, output in outputs.items():
                    if 'images' in output:
                        for image_info in output['images']:
                            filename = image_info['filename']
                            image_response = requests.get(
                                f"{self.base_url}/view?filename={filename}",
                                headers=self.headers
                            )
                            
                            with open(output_path, "wb") as f:
                                f.write(image_response.content)
                            
                            return output_path
            
            return None
        except Exception as e:
            print(f"Download error: {e}")
            return None

def main():
    """🚀 Main Function - Execute Qwen-Image Generation Task"""
    client = QwenImageClient()
    
    try:
        print("🎨 Starting Qwen-Image generation task...")
        
        # 🎯 Example Prompt - Hong Kong Neon Street Scene
        prompt = '''A vibrant, warm neon-lit street scene in Hong Kong at the afternoon, with a mix of colorful Chinese and English signs glowing brightly. The atmosphere is lively, cinematic, and rain-washed with reflections on the pavement. The colors are vivid, full of pink, blue, red, and green hues. Crowded buildings with overlapping neon signs. 1980s Hong Kong style. Signs include:
"龍鳳冰室" "金華燒臘" "HAPPY HAIR" "鴻運茶餐廳" "EASY BAR" "永發魚蛋粉" "添記粥麵" "SUNSHINE MOTEL" "美都餐室" "富記糖水" "太平館" "雅芳髮型屋" "STAR KTV" "銀河娛樂城" "百樂門舞廳" "BUBBLE CAFE" "萬豪麻雀館" "CITY LIGHTS BAR" "瑞祥香燭莊" "文記文具" "GOLDEN JADE HOTEL" "LOVELY BEAUTY" "合興百貨" "興旺電器" And the background is warm yellow street and with all stores' lights on.'''
        
        negative_prompt = "low quality, blurry, distorted, bad anatomy, deformed text"
        
        print(f"📝 Prompt: {prompt[:100]}...")
        
        # 🎨 Generate Image
        task_id = client.generate_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=1328,
            height=1328,
            steps=20,
            cfg=2.5,
            shift=3.1
        )
        
        print(f"🆔 Task ID: {task_id}")
        
        # ⏳ Wait for completion
        while True:
            status = client.get_status(task_id)
            print(f"📊 Current status: {status}")
            
            if status == "completed":
                print("✅ Image generation completed!")
                break
            elif status == "failed":
                print("❌ Image generation failed!")
                exit(1)
            
            time.sleep(10)
        
        # 📥 Download image
        output_file = client.download_image(task_id, "qwen_image_hongkong.png")
        if output_file:
            print(f"🎉 Image downloaded successfully! Saved as: {output_file}")
        else:
            print("❌ Image download failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# 🎯 Preset Example Functions
def generate_text_examples():
    """📝 Generate Different Types of Text Rendering Examples"""
    client = QwenImageClient()
    
    examples = [
        {
            "name": "Coffee Shop Sign",
            "prompt": '''A cozy coffee shop entrance with a wooden chalkboard sign reading "Qwen Coffee ☕ 通义咖啡" in beautiful handwritten style. Below it shows "今日特价 Today's Special: 拿铁 Latte ¥25". The scene has warm lighting and vintage atmosphere.''',
            "filename": "coffee_shop_sign.png"
        },
        {
            "name": "Math Formula Blackboard",
            "prompt": '''A university classroom blackboard with mathematical equations written in white chalk: "E=mc²", "π≈3.14159265359", "∫f(x)dx", "∑(n=1 to ∞)", "√(a²+b²)=c". The handwriting is clear and academic style.''',
            "filename": "math_blackboard.png"
        },
        {
            "name": "Bilingual Bookstore",
            "prompt": '''A traditional bookstore with bilingual signs: "书香门第 Book Paradise", "新书上架 New Arrivals", "文学小说 Literature", "历史传记 Biography", "儿童读物 Children's Books". Warm wooden shelves filled with books.''',
            "filename": "bilingual_bookstore.png"
        },
        {
            "name": "Japanese Ramen Shop",
            "prompt": '''A Japanese ramen shop with neon signs displaying: "らーめん Ramen", "味噌ラーメン Miso Ramen ¥800", "醤油ラーメン Shoyu Ramen ¥750", "豚骨ラーメン Tonkotsu Ramen ¥850". Traditional red lanterns and warm lighting.''',
            "filename": "ramen_shop_signs.png"
        }
    ]
    
    for example in examples:
        try:
            print(f"\n🎨 Generating example: {example['name']}")
            task_id = client.generate_image(
                prompt=example['prompt'],
                negative_prompt="low quality, blurry, illegible text, distorted characters",
                width=1328,
                height=1328,
                steps=20,
                cfg=2.5
            )
            
            # Wait for completion
            while client.get_status(task_id) != "completed":
                time.sleep(5)
            
            # Download
            output_file = client.download_image(task_id, example['filename'])
            if output_file:
                print(f"✅ {example['name']} generation completed: {output_file}")
            
        except Exception as e:
            print(f"❌ {example['name']} generation failed: {e}")

if __name__ == "__main__":
    # Run main example
    main()
    
    # Optional: Run multiple text rendering examples
    # generate_text_examples()

```
</details>