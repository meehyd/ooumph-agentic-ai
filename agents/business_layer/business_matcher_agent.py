from agno.agent import Agent
from utils.model_config import model

business_matcher_agent = Agent(
    name="BusinessMatcherAgent",
    description="Validates business trust and matches them with relevant users or communities.",
    model=model,
    markdown=True,
    memory=True
)
