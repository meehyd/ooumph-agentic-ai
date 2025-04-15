from agno.tools import tool

@tool
def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of the provided text."""
    if "fail" in text or "hate" in text:
        return "Negative 😠"
    elif "love" in text or "win" in text:
        return "Positive 😄"
    else:
        return "Neutral 😐"
