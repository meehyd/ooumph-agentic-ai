from agno.agent import Agent
from utils.model_config import model

from tools.analytics_tool import generate_report

reporting_bot = Agent(
    name="ReportingBot",
    description="Generates analytics and reports for campaigns.",
    model=model,
    tools=[generate_report],
    markdown=True,
    memory=True
)
