import whisper
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except:
        return False

if not check_ffmpeg():
    print("错误：未找到 FFmpeg，请先安装 FFmpeg 并添加到系统 PATH")
    exit(1)