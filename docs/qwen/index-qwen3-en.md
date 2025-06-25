## Introduction
Qwen3 is the latest generation of large language models in the Qwen series, offering a range of Dense and Mixture of Experts (MOE) models. Through extensive training, Qwen3 has made breakthrough advancements in reasoning, instruction following, agent capabilities, and multilingual support, featuring the following key characteristics:

- Unique support for seamless switching between thinking mode (for complex logical reasoning, mathematics, and coding) and non-thinking mode (for efficient general conversation), ensuring optimal performance across various scenarios.
- Significantly enhanced reasoning abilities, surpassing previous QwQ (in thinking mode) and Qwen2.5 instruction models (in non-thinking mode) in mathematics, code generation, and common sense logical reasoning.
- Excellent human preference alignment, demonstrating outstanding performance in creative writing, role-playing, multi-turn dialogues, and instruction following, providing a more natural, engaging, and immersive conversational experience.
- Proficient in Agent capabilities, able to precisely integrate external tools in both thinking and non-thinking modes, leading performance among open-source models in complex agent-based tasks.
- Support for over 100 languages and dialects, with strong multilingual understanding, reasoning, instruction following, and generation capabilities.

## Deployment Configuration
0.6B, 1.7B, 4B, 8B models require a minimum configuration of 24GB VRAM for deployment

14B model requires a minimum configuration of 48GB VRAM for deployment

30B, 32B models require a minimum configuration of 96GB VRAM for deployment

235B model requires a minimum configuration of 8* 96GB VRAM for deployment

## 📖 User Guide

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Quick Start</strong><br>
  After completing the model deployment, you can view the model usage instructions on the Computing Nest service instance overview page, which provides API call examples, internal network access addresses, public network access addresses, and ApiKey.
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
  <div style="text-align: center; margin-bottom: 16px;">
    <img src="../image-en/img-llm-use-desc.png" alt="Model usage instructions interface" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  </div>
</div>

### 🔌 API Call Methods

#### 🖥️ Curl Command Call

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin-bottom: 16px;">
  <img src="../image-en/img-api-call.png" alt="API call example" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 Parameter Description</strong><br>
  • <code>${ServerIP}</code>: IP address from internal or public network address<br>
  • <code>${ApiKey}</code>: ApiKey provided on the page<br>
  • <code>${ModelName}</code>: Model name
</div>

Curl command calls can directly use the API call examples from the service instance overview page. The specific structure for calling the model API is as follows:

```bash
curl -X Post http://${ServerIP}:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ApiKey}" \
  -d '{
    "model": "${ModelName}",
    "messages": [
      {
        "role": "user",
        "content": "Write a letter to my daughter from the future year 2035, telling her to study technology well, become the master of technology, and promote technological and economic development; she is currently in 3rd grade"
      }
    ]
  }'
```

</div>

#### 🐍 Python SDK Call

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚙️ Configuration Instructions</strong><br>
  • <code>${ApiKey}</code>: Fill in the ApiKey from the page<br>
  • <code>${ServerUrl}</code>: Fill in the public or internal network address from the page, must include <code>/v1</code>
</div>

The following is Python example code:

```python
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
                        "text": "Hello, please introduce yourself in as much detail as possible.",
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

</div>