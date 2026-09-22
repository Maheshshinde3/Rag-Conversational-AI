def createembeddings(Chunks: list, embedding_model: np.ndarray):
    import numpy as np
    import os

    # Get only the text from each chunk
    texts = [chunk["text"] for chunk in Chunks]

    # Convert text into embeddings
    embeddings = embedding_model.encode(texts)

    # Convert embeddings to NumPy array
    embeddings = np.array(embeddings).astype("float32")

    return embeddings

   

