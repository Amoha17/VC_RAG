import subprocess

def query_ollama_mistral(query: str, context: str = "") -> str:
    """
    Call Ollama Mistral locally using subprocess, passing context + query.
    """
    prompt = f"Context:\n{context}\n\nUser Query:\n{query}\n\nAnswer:"

    result = subprocess.run(
        ["ollama", "run", "mistral", "--prompt", prompt],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Ollama error: {result.stderr}")

    return result.stdout.strip()
