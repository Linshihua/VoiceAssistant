import json

from Invoice import record_audio
from Speech_re import recognize_speech
from Ai_Model import llm_answer
from textTovoice import  tts
import winsound


def voice_assistant(configs):
    tmp_wav_file = "user.wav"
    #录音
    record_audio(tmp_wav_file, duration=10)
    # 语音转文字
    user_text = recognize_speech(tmp_wav_file)
    print("user:", user_text)

    # 语言模型回答
    bot_text = llm_answer(user_text,configs['deepseek_key'])
    print("out:", bot_text)

    # 语音合成
    tmp_out_wav_file = "output.wav"
    tts(bot_text, tmp_out_wav_file)

    # 播放
    winsound.PlaySound(tmp_out_wav_file, winsound.SND_FILENAME)


if __name__ == '__main__':
    configs = json.load(open('config_key.json'))
    voice_assistant(configs)