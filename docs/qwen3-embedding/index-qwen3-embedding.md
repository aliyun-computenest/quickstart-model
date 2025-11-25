## 简介
Qwen3 Embedding 模型系列是 Qwen 家族的最新专有模型，专门设计用于文本嵌入和排序任务。基于 Qwen3 系列的密集基础模型，它提供了各种大小（0.6B、4B 和 8B）的全面文本嵌入和重排序模型。该系列继承了其基础模型卓越的多语言能力、长文本理解和推理技能。Qwen3 Embedding 系列表现出了在多种文本嵌入和排序任务中的显著进步，包括文本检索、代码检索、文本分类、文本聚类和双语文本挖掘。

## 使用说明
在完成模型部署后，可以在计算巢服务实例概览页面看到模型的使用方式，里面提供了Api调用示例、内网访问地址、公网访问地址和ApiKey，下面会分别介绍如何访问使用。

![img.png](img.png)

### API调用
#### Curl命令调用

![img_1.png](img_1.png)

Curl命令调用可以直接使用服务实例概览页面中的Api调用示例，调用模型API的具体结构如下：

其中${ServerIP}可以填写内网地址或公网地址中的IP地址，${ApiKey}为ApiKey，${ModelName}为模型名称。
```shell
curl -X Post http://${ServerIP}:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ApiKey}" \
  -d '{
    "model": "${ModelName}",
    "input": [
      "中国首都是北京。",
      "美国首都是华盛顿。",
      "今天是星期五。"
    ]
  }'
```

#### Python调用
以下为 Python 示例代码： 其中${ApiKey}需要填写页面上的ApiKey；${ServerUrl}需要填写页面上的公网地址或内网地址，不需要带上/v1。
```python
import requests
import json
import math

url = '${ServerUrl}/v1/embeddings'
token = '${ApiKey}'

def cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    norm_v1 = math.sqrt(sum(x**2 for x in v1))
    norm_v2 = math.sqrt(sum(y**2 for y in v2))
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return dot_product / (norm_v1 * norm_v2)

request_body = {
    "input": [
        "中国首都是北京。",
        "美国首都是华盛顿。",
        "今天是星期五。"
    ],
    "model": "Qwen3-Embedding-8B",
    # "dimensions": 4096
}

headers = {"Authorization": token}
resp = requests.post(url=url, headers=headers, json=request_body)

embeddings_data = json.loads(resp.content.decode())["data"]

embeddings_0 = embeddings_data[0]["embedding"]
embeddings_1 = embeddings_data[1]["embedding"]
embeddings_2 = embeddings_data[2]["embedding"]

sim_0_1 = cosine_similarity(embeddings_0, embeddings_1)
sim_0_2 = cosine_similarity(embeddings_0, embeddings_2)
sim_1_2 = cosine_similarity(embeddings_1, embeddings_2)

print(f"similarity({embeddings_data[0]["index"]},{embeddings_data[1]["index"]}): {sim_0_1:.6f}")
print(f"similarity({embeddings_data[0]["index"]},{embeddings_data[2]["index"]}): {sim_0_2:.6f}")
print(f"similarity({embeddings_data[1]["index"]},{embeddings_data[2]["index"]}): {sim_1_2:.6f}")
```
