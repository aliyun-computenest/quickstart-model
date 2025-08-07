<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🚀 GPT-OSS 开源语言模型</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">高性能轻量级AI模型，Apache 2.0许可证下的开放创新</p>
</div>

## 🎯 核心亮点

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">🏆 卓越性能</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>GPT-OSS-120B</strong>：与 OpenAI o4-mini 性能持平</li>
  <li><strong>GPT-OSS-20B</strong>：达到 OpenAI o3-mini 水准</li>
  <li><strong>推理优势</strong>：同等规模开放模型中表现最优</li>
  <li><strong>工具集成</strong>：强大的工具使用能力</li>
</ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h3 style="margin-top: 0; color: #1e40af;">💻 硬件友好</h3>
<ul style="margin: 0; padding-left: 20px;">
  <li><strong>120B模型</strong>：单个80GB GPU即可运行</li>
  <li><strong>20B模型</strong>：仅需16GB内存边缘设备</li>
  <li><strong>消费级硬件</strong>：优化部署成本</li>
  <li><strong>边缘计算</strong>：本地推理无需云端</li>
</ul>
</div>

</div>

## 🔬 技术特色

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
<strong>🧠 先进训练技术</strong><br>
采用强化学习结合OpenAI最先进内部模型（包括o3及其他前沿系统）启发的技术进行训练，确保模型在推理和工具使用方面的卓越表现。
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📊 性能基准对比

<div style="overflow-x: auto; margin: 16px 0;">
<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <thead style="background: #f8fafc;">
    <tr>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0;">模型</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0;">对标模型</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0;">硬件需求</th>
      <th style="padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0;">许可证</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>GPT-OSS-120B</strong></td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">OpenAI o4-mini</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">单个80GB GPU</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Apache 2.0</td>
    </tr>
    <tr>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;"><strong>GPT-OSS-20B</strong></td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">OpenAI o3-mini</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">16GB内存设备</td>
      <td style="padding: 12px; border-bottom: 1px solid #f1f5f9;">Apache 2.0</td>
    </tr>
  </tbody>
</table>
</div>

</div>

## 📖 使用说明

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 快速开始</strong><br>
  在完成模型部署后，可以在计算巢服务实例概览页面看到模型的使用方式，里面提供了 API 调用示例、内网访问地址、公网访问地址、Web应用地址和 ApiKey。
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
  <div style="text-align: center; margin-bottom: 16px;">
    <img src="../image-cn/img-llm-use-desc.png" alt="模型使用说明界面" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  </div>
</div>

### 🔌 API 调用方式

#### 🖥️ Curl 命令调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="text-align: center; margin-bottom: 16px;">
  <img src="../image-cn/img-api-call.png" alt="API调用示例" style="max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 参数说明</strong><br>
  • <code>${ServerIP}</code>：内网地址或公网地址中的 IP 地址<br>
  • <code>${ApiKey}</code>：页面提供的 ApiKey<br>
  • <code>${ModelName}</code>：模型名称
</div>

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

</div>

#### 🐍 Python SDK 调用

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚙️ 配置说明</strong><br>
  • <code>${ApiKey}</code>：填写页面上的 ApiKey<br>
  • <code>${ServerUrl}</code>：填写页面上的公网地址或内网地址，需要带上 <code>/v1</code>
</div>

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

</div>

### 🌐 Web 应用访问

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

#### 📱 访问步骤

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">🔗 步骤一：获取访问链接</h4>
<p style="margin: 0;">在服务实例概览页面中，点击 Web 应用对应的链接，即可直接进行模型服务 Web 访问。</p>
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #059669;">💬 步骤二：开始对话</h4>
<p style="margin: 0;">在模型服务 Web 页面输入框中输入问题，就可以和大模型进行对话了。</p>
</div>

</div>

#### 🖼️ 界面展示

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-web.png" alt="Web应用访问入口" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 访问提示</strong><br>
  在服务实例概览页面中找到 Web 应用对应的链接，点击即可直接访问模型服务的 Web 界面。
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="../image-cn/img-appflow.png" alt="模型对话界面" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ 使用说明</strong><br>
  在输入框中输入您的问题或需求，系统将实时响应并提供相应的模型服务。
</div>

</div>





---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🚀 <strong>GPT-OSS系列</strong> | 开放AI的未来，触手可及的强大性能
  </p>
</div>