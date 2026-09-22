def searchforcontext(Chunks: list,query_embedding: np.ndarray, index: faiss.Index ):

    distances, indices = index.search(query_embedding, 3)

    context = ""

    for i in indices[0]:
        context += Chunks[i]["text"] + "\n\n"

    return context