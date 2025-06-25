<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎨 Stable Diffusion 3 Medium 模型介绍</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">第三代扩散模型的中等参数版本，开源图像生成技术的重大进步</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**Stable Diffusion 3 Medium** 是 Stability AI 发布的第三代扩散模型的中等参数版本，代表了开源图像生成技术的重大进步。该模型在保持相对较低硬件要求的同时，显著提升了图像质量、文本理解能力和生成多样性，是 SD1.5 和高端模型之间的完美平衡选择。

</div>

## ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🏗️ 先进架构</h4>
<p style="margin: 0; color: #5b21b6;">基于多模态扩散变换器 (MMDiT) 架构</p>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🧠 增强文本理解</h4>
<p style="margin: 0; color: #065f46;">集成 T5-XXL 和双 CLIP 文本编码器</p>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">⚖️ 平衡性能</h4>
<p style="margin: 0; color: #991b1b;">20亿参数，实现质量与效率的最佳平衡</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📐 多宽高比支持</h4>
<p style="margin: 0; color: #1e40af;">原生支持各种分辨率和宽高比</p>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">👤 改进人体解剖</h4>
<p style="margin: 0; color: #9a3412;">显著减少手部和身体结构错误</p>
</div>

<div style="background: #ecfdf5; border-left: 4px solid #10b981; padding: 16px; border-radius: 4px;">
<h4 style="color: #10b981; margin: 0 0 8px 0;">🎭 风格多样性</h4>
<p style="margin: 0; color: #047857;">支持从写实到艺术的各种风格</p>
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
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">文本到图像生成</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">架构</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">多模态扩散变换器 (MMDiT)</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">参数规模</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">约 20 亿参数</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">文本编码器</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">T5-XXL + CLIP-L + CLIP-G</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">原生分辨率</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">1024×1024</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">推荐步数</td>
      <td style="padding: 12px;">20-50 步</td>
    </tr>
  </tbody>
</table>
</div>

---

# ⚙️ 配置说明

## 💻 系统要求

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 硬件配置要求</strong><br>
  <strong>ECS 显存</strong>: 推荐 8GB 或更多
</div>

## 📁 模型文件

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">文件类型</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">文件名</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">大小</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; font-weight: 500;">主模型</td>
      <td style="padding: 12px; font-family: monospace; background: #f8fafc;">sd3_medium_incl_clips_t5xxlfp16.safetensors</td>
      <td style="padding: 12px;">约 10GB</td>
    </tr>
  </tbody>
</table>
</div>

---

# 📖 使用指南

## 🌐 Web UI 使用方法

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🚀 基础操作流程

**1. 模型选择**
- 在模型选择器中选择 SD3 Medium 模型

**2. 提示词输入**
- 输入详细的图像描述

**3. 参数设置**
- 调整步数、CFG 和采样器

**4. 高级设置**
- 配置种子和批次设置

</div>

## ⚙️ 参数说明

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🔢 核心参数</h4>

**Steps (推理步数)**
- **15-20 步**: 快速生成，可接受质量
- **20-30 步**: 平衡质量和速度 (推荐)
- **30-50 步**: 最高质量，速度较慢

**CFG Scale (引导强度)**
- **4.0-5.0**: 自然结果，较少过拟合
- **5.0-7.0**: 平衡文本跟随和自然度 (推荐)
- **7.0-9.0**: 强文本跟随，可能过饱和
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">🎛️ 采样器选择</h4>

- **DPM++ 2M**: 高质量，推荐使用
- **Euler**: 快速稳定
- **DPM++ SDE**: 高质量但较慢
- **DDIM**: 经典选择，结果稳定
</div>

</div>

## 💡 提示词技巧

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">🎯 SD3 提示词特点</h4>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li><strong>更好的长文本理解</strong>: 支持更详细复杂的描述</li>
  <li><strong>改进的概念组合</strong>: 更好理解多概念组合</li>
  <li><strong>精确属性控制</strong>: 更精确控制颜色、材质、光照等</li>
  <li><strong>减少负面依赖</strong>: 对负面提示词依赖性降低</li>
</ul>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="color: #2563eb; margin: 0 0 8px 0;">📝 高质量提示词结构</h4>
<div style="background: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 14px; color: #1e40af;">
[详细主体描述] + [环境/背景] + [风格/技法] + [光照/氛围] + [质量词汇]
</div>
</div>

</div>

### 🎨 提示词示例

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📸 写实摄影风格</h4>
<div style="background: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; color: #065f46; line-height: 1.4;">
"一位自信的30多岁商务女性的专业头像，穿着深蓝色西装外套，坐在现代办公桌前，自然窗光，浅景深，85mm镜头拍摄，高分辨率，锐利对焦"
</div>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">🎨 艺术创作风格</h4>
<div style="background: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; color: #5b21b6; line-height: 1.4;">
"秋天法国乡村葡萄园的印象派绘画，金色阳光透过葡萄藤过滤，暖色调色板，松散笔触，户外写生风格，让人想起莫奈的作品"
</div>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h4 style="color: #dc2626; margin: 0 0 8px 0;">👤 角色肖像</h4>
<div style="background: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; color: #991b1b; line-height: 1.4;">
"一位年轻艺术家在工作室的详细肖像，沾满颜料的围裙，手持调色板和画笔，被画布包围，大窗户的自然光线，若有所思的表情，写实油画风格"
</div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
<h4 style="color: #ea580c; margin: 0 0 8px 0;">🏰 奇幻角色</h4>
<div style="background: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; color: #9a3412; line-height: 1.4;">
"精灵弓箭手的奇幻角色肖像，精致的皮甲，银发编织着树叶，锐利的绿眼睛，森林背景，详细的奇幻艺术，RPG角色设计"
</div>
</div>

</div>

---

## 🔌 API 调用

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff); box-shadow: 0 8px 16px rgba(37, 99, 235, 0.15);">
<summary style="font-weight: bold; font-size: 18px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); transition: all 0.3s ease; display: flex; align-items: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
📋 点击展开 API 调用 Python 代码
</summary>

```python
import requests
import base64

# 配置
base_url = "http://127.0.0.1:7680"
username = "admin"
apikey = "${APIKEY}"
auth = (username, apikey)

# 1. 切换模型
model_data = {
    "sd_model_checkpoint": "sd3_medium_incl_clips_t5xxlfp16.safetensors"
}

print("切换模型中...")
model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data, auth=auth)
print("模型切换完成")

# 2. 生成图像
prompt = "一只美丽的猫"
data = {
    "prompt": prompt,
    "steps": 20,
    "width": 512,
    "height": 512,
    "cfg_scale": 6.0,
    "sampler_name": "DPM++ 2M"
}

print("生成图像中...")
response = requests.post(f"{base_url}/sdapi/v1/txt2img", json=data, auth=auth)
result = response.json()

# 3. 保存图像
if "images" in result:
    image_data = base64.b64decode(result["images"][0])
    with open("output.png", "wb") as f:
        f.write(image_data)
    print("图像已保存为 output.png")
else:
    print("错误:", result)
```

</details>

---

## 💡 最佳实践

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="color: #059669; margin: 0 0 8px 0;">📝 提示词优化</h4>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>详细描述</strong>: SD3 能更好理解详细描述</li>
  <li><strong>自然语言</strong>: 使用自然句式而非关键词堆叠</li>
  <li><strong>具体属性</strong>: 明确指定颜色、材质、光照等属性</li>
  <li><strong>风格指导</strong>: 清楚指定艺术或技术风格</li>
  <li><strong>减少负面</strong>: 专注正面描述，减少负面提示词使用</li>
</ul>
</div>

<div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
<h4 style="color: #7c3aed; margin: 0 0 8px 0;">⚙️ 参数调优策略</h4>
<ul style="margin: 0; padding-left: 20px; color: #5b21b6;">
  <li><strong>起始设置</strong>: 25步 + CFG 6.0 + DPM++ 2M</li>
  <li><strong>快速预览</strong>: 20步 + CFG 5.0 用于快速测试</li>
  <li><strong>高质量</strong>: 30步 + CFG 6.5 获得最佳效果</li>
  <li><strong>风格实验</strong>: 在4.5-7.0范围内调整CFG测试</li>
</ul>
</div>

</div>

---

## 📊 模型对比

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">对比项目</th>
      <th style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">SD3 Medium</th>
      <th style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">SD1.5</th>
      <th style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">Flux1-Dev</th>
      <th style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0; color: #1e40af; font-weight: 600;">SDXL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">参数规模</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #059669;">2B</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #ea580c;">0.86B</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #dc2626;">12B</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #7c3aed;">3.5B</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">图像质量</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #059669;">优秀</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #ea580c;">良好</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #dc2626;">卓越</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #7c3aed;">优秀</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; font-weight: 500;">显存需求</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #059669;">8GB+</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #059669;">4GB+</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #dc2626;">12GB+</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9; text-align: center; color: #ea580c;">6GB+</td>
    </tr>
    <tr>
      <td style="padding: 12px; font-weight: 500;">生成速度</td>
      <td style="padding: 12px; text-align: center; color: #059669;">快速</td>
      <td style="padding: 12px; text-align: center; color: #059669;">很快</td>
      <td style="padding: 12px; text-align: center; color: #ea580c;">中等</td>
      <td style="padding: 12px; text-align: center; color: #7c3aed;">快速</td>
    </tr>
  </tbody>
</table>
</div>

---

## 🔧 常见问题与解决方案

<details style="border: 2px solid #dc2626; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #fef2f2, #fee2e2); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #dc2626; cursor: pointer;">🎨 生成质量问题</summary>
<div style="margin-top: 15px; color: #991b1b;">
<p><strong>解决方案：</strong></p>
<ul>
<li><strong>CFG 过高</strong>: 降低 CFG 到 4.5-7.0 范围</li>
<li><strong>步数不足</strong>: 增加到 25-30 步</li>
<li><strong>提示词过简</strong>: 使用更详细的描述</li>
</ul>
</div>
</details>

<details style="border: 2px solid #ea580c; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #fff7ed, #fed7aa); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #ea580c; cursor: pointer;">⚡ 性能问题</summary>
<div style="margin-top: 15px; color: #9a3412;">
<p><strong>优化建议：</strong></p>
<ul>
<li><strong>显存不足</strong>: 降低分辨率或使用 medvram 模式</li>
<li><strong>加载缓慢</strong>: SD3 模型较大，需要耐心</li>
<li><strong>生成缓慢</strong>: 使用更少步数或更快采样器</li>
</ul>
</div>
</details>

<details style="border: 2px solid #7c3aed; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(145deg, #faf5ff, #f3e8ff); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<summary style="font-weight: bold; font-size: 16px; color: #7c3aed; cursor: pointer;">🔧 兼容性问题</summary>
<div style="margin-top: 15px; color: #5b21b6;">
<p><strong>注意事项：</strong></p>
<ul>
<li><strong>WebUI 版本</strong>: 确保使用支持 SD3 的最新版本</li>
<li><strong>扩展兼容</strong>: 某些扩展可能与 SD3 不兼容</li>
<li><strong>参数范围</strong>: 注意 SD3 的推荐参数范围</li>
</ul>
</div>
</details>

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">📄 官方论文</h4>
<a href="https://arxiv.org/pdf/2403.03206" style="color: #2563eb; text-decoration: none; font-weight: 500;">Stable Diffusion 3 研究论文</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">了解SD3的技术原理和创新点</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">📊 技术报告</h4>
<a href="https://stability.ai/news/stable-diffusion-3-research-paper" style="color: #2563eb; text-decoration: none; font-weight: 500;">SD3 技术报告</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">详细的技术实现和性能评估</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">🤗 模型下载</h4>
<a href="https://www.modelscope.cn/models/AI-ModelScope/stable-diffusion-3-medium" style="color: #2563eb; text-decoration: none; font-weight: 500;">Model Scope 模型页面</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">官方模型文件下载地址</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">📖 使用文档</h4>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/16030" style="color: #2563eb; text-decoration: none; font-weight: 500;">WebUI SD3 支持文档</a>
<p style="margin-top: 8px; color: #64748b; font-size: 14px;">WebUI中SD3的配置和使用指南</p>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎨 <strong>开始您的 SD3 创作之旅！</strong> | 第三代扩散模型，让 AI 艺术创作更加精彩
  </p>
</div>