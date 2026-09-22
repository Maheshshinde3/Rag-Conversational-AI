def callLLm(userQuery: str, context: str):
    from huggingface_hub import InferenceClient
    import os
    
    HF_TOKEN = os.getenv("HF_TOKEN")

    client = InferenceClient(
        api_key=HF_TOKEN
    )

    response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4-Flash-0731",
    messages=[
        {
            "role": "system",
            "content": """You are a helpful AI assistant.
    Answer the user's question using only the provided context.
    If the answer is not present in the context, say:
    "I could not find the answer in the provided document."
    """
        },
        {
            "role": "user",
            "content": f"""Context:
    {context}

    Question:
    {userQuery}
    """
        }
    ]
    )

    # print(api_key)
    answer = response.choices[0].message.content
    return answer