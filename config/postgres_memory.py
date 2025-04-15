from agno.storage.sql_storage import SqlStorage

# PostgreSQL connection URL format: postgresql://user:password@host:port/database
postgres_storage = SqlStorage(
    uri="postgresql://postgres:postgres@localhost:5432/oumph_ai_memory"
)
