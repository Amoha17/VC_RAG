
import subprocess

mp3_path = "C:/Users/AMOHA/PycharmProjects/VC_RAG/src/someone.mp3"
wav_path = "C:/Users/AMOHA/PycharmProjects/VC_RAG/src/someone.wav"

subprocess.run([
    "ffmpeg",
    "-i", mp3_path,
    "-ar", "16000",   # Resample to 16 kHz
    "-ac", "1",       # Mono audio
    wav_path
])




