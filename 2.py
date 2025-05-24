
import requests

url = "http://127.0.0.1:8082/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "model": "mistralai_mistral-7b-instruct-v0.1",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
