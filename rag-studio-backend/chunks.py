def createchunks(documents: list):
    Chunks = []

    chunk_size = 800
    overlap = 150

    for doc in documents:

        text = doc["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            Chunks.append({
                "text": chunk_text,
                "source": doc["source"],
                "page": doc["page"]
            })

            start += chunk_size - overlap

    return Chunks