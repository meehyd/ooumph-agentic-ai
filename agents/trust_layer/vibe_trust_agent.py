from agno.agent import Agent
from utils.model_config import model

vibe_trust_agent = Agent(
    name="VibeTrustAgent",
    description="Calculates VibeScore for users based on behavior, sentiment, and community activity.",
    model=model,
    markdown=True,
    memory=True
)
