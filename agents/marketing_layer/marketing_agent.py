from agno.agent import Agent
from utils.model_config import model

from tools.marketing_tools import generate_blog, search_trends

marketing_agent = Agent(
    name="MarketingAgent",
    description="Handles SEO, content, and social tasks.",
    model=model,
    tools=[generate_blog, search_trends],
    markdown=True,
    memory=True
)
