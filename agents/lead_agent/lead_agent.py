from adk.agents import WorkflowAgent
from agents.marketing_layer.marketing_agent.marketing_agent import marketing_agent
# Placeholder: other agents (we'll add in future phases)

# Define LeadAgent with MarketingAgent for now
lead_agent = WorkflowAgent(
    name="LeadAgent",
    instruction="You're the brain of the Ooumph system. Detect intent and delegate tasks.",
    sub_agents=[marketing_agent]
)

# Custom dispatching logic (if needed later for complex routing)
