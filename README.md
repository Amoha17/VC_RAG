# 🎙️ VC_RAG: Multilingual Voice-Based Retrieval-Augmented Generation System

This is a prototype voice assistant for visually impaired users. It uses a multilingual speech-to-text → semantic search → LLM → text-to-speech pipeline.

---

## 🔧 Features

- 🎤 Speech-to-Text using OpenAI Whisper
- 🔎 Semantic Search using LangChain + ChromaDB
- 🧠 LLM-based question answering using LlamaCpp
- 🗣️ Text-to-Speech using Google TTS (gTTS) + pygame
- 🌐 Multilingual support (English, Hindi, Telugu, etc.)

---

## 📁 Project Structure

VC_RAG/
├── data/
│ └── documents/ # Source PDFs for knowledge base
|
├── src/
│ ├── stt_whisper.py # Whisper-based STT
│ ├── semantic_search.py # RAG logic with LangChain
│ ├── rag_wrapper.py # Wrapper to use the RAG system
│ ├── tts_engine.py # gTTS-based TTS
│ ├── vc_pipeline.py # End-to-end voice pipeline
│ └── test.py # Pipeline test script
├── models/
│ └── ggml-model-q4_0.gguf # LLaMA model file (not included)
├── requirements.txt # Python dependencies
└── README.md


---

## 🚀 Setup

### 1. 🐍 Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


2.  Download & Place Models
LLaMA GGUF model → Place it in models/

Whisper → Automatically downloaded by openai-whisper library


Run the Full Pipeline:
python src/test.py

This will:

Transcribe a voice file (WAV)
Search documents semantically
Answer using LLM
Read out the answer

Notes
Use .wav files (16kHz, mono) for input audio.
For multilingual support, language is auto-detected using langdetect.
TTS output is played using pygame and then cleaned up.

Credits

OpenAI Whisper
LangChain
gTTS
LlamaCpp
ChromaDB

Future Work

Mic input
REST API (Flask/FastAPI)
Better TTS voices (e.g., Coqui TTS)
UI for visually impaired users
