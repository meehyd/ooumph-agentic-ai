from agno.tools import tool

@tool
def generate_report(campaign_id: str) -> str:
    """Generate performance report for a given campaign."""
    return f"[Report] Campaign {campaign_id}: 4500 reach, 12.5% CTR, 8% conversion rate"
