# 🎨 Stable Diffusion 3 Medium 模型介绍

<div align="center">

![SD3 Medium](images/SD3_Medium_4294b8c6ad11.svg)
![参数量](images/参数量_8d903817f54e.svg)
![架构](images/架构_e344d0d87dab.svg)
![开源](images/开源_89f7e05eb906.svg)

</div>

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 20px; margin: 20px 0; text-align: center;">

**Stable Diffusion 3 Medium** 是 Stability AI 发布的第三代扩散模型的中等参数版本，代表了开源图像生成技术的重大进步。该模型在保持相对较低硬件要求的同时，显著提升了图像质量、文本理解能力和生成多样性，是 SD1.5 和高端模型之间的完美平衡选择。

</div>

---

## ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(108, 92, 231, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">🏗️</div>
<h3 style="margin: 10px 0;">先进架构</h3>
<p style="margin: 0; opacity: 0.9;">基于多模态扩散变换器 (MMDiT) 架构</p>
</div>

<div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(0, 184, 148, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">🧠</div>
<h3 style="margin: 10px 0;">增强文本理解</h3>
<p style="margin: 0; opacity: 0.9;">集成 T5-XXL 和双 CLIP 文本编码器</p>
</div>

<div style="background: linear-gradient(135deg, #e17055 0%, #fd79a8 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(225, 112, 85, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">⚖️</div>
<h3 style="margin: 10px 0;">平衡性能</h3>
<p style="margin: 0; opacity: 0.9;">20亿参数，实现质量与效率的最佳平衡</p>
</div>

<div style="background: linear-gradient(135deg, #0984e3 0%, #74b9ff 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(9, 132, 227, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">📐</div>
<h3 style="margin: 10px 0;">多宽高比支持</h3>
<p style="margin: 0; opacity: 0.9;">原生支持各种分辨率和宽高比</p>
</div>

<div style="background: linear-gradient(135deg, #fdcb6e 0%, #e84393 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(253, 203, 110, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">👤</div>
<h3 style="margin: 10px 0;">改进人体解剖</h3>
<p style="margin: 0; opacity: 0.9;">显著减少手部和身体结构错误</p>
</div>

<div style="background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(162, 155, 254, 0.3);">
<div style="font-size: 2.5em; margin-bottom: 15px;">🎭</div>
<h3 style="margin: 10px 0;">风格多样性</h3>
<p style="margin: 0; opacity: 0.9;">支持从写实到艺术的各种风格</p>
</div>

</div>

---

## 📊 技术规格

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 20px; margin: 30px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">🎯</span> 模型类型
</h4>
<p style="margin: 0; font-size: 1.1em;">文本到图像生成</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">🏗️</span> 架构
</h4>
<p style="margin: 0; font-size: 1.1em;">多模态扩散变换器 (MMDiT)</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">📊</span> 参数规模
</h4>
<p style="margin: 0; font-size: 1.1em;">约 20 亿参数</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">📝</span> 文本编码器
</h4>
<p style="margin: 0; font-size: 1.1em;">T5-XXL + CLIP-L + CLIP-G</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">🖼️</span> 原生分辨率
</h4>
<p style="margin: 0; font-size: 1.1em;">1024×1024</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; color: white;">
<h4 style="margin: 0 0 15px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">⚙️</span> 推荐步数
</h4>
<p style="margin: 0; font-size: 1.1em;">20-50 步</p>
</div>

</div>

</div>

---

## 🔧 配置说明

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #0984e3 0%, #74b9ff 100%); color: white; padding: 25px; border-radius: 15px; box-shadow: 0 8px 25px rgba(9, 132, 227, 0.3);">
<h3 style="margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">💻</span> 系统要求
</h3>
<div style="background: rgba(255,255,255,0.15); padding: 15px; border-radius: 10px;">
<strong>ECS 显存:</strong> 推荐 8GB 或更多
</div>
</div>

<div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%); color: white; padding: 25px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0, 184, 148, 0.3);">
<h3 style="margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">📁</span> 模型文件
</h3>
<div style="background: rgba(255,255,255,0.15); padding: 15px; border-radius: 10px;">
<strong>主模型:</strong> sd3_medium_incl_clips_t5xxlfp16.safetensors<br>
<small style="opacity: 0.8;">(约 10GB)</small>
</div>
</div>

</div>

---

# 📖 使用指南

## 🌐 Web UI 使用方法

<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); color: white; padding: 30px; border-radius: 20px; margin: 30px 0;">

### 🚀 基础操作

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; text-align: center;">
<div style="font-size: 2em; margin-bottom: 10px;">🎯</div>
<h4>1. 模型选择</h4>
<p style="margin: 0; opacity: 0.9;">在模型选择器中选择 SD3 Medium 模型</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; text-align: center;">
<div style="font-size: 2em; margin-bottom: 10px;">📝</div>
<h4>2. 提示词输入</h4>
<p style="margin: 0; opacity: 0.9;">输入详细的图像描述</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; text-align: center;">
<div style="font-size: 2em; margin-bottom: 10px;">⚙️</div>
<h4>3. 参数设置</h4>
<p style="margin: 0; opacity: 0.9;">调整步数、CFG 和采样器</p>
</div>

<div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 15px; text-align: center;">
<div style="font-size: 2em; margin-bottom: 10px;">🎨</div>
<h4>4. 高级设置</h4>
<p style="margin: 0; opacity: 0.9;">配置种子和批次设置</p>
</div>

</div>

</div>

---

## ⚙️ 参数说明

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h3 style="color: #6c5ce7; margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">🔢</span> 核心参数
</h3>

<div style="margin-bottom: 15px;">
<h4 style="color: #333; margin: 0 0 8px 0;">Steps (推理步数)</h4>
<ul style="margin: 0; padding-left: 20px; color: #666;">
<li><strong>15-20 步:</strong> 快速生成，可接受质量</li>
<li><strong>20-30 步:</strong> 平衡质量和速度 (推荐)</li>
<li><strong>30-50 步:</strong> 最高质量，速度较慢</li>
</ul>
</div>

<div style="margin-bottom: 15px;">
<h4 style="color: #333; margin: 0 0 8px 0;">CFG Scale (引导强度)</h4>
<ul style="margin: 0; padding-left: 20px; color: #666;">
<li><strong>4.0-5.0:</strong> 自然结果，较少过拟合</li>
<li><strong>5.0-7.0:</strong> 平衡文本跟随和自然度 (推荐)</li>
<li><strong>7.0-9.0:</strong> 强文本跟随，可能过饱和</li>
</ul>
</div>

</div>

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%);">
<h3 style="color: #00b894; margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">🎛️</span> 采样器选择
</h3>

<div style="space-y: 10px;">
<div style="background: rgba(0, 184, 148, 0.1); padding: 12px; border-radius: 8px; margin-bottom: 10px;">
<strong style="color: #00b894;">DPM++ 2M:</strong> 高质量，推荐使用
</div>
<div style="background: rgba(0, 184, 148, 0.1); padding: 12px; border-radius: 8px; margin-bottom: 10px;">
<strong style="color: #00b894;">Euler:</strong> 快速稳定
</div>
<div style="background: rgba(0, 184, 148, 0.1); padding: 12px; border-radius: 8px; margin-bottom: 10px;">
<strong style="color: #00b894;">DPM++ SDE:</strong> 高质量但较慢
</div>
<div style="background: rgba(0, 184, 148, 0.1); padding: 12px; border-radius: 8px;">
<strong style="color: #00b894;">DDIM:</strong> 经典选择，结果稳定
</div>
</div>

</div>

</div>


## 💡 提示词技巧

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0;">

<div style="border: 2px solid #e17055; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%);">
<h3 style="color: #e17055; margin: 0 0 20px 0;">🎯 SD3 提示词特点</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>更好的长文本理解:</strong> 支持更详细复杂的描述</li>
<li><strong>改进的概念组合:</strong> 更好理解多概念组合</li>
<li><strong>精确属性控制:</strong> 更精确控制颜色、材质、光照等</li>
<li><strong>减少负面依赖:</strong> 对负面提示词依赖性降低</li>
</ul>
</div>

<div style="border: 2px solid #0984e3; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%);">
<h3 style="color: #0984e3; margin: 0 0 20px 0;">📝 高质量提示词结构</h3>
<div style="background: rgba(9, 132, 227, 0.1); padding: 15px; border-radius: 10px; font-family: monospace; font-size: 0.9em; color: #333;">
[详细主体描述] + [环境/背景] + [风格/技法] + [光照/氛围] + [质量词汇]
</div>
</div>

</div>

### 🎨 提示词示例

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="border-left: 5px solid #00b894; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%);">
<h4 style="color: #00b894; margin: 0 0 15px 0;">📸 写实摄影风格</h4>
<div style="background: #fff; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.85em; color: #333; line-height: 1.4;">
"一位自信的30多岁商务女性的专业头像，穿着深蓝色西装外套，坐在现代办公桌前，自然窗光，浅景深，85mm镜头拍摄，高分辨率，锐利对焦"
</div>
</div>

<div style="border-left: 5px solid #6c5ce7; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h4 style="color: #6c5ce7; margin: 0 0 15px 0;">🎨 艺术创作风格</h4>
<div style="background: #fff; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.85em; color: #333; line-height: 1.4;">
"秋天法国乡村葡萄园的印象派绘画，金色阳光透过葡萄藤过滤，暖色调色板，松散笔触，户外写生风格，让人想起莫奈的作品"
</div>
</div>

<div style="border-left: 5px solid #e17055; padding: 20px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%);">
<h4 style="color: #e17055; margin: 0 0 15px 0;">👤 角色肖像</h4>
<div style="background: #fff; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.85em; color: #333; line-height: 1.4;">
"一位年轻艺术家在工作室的详细肖像，沾满颜料的围裙，手持调色板和画笔，被画布包围，大窗户的自然光线，若有所思的表情，写实油画风格"
</div>
</div>

<div style="border-left: 5px solid #fdcb6e; padding: 20px; background: linear-gradient(135deg, #fffbf0 0%, #fff3e0 100%);">
<h4 style="color: #fdcb6e; margin: 0 0 15px 0;">🏰 奇幻角色</h4>
<div style="background: #fff; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.85em; color: #333; line-height: 1.4;">
"精灵弓箭手的奇幻角色肖像，精致的皮甲，银发编织着树叶，锐利的绿眼睛，森林背景，详细的奇幻艺术，RPG角色设计"
</div>
</div>

</div>

---

## 🔌 API 调用

<details style="border: 2px solid #0066cc; border-radius: 15px; padding: 20px; margin: 20px 0; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%);">
<summary style="font-weight: bold; font-size: 20px; color: #0066cc; cursor: pointer; display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.5em;">📋</span> 点击展开 API 调用 Python 代码
</summary>

<div style="margin-top: 20px;">

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

</div>
</details>

---

## 💡 最佳实践

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0;">

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%);">
<h3 style="color: #00b894; margin: 0 0 20px 0;">📝 提示词优化</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>详细描述:</strong> SD3 能更好理解详细描述</li>
<li><strong>自然语言:</strong> 使用自然句式而非关键词堆叠</li>
<li><strong>具体属性:</strong> 明确指定颜色、材质、光照等属性</li>
<li><strong>风格指导:</strong> 清楚指定艺术或技术风格</li>
<li><strong>减少负面:</strong> 专注正面描述，减少负面提示词使用</li>
</ul>
</div>

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h3 style="color: #6c5ce7; margin: 0 0 20px 0;">⚙️ 参数调优策略</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>起始设置:</strong> 25步 + CFG 6.0 + DPM++ 2M</li>
<li><strong>快速预览:</strong> 20步 + CFG 5.0 用于快速测试</li>
<li><strong>高质量:</strong> 30步 + CFG 6.5 获得最佳效果</li>
<li><strong>风格实验:</strong> 在4.5-7.0范围内调整CFG测试</li>
</ul>
</div>

</div>

---

## 📊 模型对比

<div style="overflow-x: auto; margin: 30px 0;">

<table style="width: 100%; border-collapse: collapse; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 15px; overflow: hidden;">
<thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
<tr>
<th style="padding: 20px; text-align: left; font-size: 1.1em;">对比项目</th>
<th style="padding: 20px; text-align: center; font-size: 1.1em;">SD3 Medium</th>
<th style="padding: 20px; text-align: center; font-size: 1.1em;">SD1.5</th>
<th style="padding: 20px; text-align: center; font-size: 1.1em;">Flux1-Dev</th>
<th style="padding: 20px; text-align: center; font-size: 1.1em;">SDXL</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; font-weight: bold;">📊 参数规模</td>
<td style="padding: 15px; text-align: center; color: #00b894;">2B</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">0.86B</td>
<td style="padding: 15px; text-align: center; color: #e17055;">12B</td>
<td style="padding: 15px; text-align: center; color: #6c5ce7;">3.5B</td>
</tr>
<tr>
<td style="padding: 15px; font-weight: bold;">🎨 图像质量</td>
<td style="padding: 15px; text-align: center; color: #00b894;">优秀</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">良好</td>
<td style="padding: 15px; text-align: center; color: #e17055;">卓越</td>
<td style="padding: 15px; text-align: center; color: #6c5ce7;">优秀</td>
</tr>
<tr style="background: #f8f9fa;">
<td style="padding: 15px; font-weight: bold;">💾 显存需求</td>
<td style="padding: 15px; text-align: center; color: #00b894;">8GB+</td>
<td style="padding: 15px; text-align: center; color: #00b894;">4GB+</td>
<td style="padding: 15px; text-align: center; color: #e17055;">12GB+</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">6GB+</td>
</tr>
<tr>
<td style="padding: 15px; font-weight: bold;">⚡ 生成速度</td>
<td style="padding: 15px; text-align: center; color: #00b894;">快速</td>
<td style="padding: 15px; text-align: center; color: #00b894;">很快</td>
<td style="padding: 15px; text-align: center; color: #fdcb6e;">中等</td>
<td style="padding: 15px; text-align: center; color: #6c5ce7;">快速</td>
</tr>
</tbody>
</table>

</div>

---

## 🔧 常见问题与解决方案

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin: 30px 0;">

<div style="border: 2px solid #e17055; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%);">
<h3 style="color: #e17055; margin: 0 0 20px 0;">🎨 生成质量问题</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>CFG 过高:</strong> 降低 CFG 到 4.5-7.0 范围</li>
<li><strong>步数不足:</strong> 增加到 25-30 步</li>
<li><strong>提示词过简:</strong> 使用更详细的描述</li>
</ul>
</div>

<div style="border: 2px solid #fdcb6e; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #fffbf0 0%, #fff3e0 100%);">
<h3 style="color: #fdcb6e; margin: 0 0 20px 0;">⚡ 性能问题</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>显存不足:</strong> 降低分辨率或使用 medvram 模式</li>
<li><strong>加载缓慢:</strong> SD3 模型较大，需要耐心</li>
<li><strong>生成缓慢:</strong> 使用更少步数或更快采样器</li>
</ul>
</div>

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 25px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%);">
<h3 style="color: #6c5ce7; margin: 0 0 20px 0;">🔧 兼容性问题</h3>
<ul style="color: #666; line-height: 1.6;">
<li><strong>WebUI 版本:</strong> 确保使用支持 SD3 的最新版本</li>
<li><strong>扩展兼容:</strong> 某些扩展可能与 SD3 不兼容</li>
<li><strong>参数范围:</strong> 注意 SD3 的推荐参数范围</li>
</ul>
</div>

</div>

---

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="border: 2px solid #0984e3; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8fbff 0%, #e3f2fd 100%); text-align: center;">
<div style="font-size: 2em; margin-bottom: 15px;">📄</div>
<h3 style="color: #0984e3; margin: 10px 0;">官方论文</h3>
<a href="https://stability.ai/research/stable-diffusion-3" style="color: #0984e3; text-decoration: none; font-weight: bold;">Stable Diffusion 3 研究论文</a>
</div>

<div style="border: 2px solid #00b894; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f0fff4 0%, #e6fffa 100%); text-align: center;">
<div style="font-size: 2em; margin-bottom: 15px;">📊</div>
<h3 style="color: #00b894; margin: 10px 0;">技术报告</h3>
<a href="https://stability.ai/news/stable-diffusion-3-research-paper" style="color: #00b894; text-decoration: none; font-weight: bold;">SD3 技术报告</a>
</div>

<div style="border: 2px solid #6c5ce7; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #f8f7ff 0%, #e8e5ff 100%); text-align: center;">
<div style="font-size: 2em; margin-bottom: 15px;">🤗</div>
<h3 style="color: #6c5ce7; margin: 10px 0;">模型下载</h3>
<a href="https://huggingface.co/stabilityai/stable-diffusion-3-medium" style="color: #6c5ce7; text-decoration: none; font-weight: bold;">Hugging Face 模型页面</a>
</div>

<div style="border: 2px solid #e17055; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #fff8f5 0%, #ffe8e0 100%); text-align: center;">
<div style="font-size: 2em; margin-bottom: 15px;">📖</div>
<h3 style="color: #e17055; margin: 10px 0;">使用文档</h3>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/SD3" style="color: #e17055; text-decoration: none; font-weight: bold;">WebUI SD3 支持文档</a>
</div>

<div style="border: 2px solid #fdcb6e; border-radius: 15px; padding: 20px; background: linear-gradient(135deg, #fffbf0 0%, #fff3e0 100%); text-align: center;">
<div style="font-size: 2em; margin-bottom: 15px;">💡</div>
<h3 style="color: #fdcb6e; margin: 10px 0;">提示词指南</h3>
<a href="https://stability.ai/news/stable-diffusion-3-prompt-guide" style="color: #fdcb6e; text-decoration: none; font-weight: bold;">SD3 提示词工程指南</a>
</div>

</div>

---

<div align="center" style="margin-top: 40px;">

### 🎨 开始您的 SD3 创作之旅！

![开始创作](images/开始创作_9c49130615fc.svg)

<p style="color: #666; font-style: italic; margin-top: 20px;">
第三代扩散模型，让 AI 艺术创作更加精彩
</p>

</div>