from dotenv import load_dotenv
load_dotenv()
from agents.lead_agent.lead_agent import lead_agent

if __name__ == "__main__":
    lead_agent.print_response("Launch a trust-based real estate campaign.", stream=True)
