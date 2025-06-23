## 简介
Qwen2.5-VL  是阿里云 Qwen 团队在 Qwen2-VL 基础上结合众多开发者的宝贵反馈构建的更有用的视觉语言模型。其主要增强功能有：

- **视觉理解事物**：Qwen2.5-VL不仅能够熟练识别花、鸟、鱼、昆虫等常见物体，而且还能够分析图像中的文本、图表、图标、图形和布局。

- **代理性**：Qwen2.5-VL直接扮演视觉代理的角色，具有推理和动态指挥工具的功能，可用于电脑和手机。

- **理解长视频并捕捉事件**：Qwen2.5-VL 可以理解超过 1 小时的视频，这次它还具有通过精确定位相关视频片段来捕捉事件的新功能。

- **能够进行不同格式的视觉定位**：Qwen2.5-VL 可以通过生成边界框或点来准确定位图像中的对象，并且可以为坐标和属性提供稳定的 JSON 输出。

- **生成结构化输出**：对于发票、表格、表格等扫描件数据，Qwen2.5-VL 支持其内容的结构化输出，有利于金融、商业等领域的用途。

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


