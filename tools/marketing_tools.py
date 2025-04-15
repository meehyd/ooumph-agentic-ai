from agno.tools import tool

@tool
def generate_blog(prompt: str) -> str:
    """Generate an SEO blog post."""
    return f"[BLOG GENERATED FOR]: {prompt}"

@tool
def search_trends(topic: str) -> str:
    """Search top trends for a topic."""
    return f"[TRENDS FOUND]: {topic}"
