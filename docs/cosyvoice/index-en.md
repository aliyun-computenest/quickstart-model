## Introduction
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

## Usage Instructions
After completing the model deployment, you can see the usage method of the model on the service instance overview page of the Compute Nest, which provides API call examples, intranet access addresses, public network access addresses, and APIKey. The following will introduce how to access and use it.

![1.png](1.png)

### API Call
#### Python Call
The following is a Python example code: where ${ApiKey} needs to be filled with the APIKey on the page; ${ServerUrl} needs to be filled with the public or intranet address on the page.
``` python
import argparse
import logging
import requests
import torch
import torchaudio
import numpy as np


def main():
    url = "http://{}:{}/inference_{}".format(args.host, args.port, args.mode)
    headers = {
        "X-API-TOKEN": "${ApiKey}"  # Add custom Header
    }
    if args.mode == 'sft':
        payload = {
            'tts_text': args.tts_text,
            'spk_id': args.spk_id
        }
        response = requests.request("GET", url, data=payload, stream=True, headers=headers)
    elif args.mode == 'zero_shot':
        payload = {
            'tts_text': args.tts_text,
            'prompt_text': args.prompt_text
        }
        files = [('prompt_wav', ('prompt_wav', open(args.prompt_wav, 'rb'), 'application/octet-stream'))]
        response = requests.request("GET", url, data=payload, files=files, stream=True, headers=headers)
    elif args.mode == 'cross_lingual':
        payload = {
            'tts_text': args.tts_text,
        }
        files = [('prompt_wav', ('prompt_wav', open(args.prompt_wav, 'rb'), 'application/octet-stream'))]
        response = requests.request("GET", url, data=payload, files=files, stream=True, headers=headers)
    else:
        payload = {
            'tts_text': args.tts_text,
            'spk_id': args.spk_id,
            'instruct_text': args.instruct_text
        }
        response = requests.request("GET", url, data=payload, stream=True, headers=headers)
    tts_audio = b''
    for r in response.iter_content(chunk_size=16000):
        tts_audio += r
    tts_speech = torch.from_numpy(np.array(np.frombuffer(tts_audio, dtype=np.int16))).unsqueeze(dim=0)
    logging.info('save response to {}'.format(args.tts_wav))
    torchaudio.save(args.tts_wav, tts_speech, target_sr)
    logging.info('get response')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host',
                        type=str,
                        default='${ServerUrl}')
    parser.add_argument('--port',
                        type=int,
                        default='80')
    parser.add_argument('--mode',
                        default='sft',
                        choices=['sft', 'zero_shot', 'cross_lingual', 'instruct'],
                        help='request mode')
    parser.add_argument('--tts_text',
                        type=str,
                        default='Hello, I am Qwen, the large language model for speech synthesis. How can I assist you?')
    parser.add_argument('--spk_id',
                        type=str,
                        default='Chinese Female')
    parser.add_argument('--prompt_text',
                        type=str,
                        default='I hope you can do better than me in the future.')
    parser.add_argument('--prompt_wav',
                        type=str,
                        default='../../../asset/zero_shot_prompt.wav')
    parser.add_argument('--instruct_text',
                        type=str,
                        default='Theo \'Crimson\', is a fiery, passionate rebel leader. \
                                 Fights with fervor for justice, but struggles with impulsiveness.')
    parser.add_argument('--tts_wav',
                        type=str,
                        default='demo.wav')
    args = parser.parse_args()
    prompt_sr, target_sr = 16000, 22050
    main()

```

### Web Application
Click on the secure proxy access, and jump to the corresponding page to directly access the online model service.