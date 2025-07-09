<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🤖 NVIDIA Isaac Lab 使用指南</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">机器人学习开源统一框架 - 高保真物理模拟与智能训练平台</p>
</div>

## 🎯 产品简介

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**NVIDIA Isaac™ Lab** 是一个专为机器人学习设计的开源统一框架，致力于帮助开发者高效训练机器人策略。

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔧 核心技术栈</strong><br>
  <div style="margin-top: 8px;">
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px; margin-right: 8px;">NVIDIA Isaac Sim™</span>
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px; margin-right: 8px;">NVIDIA PhysX®</span>
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px;">NVIDIA RTX™ 渲染</span>
  </div>
</div>

### ✨ 核心优势

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎯 高保真模拟</strong><br>
    基于物理性质的RTX渲染，提供真实的物理环境
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>🔗 无缝集成</strong><br>
    弥合高保真模拟与感知训练的技术鸿沟
  </div>

  <div style="background: #ede9fe; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>⚡ 高效开发</strong><br>
    帮助研究人员更快速构建机器人应用
  </div>
</div>

</div>

## 🚀 使用说明

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 部署完成后</strong><br>
  在计算巢服务实例概览页面查看模型使用方式，服务器IP为对应ECS实例的公网IP，支持Client远程访问连接。
</div>

![img_1.png](img_1.png)

### 🎮 使用方式一：Omniverse Streaming Client 图形化开发

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Isaac Lab服务启动时会自动启动Isaac Sim，通过Omniverse Streaming Client可以远程连接Isaac Sim，使用图形界面进行快速开发和调试。

#### 📥 第一步：下载安装Streaming Client

<details style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0; background: #fafafa;">
<summary style="font-weight: bold; color: #1e40af; cursor: pointer;">💻 系统要求与准备</summary>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ 硬件要求</strong><br>
  需要一台带GPU的Windows系统电脑，并安装GPU Grid驱动
</div>

<div style="background: #dbeafe; border-left: 4px solid #3b82f6; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>☁️ 云端解决方案</strong><br>
  如果没有Windows GPU设备，可通过阿里云无影服务购买带GPU的Windows云电脑<br>
  <strong>最低配置：</strong>4 vCPU / 10 GiB / 2GiB 显存<br>
  <a href="https://help.aliyun.com/zh/wuying-workspace/user-guide/create-a-cloud-computer-3" style="color: #2563eb;">📖 无影云电脑购买指南</a>
</div>

</details>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">📦 下载客户端</h4>
<p>访问 <a href="https://docs.isaacsim.omniverse.nvidia.com/latest/installation/download.html#isaac-sim-latest-release" style="color: #2563eb;">Isaac Sim官方下载页</a>，选择Windows版本</p>

![img.png](img.png)

</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">🔧 安装启动</h4>
<p>解压下载文件，进入目录，双击 <code>omniverse-streaming-client.exe</code> 启动</p>

![img_2.png](img_2.png)
![img_3.png](img_3.png)

</div>

</div>

#### 🔗 第二步：连接Isaac Sim进行开发

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

##### 连接步骤

1. **启动连接界面**：打开Omniverse Streaming Client
2. **输入服务器地址**：在Server字段输入Isaac Lab服务实例的IP地址
3. **建立连接**：点击Connect按钮连接Isaac Sim

![img_4.png](img_4.png)
![img_5.png](img_5.png)

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ 连接成功示例</strong><br>
  参考 <a href="https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html" style="color: #059669;">Isaac Sim入门教程</a>，可以创建画布平面和立方体进行基础操作
</div>

![img_6.png](img_6.png)

### 💻 使用方式二：SSH远程执行Python脚本训练

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Isaac Lab服务通过Docker镜像部署，使用官方标准镜像加上Isaac Sim启动所需插件cache，支持容器内执行训练脚本。

#### 🔧 操作步骤

<div style="display: grid; grid-template-columns: 1fr; gap: 16px; margin: 16px 0;">

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">1️⃣ 远程登录服务器</h4>
<p>在服务实例详情页的资源中，点击"远程连接"登录到ECS服务器</p>

![img_7.png](img_7.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">2️⃣ 查看容器状态</h4>
<p>执行命令查看isaac-lab容器运行状态：</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">docker ps -a</code>
</div>

![img_8.png](img_8.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">3️⃣ 进入容器环境</h4>
<p>执行命令进入isaac-lab容器内部：</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">docker exec -it isaac-lab bash</code>
</div>

![img_9.png](img_9.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">4️⃣ 执行训练脚本</h4>
<p>参考<a href="https://docs.robotsfan.com/isaaclab/source/deployment/docker.html" style="color: #2563eb;">官网教程</a>，执行示例脚本：</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">./isaaclab.sh -p scripts/tutorials/00_sim/log_time.py --headless</code>
</div>

![img_10.png](img_10.png)

</div>

</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ 执行成功</strong><br>
  脚本能够顺利执行，您也可以运行自定义的训练脚本进行机器人学习实验
</div>

</div>

## 📚 相关资源

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">📖 官方文档</h4>
<ul style="margin: 0; padding-left: 20px;">
  <li><a href="https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html" style="color: #2563eb;">Isaac Sim快速入门</a></li>
  <li><a href="https://docs.robotsfan.com/isaaclab/source/deployment/docker.html" style="color: #2563eb;">Isaac Lab Docker部署指南</a></li>
</ul>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">☁️ 云服务支持</h4>
<ul style="margin: 0; padding-left: 20px;">
  <li><a href="https://help.aliyun.com/zh/wuying-workspace/user-guide/create-a-cloud-computer-3" style="color: #2563eb;">阿里云无影云电脑</a></li>
</ul>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🤖 <strong>NVIDIA Isaac Lab</strong> | 让机器人学习更简单高效
  </p>
</div>