<div style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 24px; border-radius: 8px; color: white; text-align: center; margin-bottom: 24px;">
  <h2 style="margin: 0; color: white;">🎤 RVC Voice Cloning Technology Guide</h2>
  <p style="margin: 8px 0 0 0; opacity: 0.9;">Professional Voice Synthesis and Conversion Solution Based on Deep Learning</p>
</div>

## 🔬 Technical Overview

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

**RVC Voice Cloning Technology** (Retrieval-based-Voice-Conversion-WebUI) is a voice synthesis technology based on deep learning. Its core principle lies in training deep learning models to learn and match the input voice samples with the target speaker's voice characteristics. Subsequently, this model is used to synthesize speech for new text, making the synthesized voice sound like the target speaker.

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>🎯 Workflow</strong><br>
  Voice Sample Training → Feature Learning & Matching → Model Generation → New Audio Inference → Voice Cloning Complete
</div>

</div>

## 🚀 Quick Start

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 16px 0;">

### 📍 Service Access

After completing model deployment, you can see the model usage instructions on the service instance overview page. The public network address opens the corresponding Web page.

<div style="text-align: center; margin: 16px 0;">
  <img src="img.png" alt="Service Instance Overview" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Usage Process</strong><br>
  RVC requires training with prepared voice samples first. After training to obtain the corresponding model, inference is performed on the audio to be processed, which can convert the target audio to the voice used in training, achieving voice conversion effects.
</div>

</div>

## 🎓 Training Tutorial

### Step 1: Enter Training Page

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Click the public network address in the service instance details to enter the RVC Web page, first go to the training page.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_5.png" alt="RVC Training Page" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### Step 2: Configure Training Parameters

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Configure training-related settings, mainly setting the experiment name and training folder. Note that the folder here refers to the corresponding directory in the container Pod.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_6.png" alt="Training Configuration" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Note</strong><br>
  The folder path must point to the actual directory within the container Pod, ensure path accuracy
</div>

</div>

### Step 3: Upload Voice Samples

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Upload the voice samples to be trained to the set training folder:

#### 3.1 Connect to Container Pod
In the service instance, click "Resources" → "Container Pod Resources", find the rvc corresponding Pod, click "Remote Connection".

<div style="text-align: center; margin: 16px 0;">
  <img src="img_7.png" alt="Pod Connection" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 3.2 Create Training Directory
Create a train directory under /workspace/rvc-git directory inside the Pod as the training folder.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_8.png" alt="Create Directory" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

#### 3.3 Upload Voice Files
Upload prepared voice samples to the train directory through the file tree interface.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="text-align: center;">
    <img src="img_9.png" alt="File Upload 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align: center;">
    <img src="img_10.png" alt="File Upload 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

<div style="text-align: center; margin: 16px 0;">
  <img src="img_11.png" alt="File Upload 3" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### Step 4: Data Processing

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

After uploading voice samples, click "Process Data" to perform data processing. The output information will show processing progress.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_12.png" alt="Data Processing" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### Step 5: Feature Extraction

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Click "Feature Extraction" to perform feature extraction. The output information will show feature extraction progress.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_13.png" alt="Feature Extraction" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### Step 6: Model Training

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Click "Train Model" to perform model training.

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Notes</strong><br>
  An Error message may appear here, but it's actually a false alarm - training is still proceeding normally. Training progress can be monitored by executing <code>tail -f /var/logs/app.log</code> command in the Pod.
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="text-align: center;">
    <img src="img_15.png" alt="Model Training" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align: center;">
    <img src="img_16.png" alt="Training Progress" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </div>
</div>

</div>

### Step 7: Build Feature Index

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

After training completion, click "Train Feature Index". When you see successful index construction, the training is complete.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_17.png" alt="Feature Index" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>✅ Training Complete</strong><br>
  Successful index construction indicates model training is complete and inference operations can be performed
</div>

</div>

## 🎯 Inference Tutorial

After training completion, we can perform inference on the voice we want to convert:

### Step 1: Load Trained Model

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Return to the model inference page on the RVC web interface, click "Refresh Voice List and Index Path" to load the just-trained model.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_18.png" alt="Load Model" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

</div>

### Step 2: Configure Inference Parameters

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Select our just-trained model and set the path for the audio file to be processed.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_20.png" alt="Inference Configuration" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>💡 Path Setting Instructions</strong><br>
  • <strong>Single Inference</strong>: Path should point to specific filename<br>
  • <strong>Batch Inference</strong>: Set to directory<br>
  • Files need to be uploaded to Pod container first (refer to training step 3)
</div>

</div>

### Step 3: Execute Voice Conversion

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">

Click convert to start voice conversion on the target audio. After conversion completion, the output audio can be played directly or downloaded.

<div style="text-align: center; margin: 16px 0;">
  <img src="img_21.png" alt="Voice Conversion" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<div style="background: #fed7aa; border-left: 4px solid #ea580c; padding: 16px; margin: 16px 0; border-radius: 4px;">
  <strong>⚠️ Important Notes</strong><br>
  The conversion process may fail, simply retry if it fails. It's recommended to operate in a stable network environment.
</div>

</div>

## 📋 Key Points Summary

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">

<div style="background: #dcfce7; border-left: 4px solid #059669; padding: 16px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #059669;">✅ Success Factors</h3>
<ul style="margin: 0; padding-left: 20px; color: #065f46;">
  <li><strong>High-quality voice samples</strong>: Clear, noise-free</li>
  <li><strong>Sufficient training data</strong>: Recommended 10-30 minutes of audio</li>
  <li><strong>Correct path configuration</strong>: Ensure file path accuracy</li>
  <li><strong>Patient training wait</strong>: Long training time is normal</li>
</ul>
</div>

<div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #dc2626;">❌ Common Issues</h3>
<ul style="margin: 0; padding-left: 20px; color: #991b1b;">
  <li>Incorrect file paths causing file not found</li>
  <li>Poor voice sample quality affecting results</li>
  <li>Insufficient training time preventing model convergence</li>
  <li>Unstable network causing operation failures</li>
</ul>
</div>

</div>

---

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎤 <strong>RVC Voice Cloning Technology</strong> | Making Every Voice Perfectly Replicable
  </p>
</div>