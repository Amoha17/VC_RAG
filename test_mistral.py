from langchain.llms import LlamaCpp


def test_llama_model():
    llm = LlamaCpp(
        model_path="C:/Users/AMOHA/PycharmProjects/VC_RAG/models/mistral-7b-instruct-v0.1.Q3_K_L.gguf",
        n_ctx=4096,
        n_threads=4,  # Adjust threads based on your CPU cores
        n_batch=8,
        verbose=True,
        temperature=0.7,
        top_p=0.9,
    )

    prompt = "Hello, how are you today?"
    response = llm(prompt)
    print("Model response:\n", response)


if __name__ == "__main__":
    test_llama_model()
