<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎨 Stable Diffusion 1.5 模型使用指南</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">开源AI图像生成的经典之作 • 轻量高效 • 生态丰富</p>
</div>

## 📖 模型简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Stable Diffusion 1.5** 是由 Stability AI 开发的经典文本到图像生成模型，作为开源AI图像生成领域的里程碑之作，至今仍是最受欢迎和应用最广泛的模型之一。该模型以其轻量化、高效率和丰富的生态系统而闻名，是AI图像生成的入门首选。

</div>

## 🚀 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🚀 性能优势</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>轻量高效</strong>: 仅需6GB显存即可运行</li>
  <li><strong>快速生成</strong>: 推理速度快，适合批量生成</li>
  <li><strong>稳定可靠</strong>: 经过大量实际应用验证</li>
</ul>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">🎨 功能特色</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af;">
  <li><strong>风格多样</strong>: 支持写实、二次元、艺术等多种风格</li>
  <li><strong>易于定制</strong>: 支持LoRA、Textual Inversion等微调技术</li>
  <li><strong>生态丰富</strong>: 拥有庞大的社区和丰富的扩展生态</li>
</ul>
</div>

</div>

## 📊 技术规格

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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">文本到图像生成（Text-to-Image）/ 图像到图像生成（Image-to-Image）</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">参数规模</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">约860M参数</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">文本编码器</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">CLIP ViT-L/14</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">VAE</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">512×512原生分辨率VAE</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">推荐步数</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">20-50步</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">许可证</td>
      <td style="padding: 12px;">开源免费，支持商业使用</td>
    </tr>
  </tbody>
</table>
</div>

---

# ⚙️ 配置说明

## 💻 系统要求

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 最低配置要求</strong><br>
  <strong>ECS的GPU显存</strong>: 6GB以上
</div>

## 📁 模型文件

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">文件类型</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">文件名</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">主模型</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">v1-5-pruned-emaonly.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">核心生成模型</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">VAE</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-family: monospace; background: #f8fafc;">vae-ft-mse-840000-ema-pruned.safetensors</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">可选的高质量VAE</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">文本编码器</td>
      <td style="padding: 12px; color: #64748b; font-style: italic;">-</td>
      <td style="padding: 12px;">内置于主模型中</td>
    </tr>
  </tbody>
</table>
</div>

---

# 📖 使用指南

## 🌐 Web UI 使用

### 📋 基础操作流程

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**1. 模型选择**
- 在左上角模型选择器中选择SD1.5模型

![img.png](img.png)

**2. 提示词输入**
- **正向提示词**: 详细描述想要生成的图像内容
- **负向提示词**: 描述不想要的元素（SD1.5对负向提示词响应良好）

**3. 参数设置**
- **步数**: 推荐 20-30步（生成质量与速度的平衡）
- **CFG Scale**: 推荐 7-12（提示词遵循程度）
- **采样器**: 推荐 DPM++ 2M Karras / Euler a
- **分辨率**: 512×512（原生分辨率，效果最佳）

**4. 高级设置**
- **种子**: 控制随机性，-1为随机
- **批次**: 设置生成数量
- **高分辨率修复**: 生成更大尺寸图像

</div>

### 🎨 推荐参数组合

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">⚡ 快速生成</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>步数</strong>: 20步</li>
  <li><strong>CFG</strong>: 7</li>
  <li><strong>采样器</strong>: Euler a</li>
  <li><strong>分辨率</strong>: 512×512</li>
</ul>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">💎 高质量</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af;">
  <li><strong>步数</strong>: 30步</li>
  <li><strong>CFG</strong>: 9-11</li>
  <li><strong>采样器</strong>: DPM++ 2M Karras</li>
  <li><strong>分辨率</strong>: 768×768</li>
</ul>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🎨 艺术风格</h4>
<ul style="margin: 0; padding-left: 20px; color: #5b21b6;">
  <li><strong>步数</strong>: 25步</li>
  <li><strong>CFG</strong>: 8-10</li>
  <li><strong>采样器</strong>: DDIM</li>
  <li><strong>分辨率</strong>: 512×768</li>
</ul>
</div>

</div>

---

## 🔌 API 调用

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 重要提示</strong><br>
  需要将 <code style="background: #f8fafc; padding: 2px 6px; border-radius: 4px;">BASE_URL</code> 和 <code style="background: #f8fafc; padding: 2px 6px; border-radius: 4px;">APIKEY</code> 替换为实际值。如果要用公网调用，则选择公网的ip:端口。
</div>

![img_1.png](img_1.png)

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
🐍 点击展开API调用Python代码
</summary>

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

</details>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 提示</strong><br>
  若未开启APIKEY，请使用以下代码修改请求：<br>
  <code style="background: #f8fafc; padding: 2px 6px; border-radius: 4px;">model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data)</code>
</div>

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">📖 官方文档</h4>
<a href="https://stability.ai/stable-diffusion" style="color: #2563eb; text-decoration: none; font-weight: 500;">Stable Diffusion官方文档</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">了解模型的官方介绍和技术细节</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">🖥️ Web界面</h4>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui" style="color: #2563eb; text-decoration: none; font-weight: 500;">Automatic1111 WebUI</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">最受欢迎的SD Web界面项目</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">🎨 模型社区</h4>
<a href="https://civitai.com/" style="color: #2563eb; text-decoration: none; font-weight: 500;">Civitai模型社区</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">下载各种风格的SD模型和LoRA</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">✍️ 提示词指南</h4>
<a href="https://prompthero.com/stable-diffusion-prompts" style="color: #2563eb; text-decoration: none; font-weight: 500;">提示词工程指南</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">学习如何编写高质量的提示词</p>
</div>

</div>

---

## 🎯 最佳实践

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">✍️ 提示词技巧</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li>使用具体的描述词而非抽象概念</li>
  <li>添加艺术家名字来指定风格</li>
  <li>使用权重语法 (word:1.2) 强调重要元素</li>
  <li>负向提示词排除不需要的内容</li>
</ul>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">⚙️ 参数调优</h4>
<ul style="margin: 0; padding-left: 20px; color: #1e40af;">
  <li>从低步数开始测试，逐步增加</li>
  <li>CFG过高会导致过度饱和</li>
  <li>不同采样器适合不同风格</li>
  <li>使用固定种子复现满意结果</li>
</ul>
</div>

</div>

---

## ❓ 常见问题

<details style="border: 2px solid #dc2626; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #fef2f2, #fee2e2); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #dc2626; cursor: pointer;">❓ 生成的图像质量不佳怎么办？</summary>
<div style="margin-top: 15px; color: #991b1b;">
<p><strong>解决方案：</strong></p>
<ul>
<li>增加生成步数到30-50步</li>
<li>调整CFG Scale到8-12</li>
<li>使用更详细的提示词</li>
<li>尝试不同的采样器</li>
<li>考虑使用高质量VAE</li>
</ul>
</div>
</details>

<details style="border: 2px solid #ea580c; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #fff7ed, #fed7aa); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #ea580c; cursor: pointer;">❓ 显存不足如何处理？</summary>
<div style="margin-top: 15px; color: #9a3412;">
<p><strong>优化建议：</strong></p>
<ul>
<li>降低生成分辨率到512×512</li>
<li>减少批次大小</li>
<li>启用低显存模式</li>
<li>关闭不必要的扩展</li>
<li>使用精度优化选项</li>
</ul>
</div>
</details>

<details style="border: 2px solid #7c3aed; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #faf5ff, #f3e8ff); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #7c3aed; cursor: pointer;">❓ 如何获得特定风格的图像？</summary>
<div style="margin-top: 15px; color: #5b21b6;">
<p><strong>风格控制方法：</strong></p>
<ul>
<li>在提示词中添加艺术家名字</li>
<li>使用风格关键词（如"oil painting", "anime style"）</li>
<li>下载并使用专门的风格LoRA</li>
<li>参考社区分享的提示词模板</li>
<li>调整CFG Scale影响风格强度</li>
</ul>
</div>
</details>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎨 <strong>开始你的AI艺术创作之旅！</strong> | Stable Diffusion 1.5 - 让创意无限可能
  </p>
</div>