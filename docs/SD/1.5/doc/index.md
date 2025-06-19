<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 40px; box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
  <h1 style="font-size: 3em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎨 Stable Diffusion 1.5 模型使用指南</h1>
  <p style="font-size: 1.3em; margin: 15px 0 0 0; opacity: 0.9;">开源AI图像生成的经典之作 • 轻量高效 • 生态丰富</p>
</div>


---

## 📖 模型简介

<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 30px; border-radius: 15px; border-left: 6px solid #2196f3; margin: 25px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.1);">
  <h3 style="color: #1976d2; margin-top: 0;">🌟 经典之作</h3>
  <p style="font-size: 1.1em; line-height: 1.6; margin-bottom: 0;"><strong>Stable Diffusion 1.5</strong> 是由 Stability AI 开发的经典文本到图像生成模型，作为开源AI图像生成领域的里程碑之作，至今仍是最受欢迎和应用最广泛的模型之一。该模型以其轻量化、高效率和丰富的生态系统而闻名，是AI图像生成的入门首选。</p>
</div>

### ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
  <h4 style="margin-top: 0; font-size: 1.3em;">🚀 性能优势</h4>
  <ul style="list-style: none; padding: 0;">
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">💾</span><strong>轻量高效</strong>: 仅需6GB显存即可运行</li>
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">⚡</span><strong>快速生成</strong>: 推理速度快，适合批量生成</li>
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">🎯</span><strong>稳定可靠</strong>: 经过大量实际应用验证</li>
  </ul>
</div>

<div style="background: linear-gradient(135deg, #f093fb, #f5576c); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
  <h4 style="margin-top: 0; font-size: 1.3em;">🎨 功能特色</h4>
  <ul style="list-style: none; padding: 0;">
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">🌈</span><strong>风格多样</strong>: 支持写实、二次元、艺术等多种风格</li>
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">🔧</span><strong>易于定制</strong>: 支持LoRA、Textual Inversion等微调技术</li>
    <li style="margin: 10px 0; display: flex; align-items: center;"><span style="margin-right: 10px;">🌍</span><strong>生态丰富</strong>: 拥有庞大的社区和丰富的扩展生态</li>
  </ul>
</div>

</div>

### 📊 技术规格

<div style="background: #f8f9fa; border-radius: 15px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">
  <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <thead>
      <tr style="background: linear-gradient(135deg, #4facfe, #00f2fe); color: white;">
        <th style="padding: 15px; text-align: left; font-weight: 600;">规格项目</th>
        <th style="padding: 15px; text-align: left; font-weight: 600;">详细信息</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">🤖 <strong>模型类型</strong></td>
        <td style="padding: 15px;">文本到图像生成（Text-to-Image）/ 图像到图像生成（Image-to-Image）</td>
      </tr>
      <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">📈 <strong>参数规模</strong></td>
        <td style="padding: 15px;">约860M参数</td>
      </tr>
      <tr style="border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">🔤 <strong>文本编码器</strong></td>
        <td style="padding: 15px;">CLIP ViT-L/14</td>
      </tr>
      <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">🖼️ <strong>VAE</strong></td>
        <td style="padding: 15px;">512×512原生分辨率VAE</td>
      </tr>
      <tr style="border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">⏱️ <strong>推荐步数</strong></td>
        <td style="padding: 15px;">20-50步</td>
      </tr>
      <tr style="background: #f8f9fa;">
        <td style="padding: 15px; font-weight: 500;">💰 <strong>许可证</strong></td>
        <td style="padding: 15px;">开源免费，支持商业使用</td>
      </tr>
    </tbody>
  </table>
</div>

---

## ⚙️ 配置说明

### 💻 系统要求

<div style="background: linear-gradient(135deg, #fff3cd, #ffeaa7); padding: 25px; border-radius: 12px; border-left: 5px solid #ffc107; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="color: #856404; margin-top: 0;">⚠️ 最低配置要求</h4>
  <p style="margin-bottom: 0; font-size: 1.1em;"><strong>🖥️ ECS的GPU显存</strong>: 6GB以上</p>
</div>

### 📁 模型文件

<div style="background: #f8f9fa; border-radius: 15px; padding: 25px; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
  <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <thead>
      <tr style="background: linear-gradient(135deg, #43e97b, #38f9d7); color: white;">
        <th style="padding: 15px; text-align: left; font-weight: 600;">文件类型</th>
        <th style="padding: 15px; text-align: left; font-weight: 600;">文件名</th>
        <th style="padding: 15px; text-align: left; font-weight: 600;">说明</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">🎯 <strong>主模型</strong></td>
        <td style="padding: 15px; font-family: monospace; background: #f8f9fa; border-radius: 4px;">v1-5-pruned-emaonly.safetensors</td>
        <td style="padding: 15px;">核心生成模型</td>
      </tr>
      <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
        <td style="padding: 15px; font-weight: 500;">🎨 <strong>VAE</strong></td>
        <td style="padding: 15px; font-family: monospace; background: #e9ecef; border-radius: 4px;">vae-ft-mse-840000-ema-pruned.safetensors</td>
        <td style="padding: 15px;">可选的高质量VAE</td>
      </tr>
      <tr>
        <td style="padding: 15px; font-weight: 500;">📝 <strong>文本编码器</strong></td>
        <td style="padding: 15px; color: #6c757d; font-style: italic;">-</td>
        <td style="padding: 15px;">内置于主模型中</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 🚀 使用指南

### 🌐 Web UI 使用

#### 📋 基础操作流程

<div style="display: grid; grid-template-columns: 1fr; gap: 20px; margin: 25px 0;">

<details style="border: 2px solid #28a745; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 18px; color: #28a745; cursor: pointer; display: flex; align-items: center; gap: 10px;">
🎯 <span>1. 模型选择</span>
</summary>
<div style="margin-top: 15px;">
<p>在左上角模型选择器中选择SD1.5模型</p>
<div style="text-align: center; margin: 15px 0; padding: 15px; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <img src="img.png" alt="模型选择界面" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="margin-top: 10px; color: #666; font-style: italic;">模型选择界面示例</p>
</div>
</div>
</details>

<details style="border: 2px solid #007bff; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 18px; color: #007bff; cursor: pointer; display: flex; align-items: center; gap: 10px;">
✍️ <span>2. 提示词输入</span>
</summary>
<div style="margin-top: 15px;">
<ul style="list-style: none; padding: 0;">
  <li style="margin: 10px 0; padding: 10px; background: white; border-radius: 8px; border-left: 4px solid #28a745;">
    <strong>✅ 正向提示词</strong>: 详细描述想要生成的图像内容
  </li>
  <li style="margin: 10px 0; padding: 10px; background: white; border-radius: 8px; border-left: 4px solid #dc3545;">
    <strong>❌ 负向提示词</strong>: 描述不想要的元素（SD1.5对负向提示词响应良好）
  </li>
</ul>
</div>
</details>

<details style="border: 2px solid #6f42c1; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #faf9ff 0%, #f0ebff 100%); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 18px; color: #6f42c1; cursor: pointer; display: flex; align-items: center; gap: 10px;">
⚙️ <span>3. 参数设置</span>
</summary>
<div style="margin-top: 15px;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;">
  <thead>
    <tr style="background: #6f42c1; color: white;">
      <th style="padding: 12px; text-align: left;">参数</th>
      <th style="padding: 12px; text-align: left;">推荐值</th>
      <th style="padding: 12px; text-align: left;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px;">📊 <strong>步数</strong></td>
      <td style="padding: 12px; font-family: monospace; background: #f8f9fa;">20-30步</td>
      <td style="padding: 12px;">生成质量与速度的平衡</td>
    </tr>
    <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px;">🎚️ <strong>CFG Scale</strong></td>
      <td style="padding: 12px; font-family: monospace; background: #e9ecef;">7-12</td>
      <td style="padding: 12px;">提示词遵循程度</td>
    </tr>
    <tr style="border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px;">🔄 <strong>采样器</strong></td>
      <td style="padding: 12px; font-family: monospace; background: #f8f9fa;">DPM++ 2M Karras / Euler a</td>
      <td style="padding: 12px;">推荐采样算法</td>
    </tr>
    <tr style="background: #f8f9fa;">
      <td style="padding: 12px;">📐 <strong>分辨率</strong></td>
      <td style="padding: 12px; font-family: monospace; background: #e9ecef;">512×512</td>
      <td style="padding: 12px;">原生分辨率，效果最佳</td>
    </tr>
  </tbody>
</table>
</div>
</details>

<details style="border: 2px solid #fd7e14; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #fff8f0 0%, #ffe8d4 100%); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 18px; color: #fd7e14; cursor: pointer; display: flex; align-items: center; gap: 10px;">
🔧 <span>4. 高级设置</span>
</summary>
<div style="margin-top: 15px;">
<ul style="list-style: none; padding: 0;">
  <li style="margin: 10px 0; padding: 10px; background: white; border-radius: 8px; display: flex; align-items: center;">
    <span style="margin-right: 10px;">🎲</span><strong>种子</strong>: 控制随机性，-1为随机
  </li>
  <li style="margin: 10px 0; padding: 10px; background: white; border-radius: 8px; display: flex; align-items: center;">
    <span style="margin-right: 10px;">📦</span><strong>批次</strong>: 设置生成数量
  </li>
  <li style="margin: 10px 0; padding: 10px; background: white; border-radius: 8px; display: flex; align-items: center;">
    <span style="margin-right: 10px;">🔍</span><strong>高分辨率修复</strong>: 生成更大尺寸图像
  </li>
</ul>
</div>
</details>

</div>

#### 🎨 推荐参数组合

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="border: 3px solid #28a745; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%); box-shadow: 0 8px 25px rgba(40, 167, 69, 0.2);">
<h4 style="color: #28a745; margin-top: 0; display: flex; align-items: center; gap: 10px;"><span>⚡</span>快速生成</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📊</span><strong>步数</strong>: 20步</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🎚️</span><strong>CFG</strong>: 7</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🔄</span><strong>采样器</strong>: Euler a</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📐</span><strong>分辨率</strong>: 512×512</li>
</ul>
</div>

<div style="border: 3px solid #007bff; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%); box-shadow: 0 8px 25px rgba(0, 123, 255, 0.2);">
<h4 style="color: #007bff; margin-top: 0; display: flex; align-items: center; gap: 10px;"><span>💎</span>高质量</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📊</span><strong>步数</strong>: 30步</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🎚️</span><strong>CFG</strong>: 9-11</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🔄</span><strong>采样器</strong>: DPM++ 2M Karras</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📐</span><strong>分辨率</strong>: 768×768</li>
</ul>
</div>

<div style="border: 3px solid #6f42c1; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #faf9ff 0%, #f0ebff 100%); box-shadow: 0 8px 25px rgba(111, 66, 193, 0.2);">
<h4 style="color: #6f42c1; margin-top: 0; display: flex; align-items: center; gap: 10px;"><span>🎨</span>艺术风格</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📊</span><strong>步数</strong>: 25步</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🎚️</span><strong>CFG</strong>: 8-10</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>🔄</span><strong>采样器</strong>: DDIM</li>
<li style="margin: 8px 0; display: flex; align-items: center; gap: 10px;"><span>📐</span><strong>分辨率</strong>: 512×768</li>
</ul>
</div>

</div>

---

### 🔌 API 调用

<div style="background: linear-gradient(135deg, #fff3cd, #ffeaa7); padding: 25px; border-radius: 12px; border-left: 5px solid #ffc107; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="color: #856404; margin-top: 0;">⚠️ 重要提示</h4>
  <p style="margin-bottom: 10px;">需要将 <code style="background: #f8f9fa; padding: 2px 6px; border-radius: 4px;">BASE_URL</code> 和 <code style="background: #f8f9fa; padding: 2px 6px; border-radius: 4px;">APIKEY</code> 替换为实际值</p>

  <div style="text-align: center; margin: 15px 0; padding: 15px; background: white; border-radius: 8px;">
    <img src="img_1.png" alt="API配置示例" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <p style="margin-top: 10px; color: #666; font-style: italic;">API配置界面示例</p>
  </div>

  <p style="margin-bottom: 0;">如果要用公网调用，则选择公网的ip:端口</p>
</div>

<details style="border: 3px solid #0066cc; border-radius: 15px; padding: 25px; margin: 25px 0; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); box-shadow: 0 8px 25px rgba(0,102,204,0.2);">
<summary style="font-weight: bold; font-size: 20px; color: #0066cc; cursor: pointer; display: flex; align-items: center; gap: 15px; padding: 10px;">
🐍 <span>点击展开API调用Python代码</span>
</summary>

<div style="margin-top: 20px; background: #1e1e1e; border-radius: 10px; padding: 20px; overflow-x: auto;">

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

<div style="background: linear-gradient(135deg, #d1ecf1, #bee5eb); padding: 20px; border-radius: 12px; border-left: 5px solid #17a2b8; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
  <h4 style="color: #0c5460; margin-top: 0;">💡 提示</h4>
  <p style="margin-bottom: 10px;">若未开启APIKEY，请使用以下代码修改请求：</p>
  <div style="background: #1e1e1e; border-radius: 8px; padding: 15px; margin-top: 10px;">
    <code style="color: #f8f9fa; font-family: 'Courier New', monospace;">
      model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data)
    </code>
  </div>
</div>

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="border: 2px solid #e9ecef; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
<h4 style="margin-top: 0; color: #495057; display: flex; align-items: center; gap: 10px;"><span>📖</span>官方文档</h4>
<a href="https://stability.ai/stable-diffusion" style="color: #007bff; text-decoration: none; font-weight: 500;">Stable Diffusion官方文档</a>
<p style="margin-top: 10px; color: #6c757d; font-size: 0.9em;">了解模型的官方介绍和技术细节</p>
</div>

<div style="border: 2px solid #e9ecef; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
<h4 style="margin-top: 0; color: #495057; display: flex; align-items: center; gap: 10px;"><span>🖥️</span>Web界面</h4>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui" style="color: #007bff; text-decoration: none; font-weight: 500;">Automatic1111 WebUI</a>
<p style="margin-top: 10px; color: #6c757d; font-size: 0.9em;">最受欢迎的SD Web界面项目</p>
</div>

<div style="border: 2px solid #e9ecef; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
<h4 style="margin-top: 0; color: #495057; display: flex; align-items: center; gap: 10px;"><span>🎨</span>模型社区</h4>
<a href="https://civitai.com/" style="color: #007bff; text-decoration: none; font-weight: 500;">Civitai模型社区</a>
<p style="margin-top: 10px; color: #6c757d; font-size: 0.9em;">下载各种风格的SD模型和LoRA</p>
</div>

<div style="border: 2px solid #e9ecef; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
<h4 style="margin-top: 0; color: #495057; display: flex; align-items: center; gap: 10px;"><span>✍️</span>提示词指南</h4>
<a href="https://prompthero.com/stable-diffusion-prompts" style="color: #007bff; text-decoration: none; font-weight: 500;">提示词工程指南</a>
<p style="margin-top: 10px; color: #6c757d; font-size: 0.9em;">学习如何编写高质量的提示词</p>
</div>

<div style="border: 2px solid #e9ecef; border-radius: 12px; padding: 20px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
<h4 style="margin-top: 0; color: #495057; display: flex; align-items: center; gap: 10px;"><span>🔧</span>LoRA训练</h4>
<a href="https://github.com/cloneofsimo/lora" style="color: #007bff; text-decoration: none; font-weight: 500;">LoRA训练教程</a>
<p style="margin-top: 10px; color: #6c757d; font-size: 0.9em;">学习如何训练自定义LoRA模型</p>
</div>

</div>

---

## 🎯 最佳实践

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #43e97b, #38f9d7); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
  <h4 style="margin-top: 0; font-size: 1.3em;">✍️ 提示词技巧</h4>
  <ul style="list-style: none; padding: 0;">
    <li style="margin: 10px 0;">• 使用具体的描述词而非抽象概念</li>
    <li style="margin: 10px 0;">• 添加艺术家名字来指定风格</li>
    <li style="margin: 10px 0;">• 使用权重语法 (word:1.2) 强调重要元素</li>
    <li style="margin: 10px 0;">• 负向提示词排除不需要的内容</li>
  </ul>
</div>

<div style="background: linear-gradient(135deg, #fa709a, #fee140); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
  <h4 style="margin-top: 0; font-size: 1.3em;">⚙️ 参数调优</h4>
  <ul style="list-style: none; padding: 0;">
    <li style="margin: 10px 0;">• 从低步数开始测试，逐步增加</li>
    <li style="margin: 10px 0;">• CFG过高会导致过度饱和</li>
    <li style="margin: 10px 0;">• 不同采样器适合不同风格</li>
    <li style="margin: 10px 0;">• 使用固定种子复现满意结果</li>
  </ul>
</div>

</div>

---

## ❓ 常见问题

<details style="border: 2px solid #dc3545; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #fff5f5, #fed7d7); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #dc3545; cursor: pointer;">❓ 生成的图像质量不佳怎么办？</summary>
<div style="margin-top: 15px; color: #721c24;">
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

<details style="border: 2px solid #fd7e14; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #fff8f0, #ffe8d4); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #fd7e14; cursor: pointer;">❓ 显存不足如何处理？</summary>
<div style="margin-top: 15px; color: #8a4a00;">
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

<details style="border: 2px solid #6f42c1; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #faf9ff, #f0ebff); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #6f42c1; cursor: pointer;">❓ 如何获得特定风格的图像？</summary>
<div style="margin-top: 15px; color: #4a1a5c;">
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

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin: 40px 0; box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
  <h2 style="margin: 0 0 15px 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎉 开始你的AI艺术创作之旅！</h2>
  <p style="font-size: 1.3em; margin: 0; opacity: 0.9; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
    <em>Stable Diffusion 1.5 - 让创意无限可能</em>
  </p>
  <div style="margin-top: 25px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 0.9em;">🎨 创意无限</span>
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 0.9em;">⚡ 高效便捷</span>
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 0.9em;">🌍 开源免费</span>
  </div>
</div>