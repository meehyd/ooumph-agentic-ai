from agno.agent import Agent
from utils.model_config import model

governance_controller_agent = Agent(
    name="GovernanceControllerAgent",
    description="Manages rules, votes, and ensures fair decision-making in Ooumph communities.",
    model=model,
    markdown=True,
    memory=True
)
