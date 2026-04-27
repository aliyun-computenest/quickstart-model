## 模型简介

DeepSeek-V4 是由 DeepSeek 公司研发并开源的全新一代大语言模型，标志着大模型迈入百万上下文普惠时代。V4 系列在架构上进行了创新性升级，通过 Sparse MQA、Fused MoE Mega Kernel 等核心组件，实现了对超长序列计算效率的跨越式提升，并在 Agent 能力、世界知识与推理性能等方面达到顶尖水准。

DeepSeek-V4 提供 **Pro** 与 **Flash** 两个版本：

- **DeepSeek-V4-Pro**：1.6T 总参数（49B 激活），面向高质量推理与复杂 Agent 场景，性能比肩世界顶级闭源模型
- **DeepSeek-V4-Flash**：284B 总参数（13B 激活），针对速度与成本优化，适合实时交互与大规模部署

DeepSeek-V4 大模型具有以下核心特点：

- **百万字超长上下文**：标配 1M token 上下文窗口，可一次性处理整本长篇小说、完整代码仓库或大型文档集，彻底打破长文本处理的场景限制
- **世界顶级推理性能**：在数学、STEM、竞赛型代码等评测中，V4-Pro 超越所有已公开评测的开源模型，达到比肩顶级闭源模型的水平
- **强大的 Agent 能力**：作为 DeepSeek 内部员工日常使用的 Agentic Coding 模型，编码与工具调用能力优于 Sonnet 4.5，接近 Opus 4.6 非思考模式
- **思考模式切换**：支持思考/非思考模式自由切换，兼顾深度推理与快速响应两种场景需求
- **结构化输出与函数调用**：原生支持 JSON 输出、Function Calling 等特性，方便与各类业务系统、Agent 框架对接
- **创新架构与高效推理**：采用 Sparse MQA、Fused MoE Mega Kernel 等架构，长上下文场景下推理效率显著领先，并适配国产昇腾芯片

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