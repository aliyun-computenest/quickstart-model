<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 40px; box-shadow: 0 15px 40px rgba(0,0,0,0.3); position: relative; overflow: hidden;">
  <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%); animation: pulse 4s ease-in-out infinite;"></div>
  <h1 style="font-size: 3.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); position: relative; z-index: 1;">🎬 Wan2.1-I2V-14B 模型使用指南</h1>
  <p style="font-size: 1.4em; margin: 20px 0 0 0; opacity: 0.95; position: relative; z-index: 1;">强大的图像到视频生成模型，让静态图片动起来！</p>
  <div style="margin-top: 30px; position: relative; z-index: 1;">
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; margin: 0 10px; font-weight: bold;">🚀 14B参数</span>
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; margin: 0 10px; font-weight: bold;">🎯 高质量</span>
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; margin: 0 10px; font-weight: bold;">⚡ 快速生成</span>
  </div>
</div>

---

## 📋 模型简介

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 30px; border-radius: 15px; border-left: 6px solid #2196f3; margin: 25px 0; box-shadow: 0 8px 25px rgba(33, 150, 243, 0.15);">
  <h3 style="color: #1976d2; margin-top: 0; font-size: 1.5em;">🎯 什么是 Wan2.1-I2V-14B？</h3>
  <p style="font-size: 1.1em; line-height: 1.6; margin-bottom: 0;">
    <strong>Wan2.1-I2V-14B</strong> 是一个革命性的图像到视频生成模型，拥有140亿参数的强大架构。它能够基于输入图像和文本提示生成高质量的视频内容，在保持输入图像主体特征的同时，根据文本描述添加逼真的动态效果和场景变化。
  </p>
</div>

### ✨ 核心特性展示

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 2.5em; margin-bottom: 15px;">🧠</div>
  <h3 style="margin: 0 0 10px 0;">参数规模</h3>
  <p style="margin: 0; opacity: 0.9;">14B参数，提供强大的图像理解和视频生成能力</p>
</div>

<div style="background: linear-gradient(135deg, #4facfe, #00f2fe); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 20px rgba(79, 172, 254, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 2.5em; margin-bottom: 15px;">🖼️</div>
  <h3 style="margin: 0 0 10px 0;">图像驱动</h3>
  <p style="margin: 0; opacity: 0.9;">以输入图像为基础，生成连贯的视频序列</p>
</div>

<div style="background: linear-gradient(135deg, #43e97b, #38f9d7); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 20px rgba(67, 233, 123, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 2.5em; margin-bottom: 15px;">🌍</div>
  <h3 style="margin: 0 0 10px 0;">多语言支持</h3>
  <p style="margin: 0; opacity: 0.9;">支持中文和英文文本提示</p>
</div>

<div style="background: linear-gradient(135deg, #fa709a, #fee140); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 20px rgba(250, 112, 154, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 2.5em; margin-bottom: 15px;">🎯</div>
  <h3 style="margin: 0 0 10px 0;">图像一致性</h3>
  <p style="margin: 0; opacity: 0.9;">保持输入图像的主要特征和风格</p>
</div>

</div>

### 🔧 技术规格

<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #2196f3;">
  <h4 style="color: #1976d2; margin: 0 0 10px 0;">📊 基础参数</h4>
  <p><strong>模型类型:</strong> 图像到视频生成（I2V）</p>
  <p><strong>量化方式:</strong> FP8量化版本</p>
  <p style="margin-bottom: 0;"><strong>参数规模:</strong> 14B</p>
</div>

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #4caf50;">
  <h4 style="color: #388e3c; margin: 0 0 10px 0;">🎥 视频规格</h4>
  <p><strong>支持分辨率:</strong> 480p</p>
  <p><strong>最大帧数:</strong> 81帧</p>
  <p style="margin-bottom: 0;"><strong>推荐帧率:</strong> 16fps</p>
</div>

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #ff9800;">
  <h4 style="color: #f57c00; margin: 0 0 10px 0;">📁 格式支持</h4>
  <p><strong>输入格式:</strong> JPEG、PNG、WebP</p>
  <p><strong>输出格式:</strong> MP4 (H.264)</p>
  <p style="margin-bottom: 0;"><strong>色彩空间:</strong> YUV420P</p>
</div>

</div>

</div>

---

## 🚀 使用说明

### 🌐 Web UI 使用教程

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); padding: 25px; border-radius: 15px; border-left: 6px solid #4CAF50; margin: 25px 0; box-shadow: 0 8px 25px rgba(76, 175, 80, 0.15);">

#### 📍 步骤一：访问界面

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin: 0; font-size: 1.1em;">单击服务实例处的访问链接</p>

  <div style="text-align: center; margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 10px;">
    <img src="img.png" alt="访问界面示例" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
    <p style="margin-top: 15px; color: #666; font-style: italic; font-size: 0.95em;">点击访问链接进入 ComfyUI 界面</p>
  </div>
</div>

#### 🔧 步骤二：选择工作流

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin: 0 0 10px 0; font-size: 1.1em;">选择 <code style="background: #e3f2fd; padding: 4px 8px; border-radius: 4px; color: #1976d2;">wanx-21.json</code> 工作流并打开</p>
  <p style="margin: 0; color: #666;">选择图生视频功能选项</p>
</div>

#### 📤 步骤三：上传图像

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <ul style="margin: 0; padding-left: 20px;">
    <li style="margin-bottom: 8px;">在 <strong>LoadImage</strong> 节点选择示例图片</li>
    <li style="margin-bottom: 0;">或从本机电脑上传自定义图像</li>
  </ul>

  <div style="text-align: center; margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 10px;">
    <img src="app3.png" alt="上传图像界面" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
    <p style="margin-top: 15px; color: #666; font-style: italic; font-size: 0.95em;">LoadImage 节点操作界面</p>
  </div>
</div>

#### ✍️ 步骤四：设置文本描述

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin: 0 0 15px 0; font-size: 1.1em;">在 <strong>TextEncode</strong> 节点填写描述词：</p>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
    <div style="background: #e8f5e8; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
      <h5 style="margin: 0 0 8px 0; color: #2e7d32;">✅ 上方输入框</h5>
      <p style="margin: 0; font-size: 0.95em;">描述希望的动作和场景变化</p>
    </div>
    <div style="background: #ffebee; padding: 15px; border-radius: 8px; border-left: 4px solid #f44336;">
      <h5 style="margin: 0 0 8px 0; color: #c62828;">❌ 下方输入框</h5>
      <p style="margin: 0; font-size: 0.95em;">不想要生成的内容</p>
    </div>
  </div>
</div>

#### ⚙️ 步骤五：配置参数

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin: 0; font-size: 1.1em;">在 <strong>ImageClip Encode</strong> 设置分辨率和帧数</p>
</div>

#### 🎬 步骤六：执行工作流

<div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin: 0; font-size: 1.1em;">点击执行按钮开始生成</p>
</div>

</div>

### 🔌 API 调用方式

#### 🔑 获取认证信息

<div style="background: linear-gradient(135deg, #fff3cd, #ffeaa7); padding: 25px; border-radius: 15px; border: 2px solid #ffc107; margin: 25px 0; box-shadow: 0 8px 25px rgba(255, 193, 7, 0.2);">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <h4 style="color: #f57c00; margin: 0 0 15px 0;">🔐 获取 Token</h4>
  <p style="margin: 0 0 15px 0;">点击右上方按钮，打开底部面板</p>

  <div style="text-align: center; padding: 15px; background: #f8f9fa; border-radius: 8px;">
    <img src="img_1.png" alt="获取Token界面" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  </div>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <h4 style="color: #f57c00; margin: 0 0 15px 0;">🌐 获取服务器地址</h4>
  <p style="margin: 0 0 15px 0;">COMFYUI_SERVER 的获取参考</p>

  <div style="text-align: center; padding: 15px; background: #f8f9fa; border-radius: 8px;">
    <img src="img_2.png" alt="获取服务器地址" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  </div>
</div>

</div>

</div>

#### 💻 Python 代码示例

<details style="border: 3px solid #2196F3; border-radius: 15px; padding: 0; margin: 30px 0; background: linear-gradient(145deg, #f0f8ff, #e6f3ff); box-shadow: 0 8px 25px rgba(33, 150, 243, 0.2); overflow: hidden;">
<summary style="font-weight: bold; font-size: 1.3em; color: white; cursor: pointer; padding: 25px; background: linear-gradient(135deg, #2196F3, #1976D2); margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; gap: 15px;">
  <span style="font-size: 1.5em;">🐍</span>
  <span>点击展开完整 Python 代码实现</span>
  <span style="margin-left: auto; font-size: 1.2em;">⬇️</span>
</summary>

<div style="padding: 30px; background: white; margin: 0;">

```python
import requests, json, uuid, time, random, os

# 🔧 配置参数
COMFYUI_SERVER, COMFYUI_TOKEN = "输入您的服务器地址", "输入您的token"
T5_MODEL = "wan2.1/umt5-xxl-enc-bf16.safetensors"
VIDEO_MODEL = "Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors"
VAE_MODEL = "wan2.1/Wan2_1_VAE_bf16.safetensors"
CLIP_MODEL = "wan2.1/open-clip-xlm-roberta-large-vit-huge-14_visual_fp16.safetensors"

# 🎯 预设参数
IMAGE_PATH = "girl.png"
PROMPT = "A beautiful anime girl with long flowing hair, graceful movements, smooth animation, cinematic lighting, high quality"
NEG_PROMPT = "bad quality video, low quality, blurry, distorted, choppy animation, static, bad anatomy"

class ComfyUIClient:
   def __init__(self, server=COMFYUI_SERVER, token=COMFYUI_TOKEN):
      self.base_url, self.token, self.client_id = f"http://{server}", token, str(uuid.uuid4())
      self.headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})}

   def upload_image(self, image_path):
      """📤 上传图片到ComfyUI"""
      if not os.path.exists(image_path):
         raise Exception(f"图片文件不存在: {image_path}")

      try:
         with open(image_path, 'rb') as f:
            files = {'image': (os.path.basename(image_path), f, 'image/png')}
            headers = {}
            if self.token:
               headers["Authorization"] = f"Bearer {self.token}"

            response = requests.post(f"{self.base_url}/upload/image", files=files, headers=headers)
            print(f"Upload response: {response.text}")

            if response.status_code != 200:
               raise Exception(f"上传失败，状态码: {response.status_code}")

            result = response.json()
            if 'name' not in result:
               raise Exception(f"上传响应中没有文件名: {result}")

            return result['name']
      except Exception as e:
         raise Exception(f"图片上传失败: {e}")

   def generate_i2v(self, image_path, prompt, neg_prompt, steps=10, cfg=6, width=512, height=512, frames=81):
      """🎬 图生视频 - 修复clip_vision输入"""
      print("📤 正在上传图片...")
      image_name = self.upload_image(image_path)
      print(f"✅ 图片上传成功: {image_name}")

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

      print("📤 提交工作流...")
      response = requests.post(f"{self.base_url}/prompt", headers=self.headers, json={"prompt": workflow, "client_id": self.client_id})
      print(f"API Response: {response.text}")
      result = response.json()
      if "error" in result: raise Exception(f"Workflow error: {result['error']}")
      if "prompt_id" not in result: raise Exception(f"No prompt_id in response: {result}")
      return result["prompt_id"]

   def get_status(self, task_id):
      """📊 获取任务状态"""
      try:
         queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
         if any(item[1] == task_id for item in queue_data.get("queue_running", [])): return "processing"
         if any(item[1] == task_id for item in queue_data.get("queue_pending", [])): return "pending"
         history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
         return "completed" if history_response.status_code == 200 and task_id in history_response.json() else "processing"
      except: return "processing"

   def download_video(self, task_id, output_path="i2v_output.mp4"):
      """📥 下载生成的视频"""
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
   """🚀 主函数 - 执行图生视频任务"""
   client = ComfyUIClient()
   try:
      print(f"🎬 开始图生视频任务...")
      print(f"📷 输入图片: {IMAGE_PATH}")
      print(f"📝 提示词: {PROMPT}")

      if not os.path.exists(IMAGE_PATH):
         print(f"❌ 图片文件不存在: {IMAGE_PATH}")
         print("请确保当前目录下有 girl.png 文件")
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

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); padding: 20px; border-radius: 10px; margin-top: 20px; border-left: 4px solid #4caf50;">
  <h4 style="color: #2e7d32; margin: 0 0 10px 0;">💡 代码说明</h4>
  <ul style="margin: 0; color: #2e7d32;">
    <li>完整的 ComfyUI 客户端实现</li>
    <li>支持图片上传、工作流提交、状态监控</li>
    <li>自动下载生成的视频文件</li>
    <li>详细的错误处理和日志输出</li>
  </ul>
</div>

</div>

</details>

#### 🔗 ComfyUI API 端点说明

<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px; padding: 25px; margin: 25px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">

<div style="overflow-x: auto;">

| 端点 | 方法 | 功能 | 说明 | 示例 |
|------|------|------|------|------|
| 🔍 `/queue` | GET | 获取队列状态 | 查看当前任务队列和运行状态 | `GET /queue` |
| 🚀 `/prompt` | POST | 提交工作流 | 执行图生视频任务 | `POST /prompt` |
| 📊 `/history/{prompt_id}` | GET | 获取执行历史 | 查看任务执行结果和输出 | `GET /history/abc123` |
| 📤 `/upload/image` | POST | 上传图片 | 上传输入图片文件 | `POST /upload/image` |
| 📥 `/view` | GET | 下载输出文件 | 获取生成的结果文件 | `GET /view?filename=output.mp4` |

</div>

</div>

---

## ⚙️ 参数详细说明

### 🎛️ 生成参数配置

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 20px rgba(255, 154, 158, 0.3);">
  <h3 style="margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.5em;">🔢</span>
    核心参数
  </h3>
  <div style="space-y: 15px;">
    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
      <strong>steps</strong><br>
      <small>推理步数（建议20-30）</small>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
      <strong>cfg</strong><br>
      <small>CFG引导强度（建议6-8）</small>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px;">
      <strong>shift</strong><br>
      <small>噪声调度偏移（建议5）</small>
    </div>
  </div>
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; box-shadow: 0 8px 20px rgba(168, 237, 234, 0.3);">
  <h3 style="margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.5em;">🎲</span>
    随机性控制
  </h3>
  <div style="space-y: 15px;">
    <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
      <strong>seed</strong><br>
      <small>随机种子（控制生成结果的随机性）</small>
    </div>
    <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px;">
      <strong>denoise_strength</strong><br>
      <small>去噪强度（0.6-0.9，控制对原图的保持程度）</small>
    </div>
  </div>
</div>

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; color: #333; box-shadow: 0 8px 20px rgba(255, 236, 210, 0.3);">
  <h3 style="margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.5em;">📐</span>
    视频规格
  </h3>
  <div style="space-y: 15px;">
    <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
      <strong>width × height</strong><br>
      <small>视频分辨率（建议512×512）</small>
    </div>
    <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
      <strong>frames</strong><br>
      <small>视频帧数（最大81帧）</small>
    </div>
    <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px;">
      <strong>frame_rate</strong><br>
      <small>帧率（推荐16fps）</small>
    </div>
  </div>
</div>

</div>


### 🖼️ 图像要求详解

> **💡 提示：** 高质量的输入图像是生成优秀视频的关键！

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 30px; border-radius: 15px; border-left: 6px solid #2196f3; margin: 25px 0;">

**📐 分辨率要求**
- 建议512×512以上，确保图像清晰度

**📄 支持格式**
- JPEG、PNG、WebP等主流格式

**🎯 内容要求**
- 清晰的主体对象，避免过于复杂的背景

**✨ 质量标准**
- 高质量图像能获得更好的视频效果

</div>

---

## 💡 提示词编写指南

### ✅ 正向提示词示例

<div style="background: linear-gradient(135deg, #d4edda, #c3e6cb); padding: 25px; border-radius: 15px; border: 2px solid #28a745; margin: 25px 0; box-shadow: 0 8px 25px rgba(40, 167, 69, 0.2);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #28a745;">
  <h4 style="color: #155724; margin: 0 0 10px 0;">🚶 人物动作</h4>
  <p style="margin: 0; font-style: italic; color: #155724;">"The person in the image is walking slowly through a garden"</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #28a745;">
  <h4 style="color: #155724; margin: 0 0 10px 0;">🐱 动物行为</h4>
  <p style="margin: 0; font-style: italic; color: #155724;">"The cat in the photo is playing with a ball of yarn"</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #28a745;">
  <h4 style="color: #155724; margin: 0 0 10px 0;">🚗 交通工具</h4>
  <p style="margin: 0; font-style: italic; color: #155724;">"The car in the image is driving down a winding mountain road"</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #28a745;">
  <h4 style="color: #155724; margin: 0 0 10px 0;">💃 艺术表演</h4>
  <p style="margin: 0; font-style: italic; color: #155724;">"The dancer in the picture is performing elegant ballet movements"</p>
</div>

</div>

</div>

### ❌ 负向提示词建议

<div style="background: linear-gradient(135deg, #f8d7da, #f5c6cb); padding: 25px; border-radius: 15px; border: 2px solid #dc3545; margin: 25px 0; box-shadow: 0 8px 25px rgba(220, 53, 69, 0.2);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #dc3545;">
  <h4 style="color: #721c24; margin: 0 0 10px 0;">🚫 静态问题</h4>
  <p style="margin: 0; font-style: italic; color: #721c24;">"static, motionless, frozen, distorted, blurry"</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #dc3545;">
  <h4 style="color: #721c24; margin: 0 0 10px 0;">⚠️ 动作问题</h4>
  <p style="margin: 0; font-style: italic; color: #721c24;">"unnatural movement, jerky motion, inconsistent"</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #dc3545;">
  <h4 style="color: #721c24; margin: 0 0 10px 0;">📉 质量问题</h4>
  <p style="margin: 0; font-style: italic; color: #721c24;">"low quality, artifacts, noise, compression"</p>
</div>

</div>

</div>

---

## 🏆 最佳实践指南

### 📸 输入图像选择策略

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 20px; border-radius: 12px; border-left: 5px solid #2196F3; box-shadow: 0 6px 18px rgba(33, 150, 243, 0.15);">
  <h4 style="color: #1976d2; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.3em;">🔍</span> 清晰度优先
  </h4>
  <p style="margin: 0; color: #1976d2;">选择高清晰度的图像，避免模糊或噪点过多的图片</p>
</div>

<div style="background: linear-gradient(135deg, #f3e5f5, #e1bee7); padding: 20px; border-radius: 12px; border-left: 5px solid #9c27b0; box-shadow: 0 6px 18px rgba(156, 39, 176, 0.15);">
  <h4 style="color: #7b1fa2; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.3em;">🎯</span> 主体明确
  </h4>
  <p style="margin: 0; color: #7b1fa2;">确保主要对象清晰可见，占据画面合适比例</p>
</div>

<div style="background: linear-gradient(135deg, #e8f5e8, #c8e6c9); padding: 20px; border-radius: 12px; border-left: 5px solid #4caf50; box-shadow: 0 6px 18px rgba(76, 175, 80, 0.15);">
  <h4 style="color: #388e3c; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.3em;">🖼️</span> 构图合理
  </h4>
  <p style="margin: 0; color: #388e3c;">避免过于复杂的背景，保持构图简洁明了</p>
</div>

<div style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); padding: 20px; border-radius: 12px; border-left: 5px solid #ff9800; box-shadow: 0 6px 18px rgba(255, 152, 0, 0.15);">
  <h4 style="color: #f57c00; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.3em;">💡</span> 光照良好
  </h4>
  <p style="margin: 0; color: #f57c00;">光照均匀的图像效果更佳，避免过暗或过曝</p>
</div>

</div>

### ✍️ 提示词编写技巧

<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #4caf50;">
  <h4 style="color: #2e7d32; margin: 0 0 15px 0;">📝 具体描述</h4>
  <p style="margin: 0; color: #666; line-height: 1.6;">详细描述希望的动作和场景，越具体越好</p>
</div>

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #2196f3;">
  <h4 style="color: #1976d2; margin: 0 0 15px 0;">🔄 保持一致</h4>
  <p style="margin: 0; color: #666; line-height: 1.6;">确保描述与图像内容相符，避免矛盾</p>
</div>

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #ff9800;">
  <h4 style="color: #f57c00; margin: 0 0 15px 0;">⚖️ 动作合理</h4>
  <p style="margin: 0; color: #666; line-height: 1.6;">描述符合物理规律的动作，避免不可能的运动</p>
</div>

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #9c27b0;">
  <h4 style="color: #7b1fa2; margin: 0 0 15px 0;">🎨 风格统一</h4>
  <p style="margin: 0; color: #666; line-height: 1.6;">保持与原图风格一致的描述</p>
</div>

</div>

</div>

### 🔧 参数调优策略

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 25px 0; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 10px; backdrop-filter: blur(10px);">
  <h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">🎨</span> 去噪强度调节
  </h4>
  <div style="margin-bottom: 10px;">
    <strong>0.6-0.7:</strong> 保持原图特征较多
  </div>
  <div>
    <strong>0.8-0.9:</strong> 允许更多变化和动态效果
  </div>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 10px; backdrop-filter: blur(10px);">
  <h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">🎯</span> CFG值设置
  </h4>
  <div style="margin-bottom: 10px;">
    <strong>6-7:</strong> 平衡的引导强度
  </div>
  <div>
    <strong>8-10:</strong> 更强的文本引导
  </div>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 10px; backdrop-filter: blur(10px);">
  <h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">⏱️</span> 步数选择
  </h4>
  <div style="margin-bottom: 10px;">
    <strong>20-25:</strong> 快速生成
  </div>
  <div>
    <strong>25-30:</strong> 更高质量
  </div>
</div>

</div>

</div>

---

## ⚠️ 重要注意事项

<div style="background: linear-gradient(135deg, #fff3cd, #ffeaa7); padding: 30px; border-radius: 15px; border: 2px solid #ffc107; margin: 30px 0; box-shadow: 0 10px 30px rgba(255, 193, 7, 0.2);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #ff9800;">
  <h4 style="color: #f57c00; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span>💾</span> 内存管理
  </h4>
  <p style="margin: 0; color: #666;">图生视频比文生视频需要更多显存，建议关闭其他占用显存的程序</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #2196f3;">
  <h4 style="color: #1976d2; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span>🔧</span> 图像预处理
  </h4>
  <p style="margin: 0; color: #666;">确保输入图像尺寸合适，避免过大或过小的图片</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #4caf50;">
  <h4 style="color: #388e3c; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎯</span> 一致性保持
  </h4>
  <p style="margin: 0; color: #666;">去噪强度不宜过高，以保持图像一致性</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #9c27b0;">
  <h4 style="color: #7b1fa2; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span>🎭</span> 动作合理性
  </h4>
  <p style="margin: 0; color: #666;">描述的动作应符合图像中对象的特征</p>
</div>

<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #f44336;">
  <h4 style="color: #d32f2f; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
    <span>⚡</span> 批处理建议
  </h4>
  <p style="margin: 0; color: #666;">建议单次处理一个任务，避免内存溢出</p>
</div>

</div>

</div>

---

## 🎯 应用场景展示

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 30px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 10px 25px rgba(255, 154, 158, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 3em; margin-bottom: 15px;">👤</div>
  <h3 style="margin: 0 0 15px 0;">人物动画</h3>
  <p style="margin: 0; opacity: 0.9; line-height: 1.5;">让静态人物照片动起来，创造生动的人物视频</p>
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; text-align: center; color: #333; box-shadow: 0 10px 25px rgba(168, 237, 234, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 3em; margin-bottom: 15px;">🛍️</div>
  <h3 style="margin: 0 0 15px 0;">产品展示</h3>
  <p style="margin: 0; opacity: 0.8; line-height: 1.5;">为产品图片添加动态效果，提升营销效果</p>
</div>

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 30px; border-radius: 15px; text-align: center; color: #333; box-shadow: 0 10px 25px rgba(255, 236, 210, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 3em; margin-bottom: 15px;">🎨</div>
  <h3 style="margin: 0 0 15px 0;">艺术创作</h3>
  <p style="margin: 0; opacity: 0.8; line-height: 1.5;">将绘画作品转换为动态视频，增强艺术表现力</p>
</div>

<div style="background: linear-gradient(135deg, #a8e6cf 0%, #dcedc1 100%); padding: 30px; border-radius: 15px; text-align: center; color: #333; box-shadow: 0 10px 25px rgba(168, 230, 207, 0.3); transform: translateY(0); transition: transform 0.3s ease;">
  <div style="font-size: 3em; margin-bottom: 15px;">📚</div>
  <h3 style="margin: 0 0 15px 0;">教育演示</h3>
  <p style="margin: 0; opacity: 0.8; line-height: 1.5;">让教学图片具有动态效果，提升学习体验</p>
</div>

</div>

---

## 📚 相关资源链接

<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px; padding: 30px; margin: 30px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #2196f3;">
  <h4 style="color: #1976d2; margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">📖</span> ComfyUI 官方文档
  </h4>
  <p style="margin: 0 0 15px 0; color: #666;">详细的 ComfyUI 使用说明和节点介绍</p>
  <a href="https://comfyui-wiki.com/zh/interface/node-options" style="color: #2196f3; text-decoration: none; font-weight: bold;">访问文档 →</a>
</div>

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #4caf50;">
  <h4 style="color: #388e3c; margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">🎥</span> WanVideo 插件文档
  </h4>
  <p style="margin: 0 0 15px 0; color: #666;">WanVideo 插件的详细使用说明</p>
  <a href="https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md" style="color: #4caf50; text-decoration: none; font-weight: bold;">查看 GitHub →</a>
</div>

<div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #ff9800;">
  <h4 style="color: #f57c00; margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 1.3em;">🔧</span> ComfyUI 技术文档
  </h4>
  <p style="margin: 0 0 15px 0; color: #666;">图像预处理和高级功能说明</p>
  <a href="https://docs.comfy.org/essentials/image_preprocessing" style="color: #ff9800; text-decoration: none; font-weight: bold;">技术文档 →</a>
</div>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin: 40px 0; position: relative; overflow: hidden; box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);">
  <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%); animation: pulse 4s ease-in-out infinite;"></div>

  <div style="position: relative; z-index: 1;">
    <div style="font-size: 4em; margin-bottom: 20px;">🎉</div>
    <h2 style="font-size: 2.5em; margin: 0 0 20px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">开始您的创作之旅！</h2>
    <p style="font-size: 1.3em; margin: 0 0 30px 0; opacity: 0.95; line-height: 1.5;">
      <strong>Wan2.1-I2V-14B</strong> 让您的静态图片焕发生机，创造无限可能！
    </p>
<div style="text-align: center; margin-top: 30px;">
  <span style="background: rgba(255,255,255,0.2); padding: 12px 24px; border-radius: 25px; font-weight: bold; margin: 0 10px; display: inline-block;">🚀 即刻开始</span>
  <span style="background: rgba(255,255,255,0.2); padding: 12px 24px; border-radius: 25px; font-weight: bold; margin: 0 10px; display: inline-block;">🎨 释放创意</span>
  <span style="background: rgba(255,255,255,0.2); padding: 12px 24px; border-radius: 25px; font-weight: bold; margin: 0 10px; display: inline-block;">✨ 精彩无限</span>
</div>


  </div>
</div>


