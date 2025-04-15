from agno.tools import tool

@tool
def generate_voting_report(proposal_id: str) -> str:
    """Generate a governance voting report for a given proposal."""
    return f"[Voting Report for Proposal {proposal_id}] Success: 78%, Fail: 22%"
