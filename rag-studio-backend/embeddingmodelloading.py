def loadembeddingmodel():
    from sentence_transformers import SentenceTransformer 

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    return embedding_model
