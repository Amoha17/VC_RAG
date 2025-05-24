
import requests
from tts_engine import speak_text

url = "http://localhost:11434/api/chat"

prompt = "What is the capital of France?"

payload = {
    "model": "mistral",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "stream": False  # Important: prevents stream output (JSONL)
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    message = data["message"]["content"]
    print(f"LLM: {message}")
    speak_text(message)
except Exception as e:
    print(f"Error: {e}")
