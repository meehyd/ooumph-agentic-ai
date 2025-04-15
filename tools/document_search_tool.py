from config.qdrant_vector_store import qdrant_client, collection_name
from utils.model_config import model

def search_documents(query: str, limit: int = 5):
    """Embed the query and search Qdrant for the most relevant documents."""
    query_vector = model.embed_text(
        text=query,
        task="retrieval_query"
    )

    results = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=limit
    )

    return [hit.payload for hit in results]