## Introduction
DeepSeek-V3 is a powerful Mixture of Experts (MoE) language model with a total of 671 billion parameters, of which 37 billion are activated for each token. To achieve efficient inference and economical training costs, DeepSeek-V3 employs Multi-head Latent Attention (MLA) and the DeepSeekMoE architecture, both thoroughly validated in DeepSeek-V2. Additionally, DeepSeek-V3 pioneers a load balancing strategy without auxiliary loss and sets a multi-token prediction training objective to enhance performance. DeepSeek pre-trained DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by supervised fine-tuning and reinforcement learning phases to fully unleash its capabilities. Comprehensive evaluations indicate that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Moreover, DeepSeek-V3 requires only 2.788 million H800 GPU hours to complete the entire training process. Furthermore, its training process is remarkably stable. Throughout the entire training, no unrecoverable loss spikes were encountered, and no rollback operations were necessary.

## Usage Instructions
After completing the model deployment, you can view the usage methods on the service instance overview page in Compute Nest. It provides API call examples, intranet access addresses, public network access addresses, and ApiKey. The following sections will explain how to access and use these.

![img-llm-use-desc.png](../image-en/img-llm-use-desc.png)

### API Calls
#### Curl Command Call

![img.png](../image-en/img-api-call.png)

You can directly use the API call example from the service instance overview page for Curl command calls. The specific structure for calling the model API is as follows:

Where ${ServerIP} can be filled with the IP address from either the intranet or public network address, ${ApiKey} is the ApiKey, and ${ModelName} is the model name.
```shell
curl -X Post http://${ServerIP}:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ApiKey}" \
  -d '{
    "model": "${ModelName}",
    "messages": [
      {
        "role": "user",
        "content": "Write a letter to my daughter from the future 2035, telling her to study technology well, be the master of technology, and promote technological and economic development; she is currently in 3rd grade"
      }
    ]
  }'
```

#### Python Call
Here's a Python example code: Where ${ApiKey} needs to be filled with the ApiKey from the page; ${ServerUrl} needs to be filled with the public or intranet address from the page, including /v1.
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
                        "text": "Hello, introduce yourself, the more detailed the better.",
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
