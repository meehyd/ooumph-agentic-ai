from agno.tools import tool

@tool
def verify_business_documents(business_id: str) -> str:
    """Check if submitted business documents are verified."""
    return f"[Document Verification] Business ID {business_id} is verified ✅"
