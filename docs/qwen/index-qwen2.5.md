<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h1 style="margin: 0; font-size: 28px; font-weight: 600;">🚀 Qwen2.5 开源模型使用指南</h1>
  <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 16px;">阿里云通义千问新一代开源模型部署与调用文档</p>
</div>

## 📖 模型简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 🎯 核心亮点

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🏆 性能突破</div>
  <div style="color: #64748b; font-size: 14px;">Qwen2.5-72B 性能超越 Llama-405B<br>整体性能提升 18%以上</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">📊 基准测试</div>
  <div style="color: #64748b; font-size: 14px;">MMLU: 86.8 | MBPP: 88.2<br>MATH: 83.1</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">🌍 多语言支持</div>
  <div style="color: #64748b; font-size: 14px;">支持 29+ 种语言<br>包含中英法西俄日越阿等</div>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
  <div style="color: #2563eb; font-weight: 600; margin-bottom: 8px;">📝 上下文能力</div>
  <div style="color: #64748b; font-size: 14px;">128K 上下文长度<br>最多生成 8K 内容</div>
</div>

</div>

### 📋 技术规格

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔧 训练数据</strong>：18T tokens 预训练数据<br>
  <strong>🎯 核心能力</strong>：编程、数学、指令跟随、结构化数据处理<br>
  <strong>📦 模型规格</strong>：0.5B、1.5B、3B、7B、14B、32B、72B 共 7 个尺寸
</div>

</div>

## 🛠️ 使用说明

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 获取访问信息

部署完成后，在计算巢服务实例概览页面可获取以下信息：

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🔗 API 调用示例</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🏠 内网访问地址</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🌐 公网访问地址</span>
  <span style="background: #eff6ff; color: #1e40af; padding: 6px 12px; border-radius: 12px; font-size: 14px; text-align: center;">🔑 API Key</span>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-llm-use-desc.png" alt="服务实例概览页面" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">服务实例概览页面示例</p>
</div>

</div>

## 🔌 API 调用方式

### 💻 Curl 命令调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-api-call.png" alt="API 调用示例" style="max-width: 100%; border-radius: 6px; border: 1px solid #e2e8f0;">
  <p style="margin-top: 8px; color: #64748b; font-size: 14px;">API 调用界面示例</p>
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📝 参数说明</strong><br>
  • <code>${ServerIP}</code>：内网或公网地址中的 IP<br>
  • <code>${ApiKey}</code>：页面提供的 API Key<br>
  • <code>${ModelName}</code>：模型名称
</div>

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">

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

</div>

</div>

### 🐍 Python SDK 调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚙️ 配置说明</strong><br>
  • <code>${ApiKey}</code>：填写页面上的 API Key<br>
  • <code>${ServerUrl}</code>：填写公网或内网地址，需要带上 <code>/v1</code> 后缀
</div>

<div style="background: #1e293b; border-radius: 6px; padding: 16px; margin: 16px 0;">

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

</div>

</div>

## 🎯 快速开始

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### ✅ 部署检查清单

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">1️⃣ 获取访问信息</div>
  <div style="color: #64748b; font-size: 14px;">从计算巢实例页面获取<br>API Key 和访问地址</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">2️⃣ 选择调用方式</div>
  <div style="color: #64748b; font-size: 14px;">Curl 命令或 Python SDK<br>根据需求选择合适方式</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">3️⃣ 配置参数</div>
  <div style="color: #64748b; font-size: 14px;">替换示例代码中的<br>占位符变量</div>
</div>

<div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 16px;">
  <div style="color: #059669; font-weight: 600; margin-bottom: 8px;">4️⃣ 开始调用</div>
  <div style="color: #64748b; font-size: 14px;">执行代码，开始使用<br>Qwen2.5 模型服务</div>
</div>

</div>

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 提示</strong><br>
  建议先使用 Curl 命令进行快速测试，确认服务正常后再集成到应用程序中。如遇到问题，请检查网络连接和 API Key 配置。
</div>