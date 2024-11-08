# pinecone_utils.py
from .pinecone_config import index

def upsert_vector(id, vector):
    """Upsert a vector with a unique ID."""
    index.upsert([(id, vector)])

def query_similar_vectors(vector, top_k=5):
    """Query similar vectors based on a given input vector."""
    results = index.query(vector, top_k=top_k, include_values=True)
    return results['matches']

def delete_vector(id):
    """Delete a vector by ID."""
    index.delete(id)
