<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🌌 Cosmos-Reason1 多模态推理模型</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">可完全定制的多模态 AI 推理专家 - 理解运动与时空关系</p>
</div>

## 🎯 产品简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Cosmos-Reason1 是一款可完全定制的多模态 AI 推理模型，它专门为理解运动、物体交互以及时空关系而构建。基于思维链（Chain-of-thought, CoT）推理，Cosmos-Reason1 模型可以解读视觉输入、根据给定的提示词预测结果、并奖励最佳决策。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔬 核心创新</strong><br>
  该模型基于真实世界的物理规律实现推理，从而生成清晰且能够感知上下文环境的自然语言回复，为多模态 AI 推理树立了新标杆。
</div>

</div>

## ✨ 核心特性

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
  <strong>🎬 运动理解专家</strong><br>
  专门为理解运动、物体交互以及时空关系而构建，能够精确分析动态场景中的复杂物理现象。
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
  <strong>🧠 思维链推理</strong><br>
  基于思维链（Chain-of-thought, CoT）推理，可以解读视觉输入、根据给定的提示词预测结果、并奖励最佳决策。
</div>

<div style="background: #fef7ff; border-left: 4px solid #a855f7; padding: 16px; border-radius: 4px;">
  <strong>⚖️ 物理规律推理</strong><br>
  基于真实世界的物理规律实现推理，生成清晰且能够感知上下文环境的自然语言回复。
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
  <strong>🔧 完全可定制</strong><br>
  可完全定制的架构设计，支持针对特定应用场景进行深度优化和个性化调整。
</div>

<div style="background: #ecfdf5; border-left: 4px solid #10b981; padding: 16px; border-radius: 4px;">
  <strong>📊 数据增强能力</strong><br>
  能够通过充当判别器或对海量视觉数据进行标注，从而增强合成数据策管能力。
</div>

</div>


## 🚀 应用场景

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
  <strong>🤖 机器人控制</strong><br>
  <div style="margin-top: 8px; color: #1e3a8a;">
    • 具身智能导航<br>
    • 物体操作规划<br>
    • 环境交互理解<br>
    • 动作序列优化
  </div>
</div>

<div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
  <strong>🎮 游戏 AI</strong><br>
  <div style="margin-top: 8px; color: #065f46;">
    • 物理引擎优化<br>
    • 智能 NPC 行为<br>
    • 场景交互设计<br>
    • 动态事件预测
  </div>
</div>

<div style="background: #fef7ff; border-left: 4px solid #a855f7; padding: 16px; border-radius: 4px;">
  <strong>🎬 视频分析</strong><br>
  <div style="margin-top: 8px; color: #6b21a8;">
    • 动作识别分类<br>
    • 事件检测定位<br>
    • 行为预测分析<br>
    • 内容理解标注
  </div>
</div>

<div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; border-radius: 4px;">
  <strong>🔬 科学研究</strong><br>
  <div style="margin-top: 8px; color: #92400e;">
    • 物理实验分析<br>
    • 现象机理解释<br>
    • 数据模式发现<br>
    • 假设验证支持
  </div>
</div>

</div>


## 使用说明
在完成模型部署后，可以在计算巢服务实例概览页面看到模型的使用方式，里面提供了Api调用示例、内网访问地址、公网访问地址（开启公网访问后会有）和Api_Key，下面会分别介绍如何访问使用。

![img.png](../image-cn/img-llm-use-desc.png)

### API调用
#### Curl命令调用

![img.png](../image-cn/img-api-call.png)

Curl命令调用可以直接使用服务实例概览页面中的Api调用示例，调用模型API的具体结构如下：

${ServerIP}可以填写内网地址或公网地址中的IP地址，${ApiKey}为ApiKey，${ModelName}为模型名称。

其中的image_url参数既可以使用http url进行指定，如https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png，也可以使用base64编码格式的图片内容，下面示例中使用了base64编码格式的图片内容。
```shell
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
                        "url": f"data:image/jpeg;base64,<图片的 base64 编码格式>"
                    },
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

#### Python调用
以下为 Python 示例代码： 其中${ApiKey}需要填写页面上的ApiKey；${ServerUrl}需要填写页面上的公网地址或内网地址，需要带上/v1。
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

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🌌 <strong>Cosmos-Reason1</strong> | 多模态推理专家，理解运动与时空的 AI 先锋
  </p>
</div>
