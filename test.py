# test.py

from src.vc_pipeline import vc_pipeline

# Path to your test audio file (ensure it exists)
audio_file_path = "C:/Users/AMOHA/PycharmProjects/VC_RAG/src/someone.wav"


if __name__ == "__main__":
    print("[TEST] Running voice-based RAG pipeline...")

    try:
        answer = vc_pipeline(audio_file_path)
        print(f"[TEST] Final Answer: {answer}")
    except Exception as e:
        print(f"[ERROR] Pipeline failed: {e}")
