from agno.tools import tool
import datetime

@tool
def schedule_post(content: str, post_time: str) -> str:
    """Schedules a post at the specified time."""
    try:
        dt = datetime.datetime.strptime(post_time, "%Y-%m-%d %H:%M:%S")
        return f"✅ Post scheduled for {dt.strftime('%Y-%m-%d %H:%M:%S')} with content: {content[:60]}"
    except ValueError:
        return "❌ Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"
