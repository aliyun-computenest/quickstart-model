## Introduction
On September 19th, at the Yunqi Conference, Alibaba Cloud released Qwen2.5, the new generation of open-source models in the Tongyi Qianwen series. The flagship model, Qwen2.5-72B, outperforms Llama-405B in performance. All models in the Qwen2.5 series have been pre-trained on 18T tokens of data, showing an overall performance improvement of over 18% compared to Qwen2, with more knowledge and stronger programming and mathematical abilities. The Qwen2.5-72B model scores as high as 86.8, 88.2, and 83.1 on the MMLU-rudex benchmark (testing general knowledge), MBPP benchmark (testing coding ability), and MATH benchmark (testing mathematical ability) respectively.

Qwen2.5 supports a context length of up to 128K and can generate content up to 8K in length. The model possesses powerful multilingual capabilities, supporting over 29 languages including Chinese, English, French, Spanish, Russian, Japanese, Vietnamese, and Arabic. It can smoothly respond to diverse system prompts, enabling tasks such as role-playing and chatbot functionalities. Qwen2.5 shows notable improvements in instruction following, understanding structured data (like tables), and generating structured output (especially JSON).

In terms of language models, Qwen2.5 has open-sourced 7 sizes: 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B. Tongyi Qianwen 2.5-32B-Instruct (Qwen2.5-32B-Instruct) is a version obtained by fine-tuning Tongyi Qianwen 2.5-32B (Qwen2.5-32B) for instruction following, capable of generating text that complies with instructions based on given prompts and conversation history.

This model can be deployed directly. The directly deployed model uses Qwen2.5-32B-Instruct as the pre-trained model and can continue writing based on any text provided by the user.

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



