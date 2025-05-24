from tts_engine import speak_gtts

# Speak English
speak_gtts("Hello, how are you?", lang="en")

# Speak Korean
speak_gtts("안녕하세요, 잘 지내세요?", lang="ko")

from fastapi import FastAPI, Query
import requests

app = FastAPI()  # <-- ✅ This defines 'app'

LLM_API_URL = "http://localhost:8081/v1/chat/completions"  # Update port to your LLM backend

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.post("/chat")
def chat(prompt: str = Query(...)):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai_mistral-7b-instruct-v0.1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(LLM_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return {"response": data["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
