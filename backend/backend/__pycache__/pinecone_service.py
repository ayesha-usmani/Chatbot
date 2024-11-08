from .pinecone_config import pc, INDEX_NAME

def query_similar_vectors(query_vector):
    try:
        # Example: Use the Pinecone client to query similar vectors
        index = pc.Index(INDEX_NAME)  # Use the initialized instance (pc)
        result = index.query([query_vector], top_k=5)
        return result

    except pinecone.exceptions.UnauthorizedException as e:
        raise ValueError(f"Unauthorized: {str(e)} - Check your API Key")
    except Exception as e:
        raise ValueError(f"An error occurred while querying Pinecone: {str(e)}")


def upsert_vector(vector_data):
    try:
        # Example: Use the Pinecone client to upsert a vector
        index = pc.Index(INDEX_NAME)  # Use the initialized instance (pc)
        index.upsert(vectors=[vector_data])
        return {"status": "success"}

    except pinecone.exceptions.UnauthorizedException as e:
        raise ValueError(f"Unauthorized: {str(e)} - Check your API Key")
    except Exception as e:
        raise ValueError(f"An error occurred while upserting the vector: {str(e)}")
