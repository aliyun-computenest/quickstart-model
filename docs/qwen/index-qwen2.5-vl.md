<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="margin: 0; font-size: 28px; font-weight: 600;">👁️ Qwen2.5-VL 视觉语言模型</h1>
  <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 16px;">阿里云通义千问新一代多模态AI模型使用指南</p>
</div>

## 📖 模型简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Qwen2.5-VL 是阿里云 Qwen 团队在 Qwen2-VL 基础上结合众多开发者的宝贵反馈构建的更有用的视觉语言模型。

### 🚀 核心能力

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">👁️ 视觉理解事物</div>
  <div style="color: #64748b; font-size: 14px;">熟练识别花、鸟、鱼、昆虫等常见物体，分析图像中的文本、图表、图标、图形和布局</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🤖 智能代理性</div>
  <div style="color: #64748b; font-size: 14px;">直接扮演视觉代理角色，具有推理和动态指挥工具功能，适用于电脑和手机</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🎬 长视频理解</div>
  <div style="color: #64748b; font-size: 14px;">理解超过 1 小时的视频，通过精确定位相关视频片段来捕捉事件</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🎯 视觉定位</div>
  <div style="color: #64748b; font-size: 14px;">通过生成边界框或点准确定位图像中的对象，提供稳定的 JSON 输出</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">📊 结构化输出</div>
  <div style="color: #64748b; font-size: 14px;">支持发票、表格等扫描件数据的结构化输出，适用于金融、商业等领域</div>
</div>

</div>

</div>

## 🛠️ 使用说明

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 获取访问信息

部署完成后，在计算巢服务实例概览页面可获取以下信息：

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🔗 API 调用示例</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🏠 内网访问地址</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🌐 公网访问地址</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🔑 API Key</span>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-llm-use-desc.png" alt="服务实例概览页面" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">服务实例概览页面示例</p>
</div>

</div>

## 🔌 API 调用方式

### 💻 Curl 命令调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-api-call.png" alt="API 调用示例" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">API 调用界面示例</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📝 参数说明</strong><br>
  • <code>${ServerIP}</code>：内网或公网地址中的 IP<br>
  • <code>${ApiKey}</code>：页面提供的 API Key<br>
  • <code>${ModelName}</code>：模型名称<br>
  • <code>image_url</code>：支持 HTTP URL 或 base64 编码格式
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🖼️ 图片格式支持</strong><br>
  • HTTP URL：如 <code>https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png</code><br>
  • Base64 编码：<code>data:image/jpeg;base64,&lt;图片的 base64 编码格式&gt;</code>
</div>

```bash
curl -X Post http://${ServerIP}:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: ${ApiKey}" \
    -d '{
        "model": "${ModelName}",
        "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64,<图片的 base64 编码格式>"
                    }
                },
                {
                    "type": "text",
                    "text": "How many sheep are there in the picture?"
                }
            ]
        }
        ]
    }'
```

</div>

### 🐍 Python SDK 调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚙️ 配置说明</strong><br>
  • <code>${ApiKey}</code>：填写页面上的 API Key<br>
  • <code>${ServerUrl}</code>：填写公网或内网地址，需要带上 <code>/v1</code> 后缀
</div>

#### 📸 图片处理示例

```python
import base64
import requests
from openai import OpenAI

##### API 配置 #####
openai_api_key = "${ApiKey}"
openai_api_base = "${ServerUrl}"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id


def encode_base64_content_from_url(content_url: str) -> str:
    """Encode a content retrieved from a remote url to base64 format."""
    with requests.get(content_url) as response:
        response.raise_for_status()
        result = base64.b64encode(response.content).decode("utf-8")
    return result


def infer_image():
    image_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/QVQ/demo.png"
    stream = True
    image_base64 = encode_base64_content_from_url(image_url)

    chat_completion_from_base64 = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "使用中文回答，图中方框处应该是数字多少?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                    },
                ],
            }
        ],
        model=model,
        max_completion_tokens=1024,
        stream=stream,
    )

    if stream:
        for chunk in chat_completion_from_base64:
            print(chunk.choices[0].delta.content, end="")
    else:
        result = chat_completion_from_base64.choices[0].message.content
        print(result)
```

#### 🎬 视频处理示例

```python
def infer_video():
    video_url = "https://pai-quickstart-predeploy-hangzhou.oss-cn-hangzhou.aliyuncs.com/modelscope/algorithms/ms-swift/video_demo.mp4"
    stream = True
    video_base64 = encode_base64_content_from_url(video_url)

    chat_completion_from_base64 = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "请描述下视频内容"},
                    {
                        "type": "video_url",
                        "video_url": {"url": f"data:video/mp4;base64,{video_base64}"},
                    },
                ],
            }
        ],
        model=model,
        max_completion_tokens=512,
        stream=stream,
    )

    if stream:
        for chunk in chat_completion_from_base64:
            print(chunk.choices[0].delta.content, end="")
    else:
        result = chat_completion_from_base64.choices[0].message.content
        print(result)


if __name__ == "__main__":
    infer_image()
    infer_video()
```

</div>

## 🎯 应用场景

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">💼 商业文档</div>
  <div style="color: #64748b; font-size: 14px;">发票识别、表格提取<br>财务数据结构化处理</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🎥 视频分析</div>
  <div style="color: #64748b; font-size: 14px;">长视频内容理解<br>事件检测与定位</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🤖 智能助手</div>
  <div style="color: #64748b; font-size: 14px;">视觉代理应用<br>多模态交互体验</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🔍 目标检测</div>
  <div style="color: #64748b; font-size: 14px;">精确对象定位<br>边界框生成</div>
</div>

</div>

</div>

## 🚀 快速开始

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### ✅ 部署检查清单

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">1️⃣ 获取访问信息</div>
  <div style="color: #64748b; font-size: 14px;">从计算巢实例页面获取<br>API Key 和访问地址</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">2️⃣ 准备多媒体内容</div>
  <div style="color: #64748b; font-size: 14px;">图片或视频文件<br>支持 URL 或 base64 格式</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">3️⃣ 选择调用方式</div>
  <div style="color: #64748b; font-size: 14px;">Curl 命令或 Python SDK<br>根据需求选择合适方式</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">4️⃣ 开始调用</div>
  <div style="color: #64748b; font-size: 14px;">执行代码，体验<br>多模态AI能力</div>
</div>

</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 提示</strong><br>
  Qwen2.5-VL 支持图片和视频两种输入格式，建议先从简单的图片识别开始测试，确认服务正常后再尝试视频分析功能。视频处理可能需要更长的响应时间。
</div>