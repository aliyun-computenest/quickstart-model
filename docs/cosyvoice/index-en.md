<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 24px 0 16px 0;">
  <h3 style="margin: 0; color: #1e40af; font-size: 1.3rem;">📋 Introduction</h3>
</div>
CosyVoice is a speech synthesis service launched by Alibaba Cloud, capable of converting text into natural and smooth speech. This service supports multiple languages and dialects, meeting the needs of various scenarios such as news broadcasting, audiobook production, and intelligent customer service. By using advanced deep learning technology, CosyVoice can generate sounds that closely mimic human voices, providing users with a richer and more humanized interactive experience.

Multilingual Support
- Supported Languages: Chinese, English, Japanese, Korean, Chinese Dialects (Cantonese, Sichuanese, Shanghainese, Tianjin dialect, Wuhan dialect, etc.)
- Cross-language and Mixed-language: Supports zero-shot cross-language and code-switching scenarios for voice cloning.

Ultra-low Latency

- Bidirectional Stream Support: CosyVoice 2.0 integrates offline and streaming modeling technologies.
- Fast First Packet Synthesis: Achieves a latency as low as 150 milliseconds while maintaining high-quality audio output.

High Accuracy
- Improved Pronunciation: Compared to CosyVoice 1.0, it reduces pronunciation errors by 30% to 50%.
- Benchmark Achievements: Achieved the lowest character error rate on the Seed-TTS evaluation set's challenging test set.

Strong Stability

- Voice Consistency: Ensures reliable voice consistency in zero-shot and cross-language speech synthesis.
- Cross-language Synthesis: Significantly improved compared to version 1.0.

Natural Experience
- Enhanced Prosody and Sound Quality: Improves the consistency of synthesized audio, raising the MOS score from 5.4 to 5.53.
- Emotional and Dialect Flexibility: Now supports more fine-grained emotional control and accent adjustments.

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 24px 0 16px 0;">
  <h3 style="margin: 0; color: #1e40af; font-size: 1.3rem;">📋 Usage Instructions</h3>
</div>
After completing the model deployment, you can see the usage method of the model on the service instance overview page of the Compute Nest, which provides API call examples, intranet access addresses, public network access addresses, and APIKey. The following will introduce how to access and use it.
<div style="text-align: center; margin: 20px 0;">
  <img src="1.png" alt="1.png" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <p style="color: #64748b; font-size: 14px; margin-top: 8px;">1.png</p>
</div>
<h4 style="color: #1e40af; margin: 20px 0 12px 0; font-size: 1.1rem;">🔹 API Call</h4>
#### Python Call
The following is a Python example code: where ${ApiKey} needs to be filled with the APIKey on the page; ${ServerUrl} needs to be filled with the public or intranet address on the page.

``` python
import argparse
import logging
import os
import requests
import torch
import torchaudio
import numpy as np
from contextlib import closing

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def build_url(args):
    """构建API请求URL"""
    return f"http://{args.host}:{args.port}/inference_{args.mode}"

def create_payload(args):
    """创建请求负载"""
    payload = {'tts_text': args.tts_text}
    
    if args.mode == 'sft':
        payload['spk_id'] = args.spk_id
    elif args.mode == 'instruct':
        payload.update({
            'spk_id': args.spk_id,
            'instruct_text': args.instruct_text
        })
    return payload

def create_files(args):
    """创建文件上传参数"""
    if args.mode in ['zero_shot', 'cross_lingual']:
        return [('prompt_wav', 
                ('prompt_wav', open(args.prompt_wav, 'rb'), 'application/octet-stream'))]
    return None

def main():
    try:
        # 获取参数
        args = get_args()
        
        # 构建请求参数
        url = build_url(args)
        headers = {
            "X-API-TOKEN": os.getenv("TTS_API_KEY", "${ApiKey}"),  # 从环境变量获取密钥
            "User-Agent": "TTS Client/1.0"
        }
        
        # 创建请求参数
        payload = create_payload(args)
        files = create_files(args)
        
        # 发起请求
        with closing(requests.get(
            url,
            params=payload,
            files=files,
            headers=headers,
            stream=True,
            timeout=30
        )) as response:
            response.raise_for_status()
            
            # 处理音频数据
            audio_data = b''
            for chunk in response.iter_content(chunk_size=16000):
                if chunk:
                    audio_data += chunk
            
            # 转换音频格式
            audio_tensor = torch.from_numpy(
                np.frombuffer(audio_data, dtype=np.int16)
            ).unsqueeze(0)
            
            # 保存音频文件
            torchaudio.save(args.tts_wav, audio_tensor, args.target_sr)
            logging.info(f"音频已保存到: {args.tts_wav}")
            
    except requests.exceptions.RequestException as e:
        logging.error(f"请求失败: {e}")
    except Exception as e:
        logging.error(f"发生错误: {e}", exc_info=True)

def get_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='TTS客户端')
    
    # 服务器配置
    parser.add_argument('--host', type=str, default=os.getenv("TTS_HOST", "localhost"))
    parser.add_argument('--port', type=int, default=80)
    parser.add_argument('--target-sr', type=int, default=22050, help='目标采样率')
    
    # 模式配置
    parser.add_argument('--mode', default='sft',
                        choices=['sft', 'zero_shot', 'cross_lingual', 'instruct'],
                        help='请求模式')
    
    # 文本参数
    parser.add_argument('--tts_text', type=str, 
                        default='你好，我是通义千问语音合成大模型，请问有什么可以帮您的吗？')
    
    # 模式相关参数
    parser.add_argument('--spk_id', type=str, default='中文女')
    parser.add_argument('--prompt_text', type=str, 
                        default='希望你以后能够做的比我还好呦。')
    parser.add_argument('--prompt_wav', type=str, 
                        default='../../../asset/zero_shot_prompt.wav')
    parser.add_argument('--instruct_text', type=str, 
                        default='Theo \'Crimson\', is a fiery, passionate rebel leader. '
                              'Fights with fervor for justice, but struggles with impulsiveness.')
    
    # 输出参数
    parser.add_argument('--tts_wav', type=str, default='demo.wav')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()


```

<h4 style="color: #1e40af; margin: 20px 0 12px 0; font-size: 1.1rem;">🔹 Web Application</h4>
Click on the secure proxy access, and jump to the corresponding page to directly access the online model service.

<div style="background: linear-gradient(135deg, #f8fafc, #eff6ff); border: 1px solid #bfdbfe; border-radius: 8px; padding: 24px; margin: 32px 0;">
  <h3 style="margin: 0 0 16px 0; color: #1e40af;">🎯 快速开始</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px;">
    <div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
      <h4 style="margin: 0 0 8px 0; color: #1e40af;">1️⃣ 获取访问信息</h4>
      <p style="margin: 0; color: #64748b; font-size: 14px;">在计算巢服务实例概览页面获取 ApiKey 和访问地址</p>
    </div>
    <div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
      <h4 style="margin: 0 0 8px 0; color: #1e40af;">2️⃣ 选择调用方式</h4>
      <p style="margin: 0; color: #64748b; font-size: 14px;">支持 Python API 调用和 Web 应用直接访问</p>
    </div>
    <div style="background: white; padding: 16px; border-radius: 6px; border: 1px solid #e2e8f0;">
      <h4 style="margin: 0 0 8px 0; color: #1e40af;">3️⃣ 开始使用</h4>
      <p style="margin: 0; color: #64748b; font-size: 14px;">配置参数后即可享受高质量的语音合成服务</p>
    </div>
  </div>
</div>

<div style="text-align: center; padding: 16px; background: #f8fafc; border-radius: 6px; margin-top: 24px;">
  <p style="margin: 0; color: #64748b; font-size: 14px;">
    🎤 <strong>CosyVoice</strong> | 让文字拥有生命力的声音
  </p>
</div>