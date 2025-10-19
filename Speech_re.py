# 语音转文字模块
import whisper

def recognize_speech(wav_file):
    # 加载模型
    model = whisper.load_model("base")
    # 转录音频文件
    result = model.transcribe(wav_file, fp16=False)
    print("result:", result)

    return result['text']


if __name__ == '__main__':
    wav_file = 'output.wav'
    text = recognize_speech(wav_file)
    print("识别结果为：", text)
