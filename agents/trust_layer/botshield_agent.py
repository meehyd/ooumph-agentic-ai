from agno.agent import Agent
from utils.model_config import model

from tools.trust_tools import detect_fake_behavior

botshield_agent = Agent(
    name="BotShieldAgent",
    description="Detects fake engagement, bots, and anomalies in community behavior.",
    model=model,
    tools=[detect_fake_behavior],
    markdown=True,
    memory=True
)
