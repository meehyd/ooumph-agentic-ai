from dotenv import load_dotenv
load_dotenv()

from agno.team import Team
from utils.model_config import model

# ────── Import Sub-Agents ────── #
from agents.marketing_layer.marketing_agent import marketing_agent
from agents.marketing_layer.seo_agent import seo_agent
from agents.marketing_layer.content_bot import content_bot
from agents.marketing_layer.social_media_agent import social_media_agent
from agents.marketing_layer.reporting_bot import reporting_bot

from agents.trust_layer.vibe_trust_agent import vibe_trust_agent
from agents.trust_layer.botshield_agent import botshield_agent

from agents.community_layer.community_builder_agent import community_builder_agent
from agents.business_layer.business_matcher_agent import business_matcher_agent
from agents.governance_layer.governance_controller_agent import governance_controller_agent

# ────── Marketing Team ────── #
marketing_team = Team(
    name="MarketingTeam",
    members=[
        marketing_agent,
        seo_agent,
        content_bot,
        social_media_agent,
        reporting_bot
    ],
    model=model,
    markdown=True
)

# ────── Lead Agent (MissionControl) ────── #
lead_agent = Team(
    name="LeadAgent",
    members=[
        marketing_team,
        vibe_trust_agent,
        botshield_agent,
        community_builder_agent,
        business_matcher_agent,
        governance_controller_agent
    ],
    model=model,
    markdown=True
)

# ────── Sync Wrapper for Streamlit & CLI ────── #
def lead_agent_response(prompt: str) -> str:
    """Sync-friendly wrapper for Team.run()."""
    return lead_agent.run(prompt)

"""
LeadAgent: MissionControl of Ooumph Agentic AI System.
This agent orchestrates Trust, Community, Business, Governance, and Marketing subsystems.
"""