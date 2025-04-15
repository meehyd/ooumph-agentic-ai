# 🧠 Ooumph Agentic AI

This is a multi-agent system powered by Ooumph AI. The architecture supports community building, marketing automation, trust scoring, governance, and business validation.

---

## 🚀 How to Run

## ⚙️ Setup Instructions

### ✅ 1. Environment Setup

```bash
python -m venv .venv
.venv\Scripts\activate           # Windows
source .venv/bin/activate        # macOS/Linux
```

### ✅ 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ 3. Configure Environment

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🧠 Qdrant Vector Store (RAG)

### 🔌 Start Qdrant (via Docker)

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 🧠 Configure in `config/qdrant_vector_store.py`

```python
from agno.knowledge.qdrant import QdrantKnowledgeBase

qdrant_knowledge = QdrantKnowledgeBase(
    host="http://localhost",
    port=6333,
    collection_name="oumph_documents"
)
```

### 📚 Upload Documents

```bash
python tools/upload_documents.py
```

> This will vectorize and add documents to Qdrant from the `docs/` folder (can be changed).

---

## 🧠 PostgreSQL Memory Store (Optional)

### 📄 `config/postgres_memory.py`

```python
from agno.storage.sql_storage import SqlStorage

postgres_storage = SqlStorage(
    uri="postgresql://user:pass@localhost:5432/oumph_ai_memory"
)
```

> You can launch PostgreSQL via Docker or a managed DB.

---

## 🧪 Run the System

### 🧠 CLI Mode

```bash
python run.py
```

### 🖥️ Web UI (Streamlit)

```bash
streamlit run ui/app.py
```

---

## 📚 Routing Logic (Optional)

Use `configs/routing.yaml` to auto-route user input based on type:

```yaml
routing:
  - condition: "type == 'marketing'"
    agent: marketing_agent
  - condition: "type == 'trust'"
    agent: vibe_trust_agent
```

---

## ✅ Agents & Tools Overview

| Agent                   | Key Functions                                             |
|------------------------|-----------------------------------------------------------|
| `LeadAgent`            | Supervisor for all workflows                              |
| `MarketingTeam`        | Blog generation, social posting, performance tracking     |
| `VibeTrustAgent`       | Trust scoring from sentiment and network behavior         |
| `BotShieldAgent`       | Detect fake profiles and bot anomalies                    |
| `CommunityBuilderAgent`| Create and manage communities                             |
| `BusinessMatcherAgent` | Match trusted users with businesses/freelancers           |
| `GovernanceController` | Conduct decentralized voting & policy checks              |


---

## 🧠 Features

- ✅ Memory per user via `default_memory=True`
- ✅ Persistent storage (coming via PostgreSQL)
- ✅ Multi-agent collaboration via `Team`
- ✅ Document grounding (RAG) via AGNO integrations


---

## 🧠 Persistent Memory (PostgreSQL)

- Configure `config/postgres_memory.py` with your database URI
- You can use Docker or a local PostgreSQL instance

## 📚 Supabase Vector Store (RAG)

- Add your Supabase project URL and service key to `config/supabase_vector_store.py`
- Required for document-aware responses and contextual injection

## 🖥️ Streamlit UI

To launch the UI:

```bash
streamlit run ui/app.py
```

Then open http://localhost:8501

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Full Stack

```bash
# Backend
python run.py

# Frontend UI
streamlit run ui/app.py

# Upload docs to Supabase
python tools/upload_documents.py
```


---

## 🧠 Qdrant Vector Store (RAG)

Instead of Supabase, we now use [Qdrant](https://qdrant.tech) to store document embeddings.

### ✅ Run Qdrant (Docker):

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 📄 Config: `config/qdrant_vector_store.py`

```python
from agno.knowledge.qdrant import QdrantKnowledgeBase

qdrant_knowledge = QdrantKnowledgeBase(
    host="http://localhost",
    port=6333,
    collection_name="oumph_documents"
)
```

### 📚 Upload Documents to Qdrant

```bash
python tools/upload_documents.py
```

Modify `upload_documents.py` to use `qdrant_knowledge` instead of `supabase_knowledge`.
