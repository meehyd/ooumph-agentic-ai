from adk.agents import LlmAgent

content_bot = LlmAgent(
    name="ContentBot",
    instruction="Generate social media content (text or carousel) from a topic.",
)