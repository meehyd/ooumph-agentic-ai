from adk.agents import WorkflowAgent
from agents.marketing_layer.seo_agent.seo_agent import seo_agent
from agents.marketing_layer.content_bot.content_bot import content_bot
from agents.marketing_layer.social_media_agent.social_media_agent import social_media_agent

marketing_agent = WorkflowAgent(
    name="MarketingAgent",
    instruction="Plan and execute marketing tasks to promote verified businesses and communities.",
    sub_agents=[seo_agent, content_bot, social_media_agent]
)
