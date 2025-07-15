<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎤 RVC声音克隆技术指南</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">基于深度学习的专业声音合成与变声解决方案</p>
</div>

## 🔬 技术简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**RVC声音克隆技术**（Retrieval-based-Voice-Conversion-WebUI）是一种基于深度学习的声音合成技术。其核心原理在于通过深度学习模型训练，将输入的语音样本与目标说话者的语音特征进行学习和匹配。随后，利用这个模型对新的文本进行语音合成，使得合成的语音听起来就像目标说话者一样。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 工作流程</strong><br>
  语音样本训练 → 特征学习匹配 → 模型生成 → 新音频推理 → 声音克隆完成
</div>

</div>

## 🚀 快速开始

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 访问服务

在完成模型部署后，可以在计算巢服务实例概览页面看到模型的使用方式，这里的公网地址打开就是对应的Web页面。

<div style="text-align: center; margin: 16px 0;">
  <img src="img.png" alt="服务实例概览" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 使用流程</strong><br>
  RVC的使用要先用准备好的语音样本进行训练，训练获取对应的模型后，再对待处理音频进行推理，就可以将待处理音频转换为训练所用的语声，达到变声的效果。
</div>

</div>

## 🎓 训练教程

### 步骤 1：进入训练页面

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

点击服务实例详情中的公网地址，即可进入到RVC Web页面，首先进到训练页面。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_5.png" alt="RVC训练页面" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### 步骤 2：配置训练参数

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

进行训练相关的配置，主要要设置实验名称，训练文件夹，注意这里的文件夹为容器Pod里对应的目录。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_6.png" alt="训练配置" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 重要提示</strong><br>
  文件夹路径必须指向容器Pod内的实际目录，确保路径正确性
</div>

</div>

### 步骤 3：上传语音样本

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

将要训练的语音样本上传到设置的训练文件夹中：

#### 3.1 连接到容器Pod
在计算巢服务实例中，点击《资源》→《容器Pod资源》，找到rvc对应的Pod，点击《远程连接》。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_7.png" alt="Pod连接" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 3.2 创建训练目录
在Pod内部/workspace/rvc-git目录下创建train目录，作为训练文件夹。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_8.png" alt="创建目录" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 3.3 上传语音文件
通过文件树界面上传准备好的语音样本到train目录。

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="text-align: center;">
    <img src="img_9.png" alt="文件上传1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align: center;">
    <img src="img_10.png" alt="文件上传2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

<div style="text-align: center; margin: 16px 0;">
  <img src="img_11.png" alt="文件上传3" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### 步骤 4：数据处理

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

语音样本上传完成后，点击《处理数据》进行数据处理，输出信息会提示处理进度。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_12.png" alt="数据处理" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### 步骤 5：特征提取

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

点击《特征提取》进行特征提取，输出信息会提示特征提取进度。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_13.png" alt="特征提取" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### 步骤 6：模型训练

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

点击《训练模型》进行模型训练。

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 注意事项</strong><br>
  这里会提示Error，但实际上是误报，训练还是在正常进行。训练进度可以在Pod中执行 <code>tail -f /var/logs/app.log</code> 命令查看。
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="text-align: center;">
    <img src="img_15.png" alt="模型训练" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align: center;">
    <img src="img_16.png" alt="训练进度" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

</div>

### 步骤 7：构建特征索引

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

训练完成后，点击《训练特征索引》，看到成功构建索引，就是训练成功了。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_17.png" alt="特征索引" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ 训练完成</strong><br>
  成功构建索引表示模型训练完成，可以进行推理操作
</div>

</div>

## 🎯 推理教程

训练完成后，我们就可以对我们想要变声的语音进行推理了：

### 步骤 1：加载训练模型

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

RVC web页面回到模型推理页面，点击《刷新音色列表和索引路径》，去加载刚才训练完成的模型。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_18.png" alt="加载模型" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### 步骤 2：配置推理参数

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

选择我们刚训练好的模型，设置待处理音频文件路径。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_20.png" alt="推理配置" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 路径设置说明</strong><br>
  • <strong>单次推理</strong>：路径要到具体文件名称<br>
  • <strong>批量推理</strong>：设置到目录即可<br>
  • 文件需要先上传到Pod容器中（参考训练步骤3）
</div>

</div>

### 步骤 3：执行声音转换

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

点击转换，开始将待处理的音频进行变声，变声完成后，输出音频可以直接播放或下载。

<div style="text-align: center; margin: 16px 0;">
  <img src="img_21.png" alt="声音转换" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 注意事项</strong><br>
  转换过程可能会失败，失败后重试即可。建议在网络稳定的环境下进行操作。
</div>

</div>

## 📋 操作要点总结

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #059669;">✅ 成功要素</h3>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>高质量语音样本</strong>：清晰、无噪音</li>
  <li><strong>充足的训练数据</strong>：建议10-30分钟音频</li>
  <li><strong>正确的路径配置</strong>：确保文件路径准确</li>
  <li><strong>耐心等待训练</strong>：训练时间较长属正常</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #dc2626;">❌ 常见问题</h3>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>文件路径错误导致找不到文件</li>
  <li>语音样本质量差影响效果</li>
  <li>训练时间不足模型未收敛</li>
  <li>网络不稳定导致操作失败</li>
</ul>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎤 <strong>RVC声音克隆技术</strong> | 让每个声音都能被完美复制
  </p>
</div>
