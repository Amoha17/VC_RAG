import whisper
import os
from pydub import AudioSegment

# Load Whisper model once
model = whisper.load_model("small")  # or use "base", "medium", "large" depending on accuracy/speed needs

def convert_to_wav_mono_16k(audio_path: str, output_path: str):
    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")

def transcribe_whisper(audio_path: str, language: str = None) -> str:
    # Optional: convert input to correct format
    converted_path = "converted_input.wav"
    convert_to_wav_mono_16k(audio_path, converted_path)

    result = model.transcribe(converted_path, language=language)
    return result["text"]

if __name__ == "__main__":
    input_audio = r"C:\Users\AMOHA\PycharmProjects\VC_RAG\src\someone.wav"
    print("Transcribing...")
    transcription = transcribe_whisper(input_audio, language=None)  # Auto-detect language
    print("Transcribed Text:", transcription)
