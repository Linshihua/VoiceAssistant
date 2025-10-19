import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(filename, duration=5, sample_rate=44100):
    print("开始录音...")
    recording = sd.rec(int(duration * sample_rate),
                       samplerate=sample_rate,
                       channels=1,
                       dtype='int16')
    sd.wait()  # 等待录音完成
    print("录音结束")

    write(filename, sample_rate, recording)


# 使用示例
if __name__ == '__main__':
    record_audio("output.wav", duration=5)