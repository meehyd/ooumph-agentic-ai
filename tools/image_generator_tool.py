from agno.tools import tool

@tool
def generate_social_image(prompt: str) -> str:
    """Generate an image for social media based on a prompt."""
    return f"[Image Generated] for prompt: '{prompt}' (mock image URL)"
