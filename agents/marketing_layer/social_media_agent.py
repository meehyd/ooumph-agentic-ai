from agno.agent import Agent
from utils.model_config import model


social_media_agent = Agent(
    name="SocialMediaAgent",
    description="Schedules, posts, and analyzes social content.",
    model=model,
    markdown=True,
    memory=True
)
