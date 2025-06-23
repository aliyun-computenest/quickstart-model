## Introduction
On September 19th, at the Yunqi Conference, Alibaba Cloud released Qwen2.5, the new generation of open-source models in the Tongyi Qianwen series. The flagship model, Qwen2.5-72B, outperforms Llama-405B in performance. All models in the Qwen2.5 series have been pre-trained on 18T tokens of data, showing an overall performance improvement of over 18% compared to Qwen2, with more knowledge and stronger programming and mathematical abilities. The Qwen2.5-72B model scores as high as 86.8, 88.2, and 83.1 on the MMLU-rudex benchmark (testing general knowledge), MBPP benchmark (testing coding ability), and MATH benchmark (testing mathematical ability) respectively.

Qwen2.5 supports a context length of up to 128K and can generate content up to 8K in length. The model possesses powerful multilingual capabilities, supporting over 29 languages including Chinese, English, French, Spanish, Russian, Japanese, Vietnamese, and Arabic. It can smoothly respond to diverse system prompts, enabling tasks such as role-playing and chatbot functionalities. Qwen2.5 shows notable improvements in instruction following, understanding structured data (like tables), and generating structured output (especially JSON).

In terms of language models, Qwen2.5 has open-sourced 7 sizes: 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B. Tongyi Qianwen 2.5-32B-Instruct (Qwen2.5-32B-Instruct) is a version obtained by fine-tuning Tongyi Qianwen 2.5-32B (Qwen2.5-32B) for instruction following, capable of generating text that complies with instructions based on given prompts and conversation history.

This model can be deployed directly. The directly deployed model uses Qwen2.5-32B-Instruct as the pre-trained model and can continue writing based on any text provided by the user.

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



