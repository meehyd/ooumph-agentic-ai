from agno.agent import Agent
from utils.model_config import model

content_bot = Agent(
    name="ContentBot",
    description="Creates visual and textual content for social platforms.",
    model=model,
    markdown=True,
    memory=True
)
