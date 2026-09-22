def createqueryembedding(userQuery :str,embedding_model: np.ndarray ):
    import numpy as np

    query_embedding = embedding_model.encode([userQuery])

    # Convert to NumPy float32
    query_embedding = np.array(query_embedding).astype("float32")
    
    return query_embedding 