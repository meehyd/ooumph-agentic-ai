# 🌐 Ooumph Agentic AI System - Full Build Log Context

## 🧠 Tech Stack & Tools
- Framework: [AGNO](https://github.com/agno-agi/agno)
- Models: Gemini (Gemini 1.5 Flash, Embedding-001)
- RAG: Qdrant Vector Store (Docker)
- App UI: Streamlit
- Environment: Python 3.13, `.venv`, `.env` for keys

## 🧱 Agentic Architecture

### Supervisor
- `LeadAgent` (Team of teams)

### Trust Layer
- `VibeTrustAgent`
- `BotShieldAgent`

### Community Layer
- `CommunityBuilderAgent`

### Business Layer
- `BusinessMatcherAgent`

### Governance Layer
- `GovernanceControllerAgent`

### Marketing Layer
- `MarketingTeam` includes:
  - `MarketingAgent`
  - `SEOAgent`
  - `ContentBot`
  - `SocialMediaAgent`
  - `ReportingBot`

## 🔧 Tools & Features

- Gemini embedding via `utils/gemini_wrapper.py`
- Qdrant integration in `upload_documents.py` and `document_search_tool.py`
- Persistent memory with AGNO (enabled)
- Streamlit UI with agent chat + document query
- `.env` uses `GOOGLE_API_KEY`

## 🔄 Deployment & Dev Flow

- Run Qdrant via Docker
- Upload docs with: `python tools/upload_documents.py`
- Launch UI with: `streamlit run ui/app.py`

## ⚠️ Errors Resolved

- `GeminiPro` import replaced with `Gemini()`
- Circular import fixed for `model_config.py`
- Fixed `get_response()` → used `.run(prompt)`
- Missing `.env` key updated
- Streamlit and agent layers now fully working

## ✅ Status
System is fully functional and responds correctly with nested teams + tools. Ready for deployment.