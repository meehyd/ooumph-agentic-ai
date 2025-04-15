from agno.knowledge.supabase import SupabaseKnowledgeBase

supabase_knowledge = SupabaseKnowledgeBase(
    supabase_url="https://your-supabase-url.supabase.co",
    supabase_key="your_supabase_service_role_key",
    table_name="document_embeddings"
)
