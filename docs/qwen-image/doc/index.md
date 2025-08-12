<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎨 Qwen-Image</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Qwen 系列图像生成基础模型 - 专精复杂文本渲染与精确图像编辑</p>
  <div style="margin-top: 20px;">
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🎯 文本渲染</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">✨ 图像编辑</span>
    <span style="background: rgba(255,255,255,0.2); color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; margin: 0 8px;">🧠 智能理解</span>
  </div>
</div>

## 🌟 模型简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

我们非常激动地发布了 **Qwen-Image**，这是 Qwen 系列中的一个图像生成基础模型，在 **复杂文本渲染** 和 **精确图像编辑** 方面取得了显著进展。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 核心优势</strong><br>
  实验显示，该模型在图像生成和编辑方面具有强大的通用能力，尤其是在文本渲染方面表现尤为出色，特别是对于中文。
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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">文本到图像生成（T2I）</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">架构</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Diffusion Transformer</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">支持分辨率</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">多种宽高比（1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3）</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">最大分辨率</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">1664×928</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">推理步数</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">推荐 50 步</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">CFG 引导</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">true_cfg_scale: 4.0</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">许可协议</td>
      <td style="padding: 12px;">Apache 2.0</td>
    </tr>
  </tbody>
</table>
</div>

---

# 🚀 快速开始
---

# 🎨 ComfyUI 使用指南

## 🌐 ComfyUI Web 界面使用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 步骤一：访问界面
![img.png](img.png)
通过服务实例的访问链接进入 ComfyUI 界面

### 🔧 步骤二：加载工作流

选择 Qwen-Image 专用工作流模板，并去掉Lora节点配置
![img_4.png](img_4.png)

### ✍️ 步骤三：设置提示词


在 **TextEncode** 节点填写描述词：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✅ 正向提示词</h4>
<p style="margin: 0; color: #065f46;">描述希望生成的图像内容和风格</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">❌ 负向提示词</h4>
<p style="margin: 0; color: #9a3412;">不想要生成的内容</p>
</div>

</div>

### ⚙️ 步骤四：配置参数

设置图像分辨率、推理步数等参数

### 🎬 步骤五：执行生成

点击执行按钮开始生成图像

</div>

---

## 🔌 API 调用方式

## 🔑 获取认证信息



<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🌐 获取服务器地址</h4>
<p style="margin: 0 0 12px 0;">记录 ComfyUI 服务器的访问地址</p>

![img_2.png](img_2.png)
</div>
<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🔐 获取 API Token</h4>
<p style="margin: 0 0 12px 0;">在 ComfyUI 界面右上角获取访问令牌</p>

![img_1.png](img_1.png)
</div>



</div>

## 💻 Python API 调用示例

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 点击展开完整 Python API 调用代码
</summary>

```python
import requests
import json
import uuid
import time
import random
import os

# 🔧 配置参数
COMFYUI_SERVER = "your-server-address"
COMFYUI_TOKEN = "your-api-token"

# 🎯 Qwen-Image 模型文件名
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
        """🎨 生成图像"""
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

        print("📤 提交 Qwen-Image 生成任务...")
        response = requests.post(
            f"{self.base_url}/prompt",
            headers=self.headers,
            json={"prompt": workflow, "client_id": self.client_id}
        )
        
        print(f"API Response: {response.text}")
        result = response.json()
        if "error" in result:
            raise Exception(f"工作流错误: {result['error']}")
        if "prompt_id" not in result:
            raise Exception(f"响应中没有 prompt_id: {result}")
        
        return result["prompt_id"]

    def get_status(self, task_id):
        """📊 获取任务状态"""
        try:
            # 检查队列状态
            queue_response = requests.get(f"{self.base_url}/queue", headers=self.headers)
            queue_data = queue_response.json()
            
            # 检查是否在运行队列中
            if any(item[1] == task_id for item in queue_data.get("queue_running", [])):
                return "processing"
            
            # 检查是否在等待队列中
            if any(item[1] == task_id for item in queue_data.get("queue_pending", [])):
                return "pending"
            
            # 检查历史记录
            history_response = requests.get(f"{self.base_url}/history/{task_id}", headers=self.headers)
            if history_response.status_code == 200:
                history = history_response.json()
                if task_id in history:
                    return "completed"
            
            return "processing"
        except Exception as e:
            print(f"状态检查错误: {e}")
            return "processing"

    def download_image(self, task_id, output_path="qwen_image_output.png"):
        """📥 下载生成的图像"""
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
            print(f"下载错误: {e}")
            return None

def main():
    """🚀 主函数 - 执行 Qwen-Image 生成任务"""
    client = QwenImageClient()
    
    try:
        print("🎨 开始 Qwen-Image 图像生成任务...")
        
        # 🎯 示例提示词 - 香港霓虹街景
        prompt = '''A vibrant, warm neon-lit street scene in Hong Kong at the afternoon, with a mix of colorful Chinese and English signs glowing brightly. The atmosphere is lively, cinematic, and rain-washed with reflections on the pavement. The colors are vivid, full of pink, blue, red, and green hues. Crowded buildings with overlapping neon signs. 1980s Hong Kong style. Signs include:
"龍鳳冰室" "金華燒臘" "HAPPY HAIR" "鴻運茶餐廳" "EASY BAR" "永發魚蛋粉" "添記粥麵" "SUNSHINE MOTEL" "美都餐室" "富記糖水" "太平館" "雅芳髮型屋" "STAR KTV" "銀河娛樂城" "百樂門舞廳" "BUBBLE CAFE" "萬豪麻雀館" "CITY LIGHTS BAR" "瑞祥香燭莊" "文記文具" "GOLDEN JADE HOTEL" "LOVELY BEAUTY" "合興百貨" "興旺電器" And the background is warm yellow street and with all stores' lights on.'''
        
        negative_prompt = "low quality, blurry, distorted, bad anatomy, deformed text"
        
        print(f"📝 提示词: {prompt[:100]}...")
        
        # 🎨 生成图像
        task_id = client.generate_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=1328,
            height=1328,
            steps=20,
            cfg=2.5,
            shift=3.1
        )
        
        print(f"🆔 任务 ID: {task_id}")
        
        # ⏳ 等待完成
        while True:
            status = client.get_status(task_id)
            print(f"📊 当前状态: {status}")
            
            if status == "completed":
                print("✅ 图像生成完成!")
                break
            elif status == "failed":
                print("❌ 图像生成失败!")
                exit(1)
            
            time.sleep(10)
        
        # 📥 下载图像
        output_file = client.download_image(task_id, "qwen_image_hongkong.png")
        if output_file:
            print(f"🎉 图像下载成功! 保存为: {output_file}")
        else:
            print("❌ 图像下载失败")
    
    except Exception as e:
        print(f"❌ 错误: {e}")

# 🎯 预设示例函数
def generate_text_examples():
    """📝 生成不同类型的文本渲染示例"""
    client = QwenImageClient()
    
    examples = [
        {
            "name": "咖啡店招牌",
            "prompt": '''A cozy coffee shop entrance with a wooden chalkboard sign reading "Qwen Coffee ☕ 通义咖啡" in beautiful handwritten style. Below it shows "今日特价 Today's Special: 拿铁 Latte ¥25". The scene has warm lighting and vintage atmosphere.''',
            "filename": "coffee_shop_sign.png"
        },
        {
            "name": "数学公式黑板",
            "prompt": '''A university classroom blackboard with mathematical equations written in white chalk: "E=mc²", "π≈3.14159265359", "∫f(x)dx", "∑(n=1 to ∞)", "√(a²+b²)=c". The handwriting is clear and academic style.''',
            "filename": "math_blackboard.png"
        },
        {
            "name": "中英文书店",
            "prompt": '''A traditional bookstore with bilingual signs: "书香门第 Book Paradise", "新书上架 New Arrivals", "文学小说 Literature", "历史传记 Biography", "儿童读物 Children's Books". Warm wooden shelves filled with books.''',
            "filename": "bilingual_bookstore.png"
        },
        {
            "name": "日式拉面店",
            "prompt": '''A Japanese ramen shop with neon signs displaying: "らーめん Ramen", "味噌ラーメン Miso Ramen ¥800", "醤油ラーメン Shoyu Ramen ¥750", "豚骨ラーメン Tonkotsu Ramen ¥850". Traditional red lanterns and warm lighting.''',
            "filename": "ramen_shop_signs.png"
        }
    ]
    
    for example in examples:
        try:
            print(f"\n🎨 生成示例: {example['name']}")
            task_id = client.generate_image(
                prompt=example['prompt'],
                negative_prompt="low quality, blurry, illegible text, distorted characters",
                width=1328,
                height=1328,
                steps=20,
                cfg=2.5
            )
            
            # 等待完成
            while client.get_status(task_id) != "completed":
                time.sleep(5)
            
            # 下载
            output_file = client.download_image(task_id, example['filename'])
            if output_file:
                print(f"✅ {example['name']} 生成完成: {output_file}")
            
        except Exception as e:
            print(f"❌ {example['name']} 生成失败: {e}")

if __name__ == "__main__":
    # 运行主示例
    main()
    
    # 可选：运行多个文本渲染示例
    # generate_text_examples()

```
</details>