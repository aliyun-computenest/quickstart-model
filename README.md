# QuickStart Model

## 简介
这是计算巢模型市场上模型对应文档仓库，由于vllm部署方式下不同模型的使用说明都是类似的，
因此将大语言模型和多模态大语言模型的使用说明抽成了公共模块，并可以通过generate_md.py
进行模型介绍Markdown文档的动态生成。

## generate_md.py使用说明
在使用generate_md.py前需要安装好python和jinjia2组件，可以使用下面的命令进行安装：
```shell
pip install Jinja2
```
执行python generate_md.py命令时，会将./docs目录下所有以.j2为结尾的jinjia文件进行渲染，并将渲染结果输出
到对应的Markdown文件中，实现模块化配置Markdown文件的效果。

这里以./docs/qwen/index-qwen3.md的生成为例，在index-qwen3.md.j2中定义好jinjia2模版
内容，里面会引用./docs/template/llm-instructions.md大语言使用说明文档，然后通过python
脚本进行渲染，并将渲染后的模版写入到./docs/qwen/index-qwen3.md文件中。
```
## 简介
Qwen3 是 Qwen 系列最新一代的大语言模型，提供了一系列密集（Dense）和混合专家(MOE）模型。基于广泛的训练，Qwen3 在推理、指令跟随、代理能力和多语言支持方面取得了突破性的进展，具有以下关键特性：

- 独特支持在思考模式（用于复杂逻辑推理、数学和编码）和 非思考模式（用于高效通用对话）之间无缝切换，确保在各种场景下的最佳性能。
- 显著增强的推理能力，在数学、代码生成和常识逻辑推理方面超越了之前的 QwQ （在思考模式下）和 Qwen2.5 指令模型（在非思考模式下）。
- 卓越的人类偏好对齐，在创意写作、角色扮演、多轮对话和指令跟随方面表现出色，提供更自然、更吸引人和更具沉浸感的对话体验。
- 擅长 Agent 能力，可以在思考和非思考模式下精确集成外部工具，在复杂的基于代理的任务中在开源模型中表现领先。
- 支持 100 多种语言和方言，具有强大的多语言理解、推理、指令跟随和生成能力。

{% include './docs/template/llm-instructions.md' %}

```