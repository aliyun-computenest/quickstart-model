# 🎬 Wan2.1-T2V-14B Text-to-Video Model

> 🚀 Transform Words into Cinematic Magic! Revolutionary AI-powered video generation that brings your imagination to life with just a text prompt.

---

## 🌟 Model Introduction

**Wan2.1-T2V-14B** is a groundbreaking text-to-video generation model that creates stunning, high-quality video content from simple text descriptions. Whether for creative expression or commercial applications, this model opens up infinite possibilities for content creation!

### ✨ Core Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3); transition: transform 0.3s ease;">
<h4 style="margin: 0 0 15px 0; font-size: 18px;">🧠 Massive Parameter Scale</h4>
<p style="margin: 0; font-size: 16px; opacity: 0.9;">14B parameters delivering exceptional understanding and generation capabilities</p>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(240, 147, 251, 0.3); transition: transform 0.3s ease;">
<h4 style="margin: 0 0 15px 0; font-size: 18px;">🏗️ Advanced Architecture</h4>
<p style="margin: 0; font-size: 16px; opacity: 0.9;">Cutting-edge Diffusion Transformer + VAE technology</p>
</div>

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(79, 172, 254, 0.3); transition: transform 0.3s ease;">
<h4 style="margin: 0 0 15px 0; font-size: 18px;">⚡ Memory Optimization</h4>
<p style="margin: 0; font-size: 16px; opacity: 0.9;">FP8 quantization for efficient GPU utilization</p>
</div>

<div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(67, 233, 123, 0.3); transition: transform 0.3s ease;">
<h4 style="margin: 0 0 15px 0; font-size: 18px;">🌍 Multi-language Support</h4>
<p style="margin: 0; font-size: 16px; opacity: 0.9;">Seamless Chinese and English text processing</p>
</div>

<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(250, 112, 154, 0.3); transition: transform 0.3s ease;">
<h4 style="margin: 0 0 15px 0; font-size: 18px;">🎭 Complex Scene Understanding</h4>
<p style="margin: 0; font-size: 16px; opacity: 0.9;">Deep text comprehension for realistic scene generation</p>
</div>

</div>

### 🔧 Technical Specifications

<div style="background: linear-gradient(145deg, #f0f8ff, #e6f3ff); border: 3px solid #2196F3; border-radius: 20px; padding: 30px; margin: 30px 0; box-shadow: 0 15px 30px rgba(33, 150, 243, 0.2);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">

<div style="text-align: center; padding: 15px;">
<div style="font-size: 24px; margin-bottom: 10px;">🤖</div>
<strong>Model Type</strong><br>
<span style="color: #2196F3;">Text-to-Video Generation</span>
</div>

<div style="text-align: center; padding: 15px;">
<div style="font-size: 24px; margin-bottom: 10px;">⚡</div>
<strong>Quantization</strong><br>
<span style="color: #2196F3;">FP8 Quantized Version</span>
</div>

<div style="text-align: center; padding: 15px;">
<div style="font-size: 24px; margin-bottom: 10px;">🎞️</div>
<strong>Maximum Frames</strong><br>
<span style="color: #2196F3;">81 frames</span>
</div>

<div style="text-align: center; padding: 15px;">
<div style="font-size: 24px; margin-bottom: 10px;">🎬</div>
<strong>Frame Rate</strong><br>
<span style="color: #2196F3;">16fps (Recommended)</span>
</div>

</div>

</div>

---

## 📖 Usage Guide

### 🌐 Method 1: ComfyUI Visual Interface

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 20px; padding: 30px; margin: 25px 0; box-shadow: 0 10px 20px rgba(255, 236, 210, 0.4);">

#### 🚀 Quick Start Guide

<div style="background: rgba(255, 255, 255, 0.3); border-radius: 12px; padding: 20px; margin: 20px 0;">

**Step 1: Access Interface**  
Click the access link at the service instance
![img_3.png](img_3.png)

**Step 2: Select Workflow**  
Follow the guidance to select the workflow sidebar, choose `wanx-21.json` or `wans.json` and open it

**Step 3: Choose Function**  
Select text-to-video at the designated location

**Step 4: Write Prompts**  
Fill in description words at TextEncode
- **Upper section**: Content you want to generate ✅
- **Lower section**: Content you don't want to generate ❌
![img.png](img/prompt.png)

**Step 5: Configure Settings**  
Set image resolution and frame count at ImageClip Encode
![img.png](img/definition.png)

</div>

#### 📚 Additional Resources
- [ComfyUI Official Documentation](https://comfyui-wiki.com/zh/interface/node-options)
- [WanVideo Plugin Detailed Guide](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md)

</div>

### 🔌 Method 2: API Integration

#### 🔑 Authentication Setup

<div style="background-color: #fff3cd; border: 2px solid #ffeaa7; border-radius: 15px; padding: 25px; margin: 25px 0;">

**🎫 Get Token**  
Click the button in the upper right corner, open the bottom panel to get token
![img_1.png](img_1.png)

**🌐 Get Server Address**  
For COMFYUI_SERVER acquisition, refer to:
![img_3.png](img_3.png)

</div>

#### 💻 Python Implementation

<details style="border: 3px solid #2196F3; border-radius: 18px; padding: 30px; margin: 30px 0; background: linear-gradient(145deg, #f0f8ff, #e3f2fd); box-shadow: 0 15px 30px rgba(33, 150, 243, 0.3);">
<summary style="font-weight: bold; font-size: 24px; color: white; cursor: pointer; padding: 25px; background: linear-gradient(135deg, #2196F3, #1976D2); border-radius: 15px; margin: -30px -30px 30px -30px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 16px rgba(33, 150, 243, 0.4);">
🐍 Click to Expand Complete Python API Code
</summary>

```python
import requests, json, uuid, time, random

# 🔧 Configuration parameters
COMFYUI_SERVER, COMFYUI_TOKEN = "Enter your server address", "Enter your token"
T5_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors"
VIDEO_MODEL = "Wan2_1-T2V-14B_fp8_e4m3fn.safetensors"
VAE_MODEL = "wan2.1/Wan2_1_VAE_bf16.safetensors"

class ComfyUIClient:
    """🎬 ComfyUI Video Generation Client"""
    
    def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
        self.base_url = f"http://{server}"
        self.token = token
        self.client_id = str(uuid.uuid4())
        self.headers = {
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {token}"} if token else {})
        }

    def generate(self, prompt, neg_prompt="", steps=15, cfg=6, width=832, height=480, frames=81):
        """
        🎥 Generate Video
        
        Args:
            prompt (str): Positive prompt
            neg_prompt (str): Negative prompt
            steps (int): Inference steps
            cfg (float): CFG guidance strength
            width (int): Video width
            height (int): Video height
            frames (int): Number of frames
        
        Returns:
            str: Task ID
        """
        workflow = {
            "1": {
                "inputs": {
                    "model_name": T5_MODEL,
                    "precision": "bf16"
                },
                "class_type": "LoadWanVideoT5TextEncoder"
            },
            "2": {
                "inputs": {
                    "positive_prompt": prompt,
                    "negative_prompt": neg_prompt,
                    "force_offload": True,
                    "t5": ["1", 0]
                },
                "class_type": "WanVideoTextEncode"
            },
            "3": {
                "inputs": {
                    "model": VIDEO_MODEL,
                    "base_precision": "bf16",
                    "quantization": "fp8_e4m3fn",
                    "load_device": "offload_device"
                },
                "class_type": "WanVideoModelLoader"
            },
            "4": {
                "inputs": {
                    "width": width,
                    "height": height,
                    "num_frames": frames
                },
                "class_type": "WanVideoEmptyEmbeds"
            },
            "5": {
                "inputs": {
                    "model_name": VAE_MODEL,
                    "precision": "bf16"
                },
                "class_type": "WanVideoVAELoader"
            },
            "6": {
                "inputs": {
                    "steps": steps,
                    "cfg": cfg,
                    "shift": 5,
                    "seed": random.randint(1, 1000000),
                    "force_offload": True,
                    "scheduler": "dpm++",
                    "riflex_freq_index": 0,
                    "model": ["3", 0],
                    "text_embeds": ["2", 0],
                    "image_embeds": ["4", 0]
                },
                "class_type": "WanVideoSampler"
            },
            "7": {
                "inputs": {
                    "enable_vae_tiling": True,
                    "tile_x": 272,
                    "tile_y": 272,
                    "tile_stride_x": 144,
                    "tile_stride_y": 128,
                    "vae": ["5", 0],
                    "samples": ["6", 0]
                },
                "class_type": "WanVideoDecode"
            },
            "8": {
                "inputs": {
                    "frame_rate": 16,
                    "loop_count": 0,
                    "filename_prefix": "generated_video",
                    "format": "video/h264-mp4",
                    "save_output": True,
                    "pingpong": False,
                    "images": ["7", 0]
                },
                "class_type": "VHS_VideoCombine"
            }
        }
        
        print("🚀 Submitting video generation task...")
        response = requests.post(
            f"{self.base_url}/prompt",
            headers=self.headers,
            json={"prompt": workflow, "client_id": self.client_id}
        )
        
        print(f"📡 API Response: {response.text}")
        result = response.json()
        
        if "prompt_id" not in result:
            raise Exception(f"❌ No prompt_id in response: {result}")
        
        return result["prompt_id"]

    def get_status(self, task_id):
        """📊 Get task status"""
        try:
            queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
            
            # Check if in running queue
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])):
                return "processing"
            
            # Check if in pending queue
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])):
                return "pending"
            
            # Check history
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            if history_response.status_code == 200 and task_id in history_response.json():
                return "completed"
            
            return "processing"
        except:
            return "processing"

    def download_video(self, task_id, output_path="generated_video.mp4"):
        """📥 Download generated video"""
        try:
            response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            history = response.json()
            
            if task_id in history:
                for output in history[task_id]['outputs'].values():
                    if 'gifs' in output:
                        filename = output['gifs'][0]['filename']
                        video_response = requests.get(
                            f"{self.base_url}/view?filename={filename}",
                            headers=self.headers
                        )
                        
                        with open(output_path, "wb") as f:
                            f.write(video_response.content)
                        
                        return output_path
            
            return None
        except Exception as e:
            print(f"❌ Download error: {e}")
            return None

def main():
    """🎬 Main function - Video generation example"""
    client = ComfyUIClient()
    
    try:
        print("🎭 Starting text-to-video generation task...")
        
        # 🎨 Example prompts
        prompt = "A beautiful anime girl with long black hair dancing gracefully in a cherry blossom garden, soft lighting, cinematic quality"
        neg_prompt = "low quality, blurry, distorted, bad anatomy, static"
        
        print(f"📝 Prompt: {prompt}")
        print(f"🚫 Negative prompt: {neg_prompt}")
        
        # 🚀 Submit generation task
        task_id = client.generate(
            prompt=prompt,
            neg_prompt=neg_prompt,
            steps=15,
            cfg=6,
            width=832,
            height=480,
            frames=81
        )
        
        print(f"🆔 Task ID: {task_id}")
        
        # 📊 Monitor task status
        while True:
            status = client.get_status(task_id)
            print(f"📈 Current status: {status}")
            
            if status == "completed":
                print("✅ Video generation completed!")
                break
            elif status == "failed":
                print("❌ Generation failed!")
                exit(1)
            
            time.sleep(10)
        
        # 📥 Download video
        output_file = client.download_video(task_id, "my_generated_video.mp4")
        
        if output_file:
            print("🎉 Video downloaded successfully!")
            print(f"📁 Saved as: {output_file}")
        else:
            print("❌ Failed to download video!")
            
    except Exception as e:
        print(f"💥 Error occurred: {e}")

if __name__ == "__main__":
    main()
```

</details>

---

## 🎯 Creative Tips & Best Practices

### ✍️ Prompt Writing Guide

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #d4edda, #c3e6cb); border: 2px solid #28a745; border-radius: 15px; padding: 25px;">
<h4 style="color: #155724; margin-top: 0;">✅ Positive Prompt Tips</h4>
<ul style="color: #155724; margin: 0;">
<li><strong>Detailed Description</strong>: Describe scenes, characters, and actions in detail</li>
<li><strong>Style Specification</strong>: Add artistic styles and lighting effects</li>
<li><strong>Quality Keywords</strong>: Use "high quality", "cinematic", etc.</li>
<li><strong>Motion Description</strong>: Clearly specify desired dynamic effects</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #f8d7da, #f5c6cb); border: 2px solid #dc3545; border-radius: 15px; padding: 25px;">
<h4 style="color: #721c24; margin-top: 0;">❌ Negative Prompt Suggestions</h4>
<ul style="color: #721c24; margin: 0;">
<li><strong>Quality Control</strong>: "low quality", "blurry", "distorted"</li>
<li><strong>Avoid Static</strong>: "static", "motionless", "frozen"</li>
<li><strong>Anatomical Accuracy</strong>: "bad anatomy", "deformed"</li>
<li><strong>Technical Issues</strong>: "artifacts", "noise", "compression"</li>
</ul>
</div>

</div>

### 🎨 Creative Examples

<div style="background: linear-gradient(145deg, #f8f9fa, #e9ecef); border-radius: 15px; padding: 25px; margin: 25px 0;">

**🌸 Anime Style**
```
A beautiful anime girl with flowing pink hair dancing in a field of cherry blossoms, 
soft wind, petals falling, golden hour lighting, studio ghibli style, high quality
```

**🏙️ Sci-Fi Scene**
```
Futuristic cityscape at night, neon lights reflecting on wet streets, 
flying cars in the distance, cyberpunk aesthetic, cinematic composition
```

**🌊 Natural Landscape**
```
Majestic waterfall cascading down moss-covered rocks, rainbow mist, 
lush green forest, birds flying, peaceful atmosphere, 4K quality
```

**🎭 Fantasy Adventure**
```
Epic dragon soaring through stormy clouds, lightning illuminating its scales, 
medieval castle below, dramatic atmosphere, fantasy art style
```

</div>

---

## 🎛️ Parameter Optimization Guide

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); border: 2px solid #2196F3; border-radius: 15px; padding: 25px;">
<h4 style="color: #1976D2; margin-top: 0;">🔢 Steps Configuration</h4>
<ul style="color: #1976D2; margin: 0;">
<li><strong>10-15 steps</strong>: Fast generation, good for testing</li>
<li><strong>15-20 steps</strong>: Balanced quality and speed</li>
<li><strong>20-30 steps</strong>: High quality, longer processing time</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #f3e5f5, #e1bee7); border: 2px solid #9c27b0; border-radius: 15px; padding: 25px;">
<h4 style="color: #7b1fa2; margin-top: 0;">🎯 CFG Settings</h4>
<ul style="color: #7b1fa2; margin: 0;">
<li><strong>4-6</strong>: More creative, less adherence to prompt</li>
<li><strong>6-8</strong>: Balanced guidance (recommended)</li>
<li><strong>8-12</strong>: Strong prompt adherence</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); border: 2px solid #4caf50; border-radius: 15px; padding: 25px;">
<h4 style="color: #388e3c; margin-top: 0;">📐 Resolution Options</h4>
<ul style="color: #388e3c; margin: 0;">
<li><strong>512x512</strong>: Square format, fast generation</li>
<li><strong>832x480</strong>: Widescreen, cinematic feel</li>
<li><strong>Custom</strong>: Adjust based on your needs</li>
</ul>
</div>

</div>

---

## 🎪 Application Scenarios

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255, 154, 158, 0.3);">
<h3>🎬 Content Creation</h3>
<p>Social media videos, marketing content, storytelling</p>
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(168, 237, 234, 0.3);">
<h3>🎨 Artistic Expression</h3>
<p>Digital art, creative projects, visual experiments</p>
</div>

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255, 236, 210, 0.3);">
<h3>📚 Educational Content</h3>
<p>Learning materials, demonstrations, tutorials</p>
</div>

<div style="background: linear-gradient(135deg, #a8e6cf 0%, #dcedc1 100%); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(168, 230, 207, 0.3);">
<h3>🚀 Prototyping</h3>
<p>Concept visualization, storyboarding, idea development</p>
</div>

</div>

---

## 📚 Resources & Documentation

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 30px; margin: 30px 0; color: white; text-align: center;">

### 🔗 Official Documentation Links

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: rgba(255, 255, 255, 0.2); border-radius: 12px; padding: 20px;">
<h4 style="margin: 0 0 15px 0;">📖 ComfyUI Official Docs</h4>
<a href="https://comfyui-wiki.com/zh/interface/node-options" style="color: #fff; text-decoration: none; font-weight: bold;">View Detailed Guide →</a>
</div>

<div style="background: rgba(255, 255, 255, 0.2); border-radius: 12px; padding: 20px;">
<h4 style="margin: 0 0 15px 0;">🎥 WanVideo Plugin Docs</h4>
<a href="https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md" style="color: #fff; text-decoration: none; font-weight: bold;">GitHub Repository →</a>
</div>

</div>

</div>

---

<div style="text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 25px; color: white; margin: 40px 0; box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);">

## 🎉 Start Your Video Creation Journey!

**Transform your ideas into stunning videos with Wan2.1-T2V-14B**

*From text to video, just one step away*

<div style="margin-top: 30px; font-size: 18px; opacity: 0.9;">
✨ Unlimited Creativity | 🚀 Lightning Fast | 🎯 Precise Control | 🌟 Professional Quality
</div>

</div>
