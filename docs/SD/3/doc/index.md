# Stable Diffusion 3 Medium 文生图模型部署指南

## 模型简介

Stable Diffusion 3 Medium 是 Stability AI 发布的第三代扩散模型的中等参数版本，代表了开源图像生成技术的重大进步。该模型在保持相对较低硬件要求的同时，显著提升了图像质量、文本理解能力和生成的多样性，是SD1.5和高端模型之间的完美平衡选择。

### 核心特性
- **先进架构**: 基于多模态扩散变换器（MMDiT）架构
- **强化文本理解**: 集成T5-XXL和双CLIP文本编码器
- **平衡性能**: 20亿参数，在质量和效率间取得最佳平衡
- **多宽高比支持**: 原生支持多种分辨率和宽高比
- **改进的人体解剖**: 显著减少手部和人体结构错误
- **更好的文字渲染**: 改善了图像中文字的生成质量
- **风格多样性**: 支持从写实到艺术的各种风格

### 技术规格
- **模型类型**: 文本到图像生成（Text-to-Image）
- **架构**: 多模态扩散变换器（MMDiT）
- **参数规模**: 约20亿参数
- **文本编码器**: T5-XXL + CLIP-L + CLIP-G
- **VAE**: 改进的变分自编码器
- **原生分辨率**: 1024×1024
- **支持分辨率**: 512×512 到 2048×2048
- **推荐步数**: 20-50步
- **CFG范围**: 4.5-9.0


## 配置说明

#### 系统要求
- **ECS的显存**: 8GB以上推荐（

#### 模型文件
- **主模型**: `sd3_medium_incl_clips_t5xxlfp16.safetensors` (约10GB)
- **文本编码器**: 集成在主模型中
    - T5-XXL (FP16)
    - CLIP-L
    - CLIP-G
- **VAE**: 内置改进版VAE


## 使用指南

### Web UI 使用

#### 基础操作
1. **模型选择**: 在模型选择器中选择SD3 Medium模型
2. **提示词输入**:
    - **正向提示词**: 详细描述想要生成的图像，支持更复杂的描述
    - **负向提示词**: SD3对负向提示词响应较弱，可以简化使用
3. **参数设置**:
    - **步数**: 推荐20-30步
    - **CFG Scale**: 推荐4.5-7.0（比SD1.5更低）
    - **采样器**: 推荐DPM++ 2M或Euler
    - **分辨率**: 1024×1024（原生）或其他支持尺寸
4. **高级设置**:
    - **种子**: 控制随机性
    - **批次设置**: 根据显存情况调整
    - **多宽高比**: 利用原生多分辨率支持


## 参数说明

### 核心参数
- **steps**: 推理步数
    - 15-20步: 快速生成，质量尚可
    - 20-30步: 平衡质量和速度（推荐）
    - 30-50步: 最高质量，速度较慢
- **cfg_scale**: CFG引导强度
    - 4.0-5.0: 自然结果，较少过拟合
    - 5.0-7.0: 平衡文本遵循和自然度（推荐）
    - 7.0-9.0: 强文本遵循，可能过度饱和
- **sampler**: 采样器选择
    - **DPM++ 2M**: 高质量，推荐
    - **Euler**: 快速稳定
    - **DPM++ SDE**: 高质量但较慢
    - **DDIM**: 经典选择，效果稳定

### 分辨率设置
SD3原生支持多种分辨率：
- **1024×1024**: 标准正方形
- **1152×896**: 横向4:3.6
- **896×1152**: 纵向3.6:4
- **1216×832**: 宽屏横向
- **832×1216**: 高屏纵向
- **1344×768**: 超宽屏
- **768×1344**: 超高屏

### SD3特有参数
- **较低CFG**: SD3在4.5-7.0范围内效果最佳
- **更少步数**: 20-25步通常足够获得好结果
- **原生多分辨率**: 无需高分辨率修复即可生成大图

## 提示词技巧

### SD3提示词特点
1. **更好的长文本理解**: 支持更详细和复杂的描述
2. **改进的概念组合**: 能更好地理解多个概念的组合
3. **精确的属性控制**: 对颜色、材质、光照等属性控制更精确
4. **减少负向依赖**: 对负向提示词的依赖性降低

### 高质量提示词结构
```
[详细主体描述] + [环境/背景] + [风格/技术] + [光照/氛围] + [质量词]
```

### 提示词示例

#### 写实摄影风格
```python
photography_prompts = [
    """A professional headshot of a confident businesswoman in her 30s, 
    wearing a navy blue blazer, sitting at a modern office desk, 
    natural window lighting, shallow depth of field, 
    shot with 85mm lens, high resolution, sharp focus""",
    
    """Street photography of a bustling Tokyo intersection at night, 
    neon signs, people crossing, motion blur on vehicles, 
    rain-soaked streets reflecting lights, urban atmosphere, 
    documentary style, Leica camera aesthetic"""
]
```

#### 艺术创作风格
```python
art_prompts = [
    """An impressionist painting of a French countryside vineyard in autumn, 
    golden sunlight filtering through grape vines, warm color palette, 
    loose brushstrokes, en plein air style, reminiscent of Monet's work""",
    
    """Digital concept art of a floating island city in the clouds, 
    waterfalls cascading into the sky, flying ships, 
    fantasy architecture, dramatic lighting, 
    highly detailed, matte painting style"""
]
```

#### 人物肖像
```python
portrait_prompts = [
    """A detailed portrait of a young artist in her studio, 
    paint-stained apron, holding a palette and brush, 
    surrounded by canvases, natural lighting from large windows, 
    thoughtful expression, realistic oil painting style""",
    
    """Fantasy character portrait of an elven archer, 
    intricate leather armor, silver hair braided with leaves, 
    piercing green eyes, forest background, 
    detailed fantasy art, RPG character design"""
]
```

## API调用
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

print("正在切换模型...")
model_response = requests.post(f"{base_url}/sdapi/v1/options", json=model_data, auth=auth)
print("模型切换完成")

# 2. 生成图片
prompt = "a beautiful cat"
data = {
    "prompt": prompt,
    "steps": 20,
    "width": 512,
    "height": 512
}

print("正在生成图片...")
response = requests.post(f"{base_url}/sdapi/v1/txt2img", json=data, auth=auth)
result = response.json()

# 3. 保存图片
if "images" in result:
    image_data = base64.b64decode(result["images"][0])
    with open("output.png", "wb") as f:
        f.write(image_data)
    print("图片已保存为 output.png")
else:
    print("错误:", result)

```
## 最佳实践

### 提示词优化
1. **详细描述**: SD3能更好地理解详细的描述
2. **自然语言**: 使用自然的句子结构而非关键词堆砌
3. **具体属性**: 明确指定颜色、材质、光照等属性
4. **风格指导**: 清楚地指定艺术风格或技术风格
5. **减少负向**: 专注于正向描述，减少负向提示词使用

### 参数调优策略
1. **起始设置**: 25步 + CFG 6.0 + DPM++ 2M
2. **快速预览**: 20步 + CFG 5.0 进行快速测试
3. **高质量**: 30步 + CFG 6.5 获得最佳效果
4. **风格实验**: 调整CFG在4.5-7.0范围内测试

## 与其他模型的比较

### vs Stable Diffusion 1.5
- **质量提升**: 显著更高的图像质量和细节
- **文本理解**: 更准确的复杂文本理解
- **解剖正确**: 更少的人体结构错误
- **资源需求**: 需要更多显存和计算资源

### vs Flux1-Dev
- **参数规模**: SD3 Medium (2B) vs Flux1-Dev (12B)
- **生成速度**: SD3相对更快
- **质量水平**: Flux在某些方面质量更高
- **硬件要求**: SD3硬件要求相对较低

### vs SDXL
- **架构先进性**: SD3使用更新的MMDiT架构
- **文本编码**: SD3集成T5-XXL，文本理解更强
- **多分辨率**: SD3原生支持更多分辨率
- **参数效率**: SD3在相似参数下效果更好

## 常见问题与解决方案

### 生成质量问题
1. **CFG过高**: 降低CFG到4.5-7.0范围
2. **步数不足**: 增加到25-30步
3. **提示词过于简单**: 使用更详细的描述

### 性能问题
1. **显存不足**: 降低分辨率或使用medvram模式
2. **加载缓慢**: SD3模型较大，需要耐心等待
3. **生成速度慢**: 使用较少步数或快速采样器

### 兼容性问题
1. **WebUI版本**: 确保使用支持SD3的最新版本
2. **扩展兼容**: 某些扩展可能不兼容SD3
3. **参数范围**: 注意SD3的推荐参数范围

## 相关资源

- [Stable Diffusion 3 官方论文](https://stability.ai/research/stable-diffusion-3)
- [SD3 技术报告](https://stability.ai/news/stable-diffusion-3-research-paper)
- [Hugging Face SD3 模型页面](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
- [WebUI SD3 支持文档](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/SD3)
- [SD3 提示词工程指南](https://stability.ai/news/stable-diffusion-3-prompt-guide)