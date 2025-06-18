## Introduction
Qwen2.5-VL is a more useful visual language model built by the Alibaba Cloud Qwen team based on Qwen2-VL, incorporating valuable feedback from numerous developers. Its main enhanced features include:

- Visual understanding of objects: Qwen2.5-VL can not only skillfully recognize common objects like flowers, birds, fish, and insects, but also analyze text, charts, icons, graphics, and layouts in images.

- Agency: Qwen2.5-VL directly plays the role of a visual agent, with the ability to reason and dynamically direct tools, applicable for both computers and mobile phones.

- Understanding long videos and capturing events: Qwen2.5-VL can understand videos over 1 hour long, and now has the new ability to capture events by precisely locating relevant video segments.

- Capable of visual localization in different formats: Qwen2.5-VL can accurately locate objects in images by generating bounding boxes or points, and can provide stable JSON output for coordinates and attributes.

- Generating structured output: For scanned data such as invoices, forms, and tables, Qwen2.5-VL supports structured output of their content, beneficial for applications in fields like finance and business.

## Usage Instructions
After completing the model deployment, you can view the model's usage methods on the Compute Nest service instance overview page. It provides API call examples, intranet access addresses, public network access addresses (available after enabling public network access), and Api_Key. The following sections will explain how to access and use these.

![img.png](../image-en/img-llm-use-desc.png)

### API Calls
#### Curl Command Call

![img.png](../image-en/img-api-call.png)

For Curl command calls, you can directly use the API call example from the service instance overview page. The specific structure for calling the model API is as follows:

${ServerIP} can be filled with the IP address from either the intranet or public network address, ${ApiKey} is the ApiKey, and ${ModelName} is the model name.

The image_url parameter can be specified using either an HTTP URL, such as https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png, or using base64 encoded image content. The example below uses base64 encoded image content.

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
                        "url": f"data:image/jpeg;base64,<base64 encoded image>"
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

#### Python Call
Here's a Python example code: Where ${ApiKey} needs to be filled with the ApiKey from the page; ${ServerUrl} needs to be filled with the public or intranet address from the page, including /v1.

```python
import base64

import requests
from openai import OpenAI

##### API Configuration #####
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
                        "text": "Answer in Chinese, what number should be in the box in the image?",
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
                    {"type": "text", "text": "Please describe the video content"},
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

### Web Application
Click on the online access link to jump to the corresponding page where you can directly access the model service online.


