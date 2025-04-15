import os
from dotenv import load_dotenv
from qdrant_client.models import PointStruct

from utils.model_config import model  # ✅ Supported model wrapper
from config.qdrant_vector_store import (
    qdrant_client,
    collection_name,
    ensure_qdrant_collection
)

# Load environment variables like GOOGLE_API_KEY
load_dotenv()

# Gemini Model
model = Gemini(
    model_name="gemini-1.5-flash",
    embed_model="embedding-001"
)

def embed_text(text: str):
    return model.embed_text(text, task="retrieval_document")

def upload_documents_to_qdrant(directory: str = "docs"):
    ensure_qdrant_collection()

    documents = []
    doc_id = 1

    for filename in os.listdir(directory):
        if filename.endswith(".txt") or filename.endswith(".md"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                text = f.read()
                vector = embed_text(text)
                documents.append(PointStruct(
                    id=doc_id,
                    vector=vector,
                    payload={"filename": filename, "text": text}
                ))
                doc_id += 1

    qdrant_client.upsert(collection_name=collection_name, points=documents)
    print(f"✅ Uploaded {len(documents)} documents to Qdrant.")

if __name__ == "__main__":
    upload_documents_to_qdrant()