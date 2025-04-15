from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, CollectionStatus

collection_name = "ooumph_documents"
embedding_dim = 768  # Must match the output size of Gemini embeddings

# Initialize Qdrant client
qdrant_client = QdrantClient(host="localhost", port=6333)

def ensure_qdrant_collection():
    """Create collection if it doesn't exist."""
    if not qdrant_client.collection_exists(collection_name):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=embedding_dim,
                distance=Distance.COSINE
            )
        )
        print(f"✅ Created Qdrant collection: {collection_name}")
    else:
        status = qdrant_client.get_collection(collection_name).status
        if status == CollectionStatus.GREEN:
            print(f"✅ Qdrant collection '{collection_name}' is ready.")
        else:
            print(f"⚠️ Qdrant collection '{collection_name}' status: {status}")