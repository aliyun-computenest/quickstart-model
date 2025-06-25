<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="font-size: 2.5em; margin: 0; font-weight: 600;">🎬 Wan2.1-I2V-14B 模型使用指南</h1>
  <p style="font-size: 1.2em; margin: 16px 0 0 0; opacity: 0.9;">强大的图像到视频生成模型，让静态图片动起来</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🚀 14B参数</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 高质量</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">⚡ 快速生成</span>
  </div>
</div>

## 📋 模型简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Wan2.1-I2V-14B** 是一个革命性的图像到视频生成模型，拥有140亿参数的强大架构。它能够基于输入图像和文本提示生成高质量的视频内容，在保持输入图像主体特征的同时，根据文本描述添加逼真的动态效果和场景变化。

</div>

## ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #1e40af; margin: 0 0 8px 0;">🧠 强大参数规模</h4>
<p style="margin: 0; color: #1e40af;">14B参数，提供强大的图像理解和视频生成能力</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🖼️ 图像驱动生成</h4>
<p style="margin: 0; color: #065f46;">以输入图像为基础，生成连贯的视频序列</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🌍 多语言支持</h4>
<p style="margin: 0; color: #9a3412;">支持中文和英文文本提示</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🎯 图像一致性</h4>
<p style="margin: 0; color: #5b21b6;">保持输入图像的主要特征和风格</p>
</div>

</div>

## 🔧 技术规格

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">规格项目</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">详细信息</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">模型类型</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">图像到视频生成（I2V）</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">参数规模</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">14B</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">量化方式</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">FP8量化版本</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">支持分辨率</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">480p</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">最大帧数</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">81帧</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">推荐帧率</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16fps</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">输入格式</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">JPEG、PNG、WebP</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">输出格式</td>
      <td style="padding: 12px;">MP4 (H.264)</td>
    </tr>
  </tbody>
</table>
</div>

---

# 🚀 使用说明

## 🌐 Web UI 使用教程

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 步骤一：访问界面

单击服务实例处的访问链接

<div style="text-align: center; margin: 16px 0;">
  <img src="img.png" alt="访问界面示例" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">点击访问链接进入 ComfyUI 界面</p>
</div>

### 🔧 步骤二：选择工作流

选择 `wanx-21.json` 工作流并打开，选择图生视频功能选项

### 📤 步骤三：上传图像

- 在 **LoadImage** 节点选择示例图片
- 或从本机电脑上传自定义图像

<div style="text-align: center; margin: 16px 0;">
  <img src="app3.png" alt="上传图像界面" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">LoadImage 节点操作界面</p>
</div>

### ✍️ 步骤四：设置文本描述

在 **TextEncode** 节点填写描述词：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 正向提示词</h4>
<p style="margin: 0; color: #065f46;">描述希望的动作和场景变化</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">❌ 负向提示词</h4>
<p style="margin: 0; color: #9a3412;">不想要生成的内容</p>
</div>

</div>

### ⚙️ 步骤五：配置参数

在 **ImageClip Encode** 设置分辨率和帧数

### 🎬 步骤六：执行工作流

点击执行按钮开始生成

</div>

---

## 🔌 API 调用方式

### 🔑 获取认证信息

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🔐 获取 Token</h4>
<p style="margin: 0 0 12px 0;">点击右上方按钮，打开底部面板</p>
<div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 6px;">
  <img src="img_1.png" alt="获取Token界面" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
</div>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🌐 获取服务器地址</h4>
<p style="margin: 0 0 12px 0;">COMFYUI_SERVER 的获取参考</p>
<div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 6px;">
  <img src="img_2.png" alt="获取服务器地址" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
</div>
</div>

</div>

### 💻 Python 代码示例

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 点击展开完整 Python 代码实现
</summary>

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
        """🎬 图生视频生成"""
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
        if "error" in result: 
            raise Exception(f"Workflow error: {result['error']}")
        if "prompt_id" not in result: 
            raise Exception(f"No prompt_id in response: {result}")
        return result["prompt_id"]

    def get_status(self, task_id):
        """📊 获取任务状态"""
        try:
            queue_data = requests.get(f"{self.base_url}/queue", headers=self.headers).json()
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])): 
                return "processing"
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])): 
                return "pending"
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            return "completed" if history_response.status_code == 200 and task_id in history_response.json() else "processing"
        except: 
            return "processing"

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
                        with open(output_path, "wb") as f: 
                            f.write(video_response.content)
                        return output_path
        except Exception as e: 
            print(f"Download error: {e}")
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
            if status == "completed": 
                print("✅ Video ready!"); 
                break
            elif status == "failed": 
                print("❌ Generation failed!"); 
                exit(1)
            time.sleep(10)

        output_file = client.download_video(task_id, "i2v_output.mp4")
        print("🎉 Video downloaded successfully!" if output_file else "❌ Failed to download video")
        if output_file: 
            print(f"📁 Saved as: {output_file}")

    except Exception as e: 
        print(f"❌ Error: {e}")

if __name__ == "__main__": 
    main()
```

</details>

### 🔗 ComfyUI API 端点说明

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">端点</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">方法</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">功能</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">/queue</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">GET</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">获取队列状态</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">查看当前任务队列和运行状态</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">/prompt</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">POST</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">提交工作流</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">执行图生视频任务</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">/history/{prompt_id}</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">GET</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">获取执行历史</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">查看任务执行结果和输出</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">/upload/image</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">POST</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">上传图片</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">上传输入图片文件</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-family: monospace; background: #f8fafc;">/view</td>
      <td style="padding: 12px;">GET</td>
      <td style="padding: 12px;">下载输出文件</td>
      <td style="padding: 12px;">获取生成的结果文件</td>
    </tr>
  </tbody>
</table>
</div>

---

# ⚙️ 参数详细说明

## 🎛️ 生成参数配置

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #1e40af; margin: 0 0 8px 0;">🔢 核心参数</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af;">
  <li><strong>steps</strong>: 推理步数（建议20-30）</li>
  <li><strong>cfg</strong>: CFG引导强度（建议6-8）</li>
  <li><strong>shift</strong>: 噪声调度偏移（建议5）</li>
</ul>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎲 随机性控制</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>seed</strong>: 随机种子（控制生成结果的随机性）</li>
  <li><strong>denoise_strength</strong>: 去噪强度（0.6-0.9，控制对原图的保持程度）</li>
</ul>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">📐 视频规格</h4>
<ul style="margin: 0; padding-left: 20px; color: #5b21b6;">
  <li><strong>width × height</strong>: 视频分辨率（建议512×512）</li>
  <li><strong>frames</strong>: 视频帧数（最大81帧）</li>
  <li><strong>frame_rate</strong>: 帧率（推荐16fps）</li>
</ul>
</div>

</div>

## 🖼️ 图像要求详解

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 图像输入要求</strong><br>
  <strong>分辨率要求</strong>: 建议512×512以上，确保图像清晰度<br>
  <strong>支持格式</strong>: JPEG、PNG、WebP等主流格式<br>
  <strong>内容要求</strong>: 清晰的主体对象，避免过于复杂的背景<br>
  <strong>质量标准</strong>: 高质量图像能获得更好的视频效果
</div>

---

# 💡 提示词编写指南

## ✅ 正向提示词示例

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🚶 人物动作</h4>
<p style="margin: 0; font-style: italic; color: #065f46;">"The person in the image is walking slowly through a garden"</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🐱 动物行为</h4>
<p style="margin: 0; font-style: italic; color: #065f46;">"The cat in the photo is playing with a ball of yarn"</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🚗 交通工具</h4>
<p style="margin: 0; font-style: italic; color: #065f46;">"The car in the image is driving down a winding mountain road"</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">💃 艺术表演</h4>
<p style="margin: 0; font-style: italic; color: #065f46;">"The dancer in the picture is performing elegant ballet movements"</p>
</div>

</div>

## ❌ 负向提示词建议

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🚫 静态问题</h4>
<p style="margin: 0; font-style: italic; color: #9a3412;">"static, motionless, frozen, distorted, blurry"</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">⚠️ 动作问题</h4>
<p style="margin: 0; font-style: italic; color: #9a3412;">"unnatural movement, jerky motion, inconsistent"</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">📉 质量问题</h4>
<p style="margin: 0; font-style: italic; color: #9a3412;">"low quality, artifacts, noise, compression"</p>
</div>

</div>

---

# 🏆 最佳实践指南

## 📸 输入图像选择策略

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #1e40af; margin: 0 0 8px 0;">🔍 清晰度优先</h4>
<p style="margin: 0; color: #1e40af;">选择高清晰度的图像，避免模糊或噪点过多的图片</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎯 主体明确</h4>
<p style="margin: 0; color: #065f46;">确保主要对象清晰可见，占据画面合适比例</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🖼️ 构图合理</h4>
<p style="margin: 0; color: #9a3412;">避免过于复杂的背景，保持构图简洁明了</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">💡 光照良好</h4>
<p style="margin: 0; color: #5b21b6;">光照均匀的图像效果更佳，避免过暗或过曝</p>
</div>

</div>

## ✍️ 提示词编写技巧

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📝 编写要点</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>具体描述</strong>: 详细描述希望的动作和场景，越具体越好</li>
  <li><strong>保持一致</strong>: 确保描述与图像内容相符，避免矛盾</li>
  <li><strong>动作合理</strong>: 描述符合物理规律的动作，避免不可能的运动</li>
  <li><strong>风格统一</strong>: 保持与原图风格一致的描述</li>
</ul>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">⚙️ 参数调优策略</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af;">
  <li><strong>去噪强度</strong>: 0.6-0.7保持原图特征，0.8-0.9允许更多变化</li>
  <li><strong>CFG值设置</strong>: 6-7平衡引导，8-10更强文本引导</li>
  <li><strong>步数选择</strong>: 20-25快速生成，25-30更高质量</li>
</ul>
</div>

</div>

---

# ⚠️ 重要注意事项

<details style="border: 2px solid #ea580c; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #fff7ed, #fed7aa); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #ea580c; cursor: pointer;">💾 内存管理注意事项</summary>
<div style="margin-top: 15px; color: #9a3412;">
<p><strong>重要提醒：</strong></p>
<ul>
<li>图生视频比文生视频需要更多显存，建议关闭其他占用显存的程序</li>
<li>确保输入图像尺寸合适，避免过大或过小的图片</li>
<li>去噪强度不宜过高，以保持图像一致性</li>
<li>描述的动作应符合图像中对象的特征</li>
</ul>
</div>
</details>

---

# 🎯 应用场景展示

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #2563eb;">👤</div>
<h4 style="margin: 0 0 8px 0; color: #1e40af;">人物动画</h4>
<p style="margin: 0; color: #1e40af;">让静态人物照片动起来，创造生动的人物视频</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #059669;">🛍️</div>
<h4 style="margin: 0 0 8px 0; color: #059669;">产品展示</h4>
<p style="margin: 0; color: #065f46;">为产品图片添加动态效果，提升营销效果</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #ea580c;">🎨</div>
<h4 style="margin: 0 0 8px 0; color: #ea580c;">艺术创作</h4>
<p style="margin: 0; color: #9a3412;">将绘画作品转换为动态视频，增强艺术表现力</p>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px; text-align: center;">
<div style="font-size: 2.5em; margin-bottom: 12px; color: #7c3aed;">📚</div>
<h4 style="margin: 0 0 8px 0; color: #7c3aed;">教育演示</h4>
<p style="margin: 0; color: #5b21b6;">让教学图片具有动态效果，提升学习体验</p>
</div>

</div>

---

# 📚 相关资源链接

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">📖 ComfyUI 官方文档</h4>
<a href="https://comfyui-wiki.com/zh/interface/node-options" style="color: #2563eb; text-decoration: none; font-weight: 500;">ComfyUI 使用指南 →</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">详细的 ComfyUI 使用说明和节点介绍</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">🎥 WanVideo 插件文档</h4>
<a href="https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/readme.md" style="color: #2563eb; text-decoration: none; font-weight: 500;">GitHub 项目页面 →</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">WanVideo 插件的详细使用说明</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">🔧 ComfyUI 技术文档</h4>
<a href="https://docs.comfy.org/essentials/image_preprocessing" style="color: #2563eb; text-decoration: none; font-weight: 500;">图像预处理指南 →</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">图像预处理和高级功能说明</p>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎬 <strong>开始您的创作之旅！</strong> | Wan2.1-I2V-14B 让您的静态图片焕发生机，创造无限可能
  </p>
</div>