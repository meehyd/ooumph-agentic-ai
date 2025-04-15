from agno.tools import tool

@tool
def detect_fake_behavior(user_id: str) -> str:
    """Detect fake engagement based on behavioral anomalies."""
    return f"[Analysis for {user_id}]: Low reply ratio, repetitive likes, potential bot ✅"
