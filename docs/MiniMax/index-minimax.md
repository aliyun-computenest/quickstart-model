## 模型简介

MiniMax 大模型是由 MiniMax 公司研发的一系列先进的人工智能语言模型。MiniMax 模型在自然语言理解、文本生成、逻辑推理等方面表现出色，能够处理复杂的对话场景和多轮交互任务。

MiniMax 大模型具有以下特点：

- **强大的语言理解能力**：能够准确理解用户意图，处理复杂的语义表达
- **流畅的文本生成**：生成自然流畅、逻辑清晰的文本内容
- **多场景适配**：适用于客服对话、内容创作、智能助手等多种应用场景
- **持续优化**：基于海量数据训练，模型能力持续迭代升级

## 使用说明

**快速开始**

在完成模型部署后，可以在计算巢服务实例概览页面看到模型的使用方式，里面提供了 API 调用示例、内网访问地址、公网访问地址、Web应用地址和 ApiKey。

![模型使用说明界面](../image-cn/img-llm-use-desc.png)

### API 调用方式

#### Curl 命令调用

![API调用示例](../image-cn/img-api-call.png)

**参数说明**

- `${ServerIP}`：内网地址或公网地址中的 IP 地址
- `${ApiKey}`：页面提供的 ApiKey
- `${ModelName}`：模型名称

Curl 命令调用可以直接使用服务实例概览页面中的 API 调用示例，调用模型 API 的具体结构如下：

```bash
curl -X Post http://${ServerIP}:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ApiKey}" \
  -d '{
    "model": "${ModelName}",
    "messages": [
      {
        "role": "user",
        "content": "给闺女写一份来自未来2035的信，同时告诉她要好好学习科技，做科技的主人，推动科技，经济发展；她现在是3年级"
      }
    ]
  }'
```

#### Python SDK 调用

**配置说明**

- `${ApiKey}`：填写页面上的 ApiKey
- `${ServerUrl}`：填写页面上的公网地址或内网地址，需要带上 `/v1`

以下为 Python 示例代码：

```python
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
print(model)

def main():
    stream = True

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "你好，介绍一下你自己，越详细越好。",
                    }
                ],
            }
        ],
        model=model,
        max_completion_tokens=1024,
        stream=stream,
    )

    if stream:
        for chunk in chat_completion:
            print(chunk.choices[0].delta.content, end="")
    else:
        result = chat_completion.choices[0].message.content
        print(result)

if __name__ == "__main__":
    main()
```

### Web 应用访问

1. 在服务实例概览页面中，点击 Web 应用对应的链接。

![Web应用访问入口](../image-cn/img-web.png)

2. 在模型服务 Web 页面输入框中输入问题，即可与大模型进行对话。

![模型对话界面](../image-cn/img-appflow.png)
