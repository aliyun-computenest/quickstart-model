## Introduction
DeepSeek-V3 is a powerful Mixture of Experts (MoE) language model with a total of 671 billion parameters, of which 37 billion are activated for each token. To achieve efficient inference and economical training costs, DeepSeek-V3 employs Multi-head Latent Attention (MLA) and the DeepSeekMoE architecture, both thoroughly validated in DeepSeek-V2. Additionally, DeepSeek-V3 pioneers a load balancing strategy without auxiliary loss and sets a multi-token prediction training objective to enhance performance. DeepSeek pre-trained DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by supervised fine-tuning and reinforcement learning phases to fully unleash its capabilities. Comprehensive evaluations indicate that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Moreover, DeepSeek-V3 requires only 2.788 million H800 GPU hours to complete the entire training process. Furthermore, its training process is remarkably stable. Throughout the entire training, no unrecoverable loss spikes were encountered, and no rollback operations were necessary.

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
