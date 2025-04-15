# 🔧 Configuration Guide

## PostgreSQL Memory Setup
- Edit `postgres_memory.py` with your own PostgreSQL URL:
  ```python
  uri="postgresql://user:pass@host:port/dbname"
  ```
- Make sure the database is running locally or in Docker.

## Supabase Vector Store Setup
- Go to your Supabase project → API Settings.
- Use:
  ```python
  supabase_url="https://xyzcompany.supabase.co"
  supabase_key="your_service_role_key"
  ```
- Table `document_embeddings` will be created automatically when uploading docs.

## Dashboard Connection (Shared Memory + Vectors)
- Use `lead_agent` with both:
  - `storage=postgres_storage`
  - `knowledge_base=supabase_knowledge`
- This creates a shared agent that reasons across memory + documents.
