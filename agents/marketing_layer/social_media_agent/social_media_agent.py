from adk.agents import LlmAgent
from tools.scheduler_tool import SchedulerTool

social_media_agent = LlmAgent(
    name="SocialMediaAgent",
    instruction="Schedule social media posts using Buffer or X APIs.",
    tools=[SchedulerTool()],
)
