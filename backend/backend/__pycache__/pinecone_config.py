import os
from pinecone import Pinecone, ServerlessSpec

# Get your Pinecone API key from environment variables or configure directly
API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone instance
pc = Pinecone(api_key=API_KEY)

# Ensure the index exists or create it if necessary
INDEX_NAME = "myindex-123"  # Make sure this is valid

# Check if the index exists first
if INDEX_NAME not in pc.list_indexes().names():
    # If not, create it
    pc.create_index(
        name=INDEX_NAME, 
        dimension=1536, 
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'  # Use a supported region for free plan
        )
    )
