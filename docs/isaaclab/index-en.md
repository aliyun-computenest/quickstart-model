<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🤖 NVIDIA Isaac Lab User Guide</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Open-source Unified Framework for Robot Learning - High-Fidelity Physics Simulation and Intelligent Training Platform</p>
</div>

## 🎯 Product Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**NVIDIA Isaac™ Lab** is an open-source unified framework specifically designed for robot learning, dedicated to helping developers efficiently train robot policies.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔧 Core Technology Stack</strong><br>
  <div style="margin-top: 8px;">
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px; margin-right: 8px;">NVIDIA Isaac Sim™</span>
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px; margin-right: 8px;">NVIDIA PhysX®</span>
    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 12px;">NVIDIA RTX™ Rendering</span>
  </div>
</div>

### ✨ Core Advantages

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
    <strong>🎯 High-Fidelity Simulation</strong><br>
    Physics-based RTX rendering providing realistic physical environments
  </div>

  <div style="background: #fef3c7; border-left: 4px solid #d97706; padding: 16px; border-radius: 4px;">
    <strong>🔗 Seamless Integration</strong><br>
    Bridging the gap between high-fidelity simulation and perception-based training
  </div>

  <div style="background: #ede9fe; border-left: 4px solid #7c3aed; padding: 16px; border-radius: 4px;">
    <strong>⚡ Efficient Development</strong><br>
    Helping researchers build robot applications faster
  </div>
</div>

</div>

## 🚀 Usage Instructions

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>📋 After Deployment</strong><br>
  View model usage methods on the Computing Nest service instance overview page. The server IP is the public IP of the corresponding ECS instance, supporting remote client access connections.
</div>

![img_1.png](img_1.png)

### 🎮 Method 1: Omniverse Streaming Client Graphical Development

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Isaac Lab service automatically starts Isaac Sim upon launch. You can remotely connect to Isaac Sim through Omniverse Streaming Client and use the graphical interface for rapid development and debugging.

#### 📥 Step 1: Download and Install Streaming Client

<details style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0; background: #fafafa;">
<summary style="font-weight: bold; color: #1e40af; cursor: pointer;">💻 System Requirements and Preparation</summary>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Hardware Requirements</strong><br>
  Requires a Windows computer with GPU and GPU Grid driver installation
</div>

<div style="background: #dbeafe; border-left: 4px solid #3b82f6; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>☁️ Cloud Solution</strong><br>
  If you don't have a Windows GPU device, you can purchase a GPU-enabled Windows cloud computer through Alibaba Cloud Wuying service<br>
  <strong>Minimum Configuration:</strong> 4 vCPU / 10 GiB / 2GiB VRAM<br>
  <a href="https://help.aliyun.com/zh/wuying-workspace/user-guide/create-a-cloud-computer-3" style="color: #2563eb;">📖 Wuying Cloud Computer Purchase Guide</a>
</div>

</details>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">📦 Download Client</h4>
<p>Visit the <a href="https://docs.isaacsim.omniverse.nvidia.com/latest/installation/download.html#isaac-sim-latest-release" style="color: #2563eb;">Isaac Sim Official Download Page</a> and select the Windows version</p>

![img.png](img.png)

</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">🔧 Installation and Launch</h4>
<p>Extract the downloaded file, navigate to the directory, and double-click <code>omniverse-streaming-client.exe</code> to launch</p>

![img_2.png](img_2.png)
![img_3.png](img_3.png)

</div>

</div>

#### 🔗 Step 2: Connect to Isaac Sim for Development

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

##### Connection Steps

1. **Launch Connection Interface**: Open Omniverse Streaming Client
2. **Enter Server Address**: Input the Isaac Lab service instance IP address in the Server field
3. **Establish Connection**: Click the Connect button to connect to Isaac Sim

![img_4.png](img_4.png)
![img_5.png](img_5.png)

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Successful Connection Example</strong><br>
  Refer to the <a href="https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html" style="color: #059669;">Isaac Sim Getting Started Tutorial</a> to create canvas planes and cubes for basic operations
</div>

![img_6.png](img_6.png)

</div>

</div>

### 💻 Method 2: SSH Remote Python Script Training

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

Isaac Lab service is deployed through Docker images, using official standard images plus the plugin cache required for Isaac Sim startup, supporting training script execution within containers.

#### 🔧 Operation Steps

<div style="display: grid; grid-template-columns: 1fr; gap: 16px; margin: 16px 0;">

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">1️⃣ Remote Login to Server</h4>
<p>In the service instance details page resources section, click "Remote Connection" to log into the ECS server</p>

![img_7.png](img_7.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">2️⃣ Check Container Status</h4>
<p>Execute command to check isaac-lab container running status:</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">docker ps -a</code>
</div>

![img_8.png](img_8.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">3️⃣ Enter Container Environment</h4>
<p>Execute command to enter isaac-lab container:</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">docker exec -it isaac-lab bash</code>
</div>

![img_9.png](img_9.png)

</div>

<div style="background: white; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
<h4 style="margin-top: 0; color: #1e40af;">4️⃣ Execute Training Script</h4>
<p>Refer to the <a href="https://docs.robotsfan.com/isaaclab/source/deployment/docker.html" style="color: #2563eb;">official tutorial</a> and execute the example script:</p>
<div style="background: #1e293b; border-radius: 6px; padding: 12px; margin: 8px 0;">
<code style="color: #e2e8f0; font-family: 'Courier New', monospace;">./isaaclab.sh -p scripts/tutorials/00_sim/log_time.py --headless</code>
</div>

![img_10.png](img_10.png)

</div>

</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Execution Success</strong><br>
  The script executes successfully. You can also run custom training scripts for robot learning experiments
</div>

</div>

## 📚 Related Resources

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">📖 Official Documentation</h4>
<ul style="margin: 0; padding-left: 20px;">
  <li><a href="https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html" style="color: #2563eb;">Isaac Sim Quick Start</a></li>
  <li><a href="https://docs.robotsfan.com/isaaclab/source/deployment/docker.html" style="color: #2563eb;">Isaac Lab Docker Deployment Guide</a></li>
</ul>
</div>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
<h4 style="margin-top: 0; color: #1e40af;">☁️ Cloud Service Support</h4>
<ul style="margin: 0; padding-left: 20px;">
  <li><a href="https://help.aliyun.com/zh/wuying-workspace/user-guide/create-a-cloud-computer-3" style="color: #2563eb;">Alibaba Cloud Wuying Cloud Computer</a></li>
</ul>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🤖 <strong>NVIDIA Isaac Lab</strong> | Making Robot Learning Simpler and More Efficient
  </p>
</div>