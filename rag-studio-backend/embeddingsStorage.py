def storeEmbeddings(embeddings: np.ndarray, index: faiss.Index):
    import faiss

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    
    # Add embeddings
    index.add(embeddings)

    # Check stored vectors
    print("Total vectors:", index.ntotal)

    return index