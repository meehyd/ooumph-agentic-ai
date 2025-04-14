from agents.lead_agent.lead_agent import lead_agent

if __name__ == "__main__":
    print("🚀 Welcome to Ooumph Agentic AI Interface")
    user_input = input("📝 Enter a task prompt: ")

    payload = {
        "type": "marketing",
        "task": "launch_campaign",
        "data": {
            "prompt": user_input
        }
    }

    output = lead_agent.run(payload)
    print("📤 Output from Agent:\n", output)
