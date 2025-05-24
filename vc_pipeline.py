# src/vc_pipeline.py

from stt_whisper import transcribe_whisper
from rag_wrapper import query_semantic_search
from tts_engine import speak_gtts


def vc_pipeline(audio_path):
    print("Transcribing audio...")
    query = transcribe_whisper(audio_path)

    print("Querying semantic search with LLM...")
    answer = query_semantic_search(query)

    print("Converting response to speech...")
    speak_gtts(answer)

    return answer

from tts_engine import speak_gtts
# Example usage after getting the response
answer = "The capital of India is New Delhi."  # ← replace with your LLM output
speak_gtts(answer)
