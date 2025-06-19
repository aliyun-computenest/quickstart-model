# 🎨 Stable Diffusion 1.5 模型使用指南

<div align="center">

![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-1.5-blue?style=for-the-badge&logo=stability-ai)
![License](https://img.shields.io/badge/License-Open%20Source-green?style=for-the-badge)
![GPU](https://img.shields.io/badge/GPU-6GB+-orange?style=for-the-badge&logo=nvidia)

</div>

---

## 📖 模型简介

**Stable Diffusion 1.5** 是由 Stability AI 开发的经典文本到图像生成模型，作为开源AI图像生成领域的里程碑之作，至今仍是最受欢迎和应用最广泛的模型之一。该模型以其轻量化、高效率和丰富的生态系统而闻名，是AI图像生成的入门首选。

### ✨ 核心特性

<table>
<tr>
<td width="50%">

**🚀 性能优势**
- 💾 **轻量高效**: 仅需6GB显存即可运行
- ⚡ **快速生成**: 推理速度快，适合批量生成
- 🎯 **稳定可靠**: 经过大量实际应用验证

</td>
<td width="50%">

**🎨 功能特色**
- 🌈 **风格多样**: 支持写实、二次元、艺术等多种风格
- 🔧 **易于定制**: 支持LoRA、Textual Inversion等微调技术
- 🌍 **生态丰富**: 拥有庞大的社区和丰富的扩展生态

</td>
</tr>
</table>

### 📊 技术规格

| 规格项目 | 详细信息 |
|---------|---------|
| 🤖 **模型类型** | 文本到图像生成（Text-to-Image）/ 图像到图像生成（Image-to-Image） |
| 📈 **参数规模** | 约860M参数 |
| 🔤 **文本编码器** | CLIP ViT-L/14 |
| 🖼️ **VAE** | 512×512原生分辨率VAE |
| ⏱️ **推荐步数** | 20-50步 |
| 💰 **许可证** | 开源免费，支持商业使用 |

---

## ⚙️ 配置说明

### 💻 系统要求

> **最低配置要求**
>
> 🖥️ **ECS的GPU显存**: 6GB以上

### 📁 模型文件

| 文件类型 | 文件名 | 说明 |
|---------|--------|------|
| 🎯 **主模型** | `v1-5-pruned-emaonly.safetensors` | 核心生成模型 |
| 🎨 **VAE** | `vae-ft-mse-840000-ema-pruned.safetensors` | 可选的高质量VAE |
| 📝 **文本编码器** | - | 内置于主模型中 |

---

## 🚀 使用指南

### 🌐 Web UI 使用

#### 📋 基础操作流程

<details>
<summary><strong>🎯 1. 模型选择</strong></summary>

在左上角模型选择器中选择SD1.5模型

![模型选择](img.png)

</details>

<details>
<summary><strong>✍️ 2. 提示词输入</strong></summary>

- **✅ 正向提示词**: 详细描述想要生成的图像内容
- **❌ 负向提示词**: 描述不想要的元素（SD1.5对负向提示词响应良好）

</details>

<details>
<summary><strong>⚙️ 3. 参数设置</strong></summary>

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| 📊 **步数** | 20-30步 | 生成质量与速度的平衡 |
| 🎚️ **CFG Scale** | 7-12 | 提示词遵循程度 |
| 🔄 **采样器** | DPM++ 2M Karras / Euler a | 推荐采样算法 |
| 📐 **分辨率** | 512×512 | 原生分辨率，效果最佳 |

</details>

<details>
<summary><strong>🔧 4. 高级设置</strong></summary>

- 🎲 **种子**: 控制随机性，-1为随机
- 📦 **批次**: 设置生成数量
- 🔍 **高分辨率修复**: 生成更大尺寸图像

</details>

#### 🎨 推荐参数组合

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="border: 2px solid #28a745; border-radius: 10px; padding: 15px; background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%);">
<h4 style="color: #28a745; margin-top: 0;">⚡ 快速生成</h4>
<ul>
<li>📊 步数: 20步</li>
<li>🎚️ CFG: 7</li>
<li>🔄 采样器: Euler a</li>
<li>📐 分辨率: 512×512</li>
</ul>
</div>

<div style="border: 2px solid #007bff; border-radius: 10px; padding: 15px; background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%);">
<h4 style="color: #007bff; margin-top: 0;">💎 高质量</h4>
<ul>
<li>📊 步数: 30步</li>
<li>🎚️ CFG: 9-11</li>
<li>🔄 采样器: DPM++ 2M Karras</li>
<li>📐 分辨率: 768×768</li>
</ul>
</div>

<div style="border: 2px solid #6f42c1; border-radius: 10px; padding: 15px; background: linear-gradient(135deg, #faf9ff 0%, #f0ebff 100%);">
<h4 style="color: #6f42c1; margin-top: 0;">🎨 艺术风格</h4>
<ul>
<li>📊 步数: 25步</li>
<li>🎚️ CFG: 8-10</li>
<li>🔄 采样器: DDIM</li>
<li>📐 分辨率: 512×768</li>
</ul>
</div>

</div>

---

### 🔌 API 调用

> **⚠️ 重要提示**
>
> 需要将 `BASE_URL` 和 `APIKEY` 替换为实际值
>
> ![API配置](img_1.png)
>
> 如果要用公网调用，则选择公网的ip:端口

<details style="border: 2px solid #0066cc; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 18px; color: #0066cc; cursor: pointer; display: flex; align-items: center; gap: 10px;">
🐍 <span>点击展开API调用Python代码</span>
</summary>

<div style="margin-top: 15px;">

```python
import requests
import base64

# 🔧 配置信息
base_url = "<部署服务的Output URL>"
username = "admin"
apikey = "${APIKEY}"
auth = (username, apikey)

# 🔄 1. 切换模型
model_data = {
    "sd_model_checkpoint": "v1-5-pruned-emaonly.safetensors"
}

print("🔄 正在切换模型...")
model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data, auth=auth)
print("✅ 模型切换完成")

# 🎨 2. 生成图片
prompt = "a beautiful cat"
data = {
    "prompt": prompt,
    "steps": 20,
    "width": 512,
    "height": 512
}

print("🎨 正在生成图片...")
response = requests.post(f"{base_url}/sdapi/v1/txt2img", json=data, auth=auth)
result = response.json()

# 💾 3. 保存图片
if "images" in result:
    image_data = base64.b64decode(result["images"][0])
    with open("output.png", "wb") as f:
        f.write(image_data)
    print("✅ 图片已保存为 output.png")
else:
    print("❌ 错误:", result)
```

</div>
</details>

> **💡 提示**
>
> 若未开启APIKEY，请使用以下代码修改请求：
>
> ```python
> model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data)
> ```

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="border: 1px solid #dee2e6; border-radius: 8px; padding: 15px; background: #fff;">
<h4 style="margin-top: 0; color: #495057;">📖 官方文档</h4>
<a href="https://stability.ai/stable-diffusion" style="color: #007bff; text-decoration: none;">Stable Diffusion官方文档</a>
</div>

<div style="border: 1px solid #dee2e6; border-radius: 8px; padding: 15px; background: #fff;">
<h4 style="margin-top: 0; color: #495057;">🖥️ Web界面</h4>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui" style="color: #007bff; text-decoration: none;">Automatic1111 WebUI</a>
</div>

<div style="border: 1px solid #dee2e6; border-radius: 8px; padding: 15px; background: #fff;">
<h4 style="margin-top: 0; color: #495057;">🎨 模型社区</h4>
<a href="https://civitai.com/" style="color: #007bff; text-decoration: none;">Civitai模型社区</a>
</div>

<div style="border: 1px solid #dee2e6; border-radius: 8px; padding: 15px; background: #fff;">
<h4 style="margin-top: 0; color: #495057;">✍️ 提示词指南</h4>
<a href="https://prompthero.com/stable-diffusion-prompts" style="color: #007bff; text-decoration: none;">提示词工程指南</a>
</div>

<div style="border: 1px solid #dee2e6; border-radius: 8px; padding: 15px; background: #fff;">
<h4 style="margin-top: 0; color: #495057;">🔧 LoRA训练</h4>
<a href="https://github.com/cloneofsimo/lora" style="color: #007bff; text-decoration: none;">LoRA训练教程</a>
</div>

</div>

---

<div align="center" style="margin-top: 40px; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">

**🎉 开始你的AI艺术创作之旅！**

*Stable Diffusion 1.5 - 让创意无限可能*

</div>