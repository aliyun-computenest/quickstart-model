# Qwen3 Reranker Model Usage Guide

## Introduction
The Qwen3 Embedding model series is the latest proprietary model from the Qwen family, specifically designed for text embedding and ranking tasks. Built upon the dense foundation models of the Qwen3 series, it offers comprehensive text embedding and reranking models in various sizes (0.6B, 4B, and 8B). The series inherits the exceptional multilingual capabilities, long-text understanding, and reasoning skills of its base models. The Qwen3 Embedding series represents significant advancements across multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bilingual text mining.

## Usage Instructions
After completing the model deployment, you can view the usage methods on the ComputeNest service instance overview page, which provides private network access address, public network access address, and ApiKey. The following sections will introduce how to access and use the service.

![img.png](img.png)

### API Calls

#### Python Call
Below is a Python example code:

Where `${ApiKey}` needs to be filled with the ApiKey from the page; `${ServerUrl}` needs to be filled with the public or private network address from the page, without the `/v1` suffix.

```python
import json

import requests

url = "${ServerUrl}/v1/rerank"
token = "${ApiKey}"
headers = {"Authorization": token}

prefix = '<|im_start|>system\nJudge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>\n<|im_start|>user\n'
suffix = "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"

query_template = "{prefix}<Instruct>: {instruction}\n<Query>: {query}\n"
document_template = "<Document>: {doc}{suffix}"
instruction = "Given a web search query, retrieve relevant passages that answer the query"

data = {
    "model": "Qwen3-Reranker-8B",
    "query": query_template.format(prefix=prefix, instruction=instruction, query="中国首都是哪儿?"),
    "documents": [
        document_template.format(doc="中国首都是北京。", suffix=suffix),
        document_template.format(doc="美国首都是华盛顿。", suffix=suffix),
        document_template.format(doc="今天是星期五。", suffix=suffix)
    ],
}


def main():
    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Request successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
```
