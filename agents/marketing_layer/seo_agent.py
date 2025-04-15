from agno.agent import Agent
from utils.model_config import model

from tools.marketing_tools import generate_blog, search_trends

seo_agent = Agent(
    name="SEOAgent",
    description="Creates optimized blog and webpage content.",
    model=model,
    tools=[generate_blog, search_trends],
    markdown=True,
    memory=True
)
