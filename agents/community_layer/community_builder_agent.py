from agno.agent import Agent
from utils.model_config import model

community_builder_agent = Agent(
    name="CommunityBuilderAgent",
    description="Creates and configures new Ooumph communities based on user prompts and needs.",
    model=model,
    markdown=True,
    memory=True
)
