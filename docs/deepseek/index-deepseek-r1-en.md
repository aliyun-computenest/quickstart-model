## Introduction
DeepSeek-R1 is a large language model (LLM) developed by Hangzhou DeepSeek Company, specifically optimized for tasks such as mathematics, coding, and logical reasoning. It employs advanced technologies like Mixture of Experts (MoE) and Multi-head Latent Attention (MLA), boasting 671 billion parameters and supporting input contexts of up to 128,000 tokens. DeepSeek-R1 aims to match or surpass the performance of OpenAI's o1 model in reasoning tasks.

- **Strong Reasoning Ability**: DeepSeek-R1 excels in tasks such as mathematics, code generation, and natural language reasoning, even surpassing similar models.

- **MoE Architecture**: Utilizes a Mixture of Experts model, employing numerous experts in each layer to process different inputs, thereby enhancing reasoning capabilities.

- **Long Context Support**: Can handle longer input contexts (128,000 tokens), which is crucial for complex reasoning tasks.

- **Fully Open Source**: DeepSeek Company has completely open-sourced DeepSeek-R1's training techniques and model weights, allowing developers to conduct further exploration and research.

- **Open Source Distilled Models**: DeepSeek R1 has generated six smaller models (such as Qwen2.5 and Llama3.1) for community use through distillation technology.


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