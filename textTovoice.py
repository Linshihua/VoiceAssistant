import pyttsx3  # https://pypi.org/project/pyttsx3/

def tts(text, output_wav_path):
    engine = pyttsx3.init() # object creation
    engine.save_to_file(text, output_wav_path)
    engine.runAndWait()


if __name__ == '__main__':
    tts('今天天气怎么样？', 'user1.wav')