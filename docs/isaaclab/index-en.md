<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🤖 NVIDIA Isaac Lab User Guide</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Complete Tutorial for Isaac Sim-based Unified Robotics Learning Framework</p>
</div>

## 🎯 Product Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**NVIDIA Isaac™ Lab** is an open-source unified framework for robotics learning, designed to help train robot policies.

Isaac Lab is built on **NVIDIA Isaac Sim™**, utilizing **NVIDIA® PhysX®** and physics-based **NVIDIA RTX™** rendering to provide high-fidelity physics simulation. It bridges the gap between high-fidelity simulation and perception-based robot training, helping developers and researchers build more robots more efficiently.

</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 Core Features</strong><br>
  Isaac Lab service instances come with a complete Isaac Sim application built-in, supporting two training modes: standalone Isaac Sim simulation training and reinforcement learning training based on the Isaac Lab framework.
</div>

## 🖥️ Environment Access Configuration

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
<h3 style="margin-top: 0; color: #1e40af;">💻 System Environment</h3>

The corresponding ECS instance is installed with Ubuntu graphical interface, supporting direct use through VNC in the ECS console.

</div>

### 🔗 Accessing ECS Instance via VNC

<div style="display: grid; grid-template-columns: 1fr; gap: 16px; margin: 16px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">Step 1: Enter ECS Console</h4>
<p>In the resources section of the service instance details page, find the corresponding ECS instance and click to go to the ECS console.</p>

![img_17.png](img_17.png)

</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">Step 2: Select VNC Login</h4>
<p>Click on the remote connection in the upper right corner, select VNC login method to enter the Ubuntu system's graphical interface.</p>

![img_18.png](img_18.png)

</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
<h4 style="margin-top: 0; color: #1e40af;">Step 3: Enter Login Password</h4>
<p>Here you need to enter the login password for the isaac-sim account. The password is the same as the ECS instance password, which can be viewed on the service instance overview page.</p>

![img_19.png](img_19.png)

</div>

</div>

## 🎮 Isaac Sim User Guide

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
<h3 style="margin-top: 0; color: #1e40af;">📁 Directory Structure</h3>

After logging into the ECS instance using the above method, open Terminal and you can see two important directories under the isaac-sim account:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>📂 isaacsim</strong><br>
    Isaac Sim installation directory, containing related startup and training scripts
  </div>
  <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; border-radius: 4px;">
    <strong>📦 isaacsim_assets</strong><br>
    Isaac Sim assets directory, pre-downloaded resources for convenient training use
  </div>
</div>

![img_21.png](img_21.png)

</div>

### 🔬 Example 1: Headless Mode Scene-based Synthetic Dataset Generation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<h4 style="margin-top: 0; color: #1e40af;">📋 Feature Description</h4>
This example demonstrates the process of generating synthetic datasets using the omni.replicator extension. The generated data will be stored offline (on disk), making it available for training deep neural networks. The example can run in Isaac Sim's Python standalone environment and utilizes Isaac Sim and Replicator to create offline synthetic datasets for training machine learning models.

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Note</strong><br>
  It is recommended to copy the official example code to the user directory for modification and use.
</div>

</div>

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff);">
<summary style="font-weight: bold; font-size: 16px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px;">
💻 Click to View Complete Execution Code
</summary>

```bash
cd /home/isaac-sim
mkdir -p isaacsim_test
cd /home/isaac-sim/isaacsim_test
mkdir -p scene_based_sdg
cp -rf /home/isaac-sim/isaacsim/standalone_examples/replicator/scene_based_sdg/* /home/isaac-sim/isaacsim_test/scene_based_sdg/

# Render synthesis
# --config specifies configuration file path with headless=true setting
# --/persistent/isaac/asset_root/default specifies 3D asset storage path
/home/isaac-sim/isaacsim/python.sh ./scene_based_sdg/scene_based_sdg.py \
  --config="/home/isaac-sim/isaacsim_test/scene_based_sdg/config/config_coco_writer.yaml" \
  --/persistent/isaac/asset_root/default="/home/isaac-sim/isaacsim_assets/Assets/Isaac/4.5"
```

</details>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Execution Results</strong><br>
  Generated results are stored in "./isaacsim_test/_out_coco", visualization effects are as follows:
</div>

![img_23.png](img_23.png)![img_22.png](img_22.png)

### 🖼️ Example 2: Using Isaac Sim in GUI Mode

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<h4 style="margin-top: 0; color: #1e40af;">🚀 Launch Command</h4>
Execute the following command in Terminal to enter Isaac Sim's GUI interface:

```bash
cd /home/isaac-sim/isaacsim
./isaac-sim.sh
```

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Notes</strong><br>
  Isaac Sim startup is relatively slow and will show a waiting window. No action is required, just wait for some time.
</div>

![img_24.png](img_24.png)

</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Operation Example</strong><br>
  Below is a cube created following the steps in the <a href="https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/quickstart_isaacsim.html" style="color: #2563eb;">Getting Started Tutorial</a>.
</div>

![img_25.png](img_25.png)

## 🧠 Isaac Lab User Guide

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">
<h3 style="margin-top: 0; color: #1e40af;">📍 Installation Location</h3>

Isaac Lab service installation directory is located at `/home/isaac-sim/IsaacLab`, containing Isaac Lab's installation directory and startup scripts.

</div>

### 🎯 Example 1: Headless Mode Agent Training

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<h4 style="margin-top: 0; color: #1e40af;">🎮 Training Task Description</h4>
This case uses the **Stable-Baselines3** reinforcement learning (RL) framework to solve the Cartpole balance control agent task.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 Training Objective</strong><br>
  Train the agent to learn how to control the cart's left and right movement to keep the pole upright.
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🔧 Technical Framework</strong><br>
  Stable-Baselines3 is a PyTorch-based reinforcement learning library that provides various stable and easy-to-use RL algorithms such as PPO, SAC, DQN, etc.
</div>

</div>

<details style="border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 20px 0; background: linear-gradient(145deg, #f8fafc, #eff6ff);">
<summary style="font-weight: bold; font-size: 16px; color: white; cursor: pointer; padding: 16px; background: linear-gradient(135deg, #2563eb, #1e40af); border-radius: 8px; margin: -20px -20px 20px -20px;">
💻 Click to View Training Code
</summary>

```bash
cd /home/isaac-sim
mkdir -p isaaclab_test
cd /home/isaac-sim/isaaclab_test
mkdir -p sb3
cp -rf /home/isaac-sim/IsaacLab/scripts/reinforcement_learning/sb3/* /home/isaac-sim/isaaclab_test/sb3/

# Start training
# --task specifies training task
# --num_envs specifies number of parallel environments
# --headless GUI-less mode
# --video generates training video
/home/isaac-sim/IsaacLab/isaaclab.sh -p ./sb3/train.py \
  --task Isaac-Cartpole-v0 \
  --num_envs 64 \
  --headless \
  --video
```

</details>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Training Results</strong><br>
  Training results are saved to <code>./logs/sb3/Isaac-Cartpole-v0</code>, visualization results are as follows:
</div>

![img_26.png](img_26.png)

### 🎨 Example 2: GUI Mode Basic Object Generation

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

<h4 style="margin-top: 0; color: #1e40af;">🚀 Launch Command</h4>
Execute the following command in Terminal to enter Isaac Lab's GUI interface:

```bash
cd /home/isaac-sim/IsaacLab
./isaaclab.sh -p scripts/tutorials/00_sim/spawn_prims.py
```

![img_27.png](img_27.png)

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🤖 <strong>NVIDIA Isaac Lab</strong> | Making Robot Learning Simpler and More Efficient
  </p>
</div>