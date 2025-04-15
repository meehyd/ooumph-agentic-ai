from dotenv import load_dotenv
load_dotenv()

import os
import sys
import streamlit as st

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.lead_agent.lead_agent import lead_agent_response
from tools.document_search_tool import search_documents

# ───────────────────────────────────────────────────────────────── #
# 🎯 Streamlit App Config
st.set_page_config(page_title="🧠 Ooumph Agentic AI", layout="centered")
st.title("🧠 Ooumph Multi-Agent Assistant")

# Session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Mode toggle
mode = st.sidebar.radio("Select Mode", ["🤖 Agent Chat", "📚 Ask Your Docs"])

# ───────────────────────────────────────────────────────────────── #
# 🔹 MODE 1: AGENTIC CHAT
if mode == "🤖 Agent Chat":
    st.header("🧠 LeadAgent — Talk to Your Agentic AI")

    user_input = st.chat_input("Ask something (e.g., 'Build a startup community')")

    if user_input:
        # Log user input
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("🤖 LeadAgent thinking..."):
            response = lead_agent_response(user_input)
            st.session_state.chat_history.append({
                "role": "agent",
                "content": response.content  # ✅ Only show plain response
            })

    # Display chat history
    for msg in st.session_state.chat_history:
        role = "user" if msg["role"] == "user" else "assistant"
        st.chat_message(role).markdown(msg["content"])

# ───────────────────────────────────────────────────────────────── #
# 🔹 MODE 2: DOCUMENT SEARCH (RAG)
elif mode == "📚 Ask Your Docs":
    st.header("📂 Ask Your Uploaded Documents")

    doc_query = st.text_input("Ask something based on your documents (e.g., 'Explain the trust framework')")

    if st.button("Search Documents") and doc_query:
        with st.spinner("🔍 Searching your document knowledge base..."):
            results = search_documents(doc_query)
            if results:
                for i, result in enumerate(results, 1):
                    st.markdown(f"**Result {i}:**")
                    st.write(result["text"])
                    st.caption(f"📄 Source: `{result.get('filename', 'unknown')}`")
            else:
                st.warning("No relevant documents found.")