from adk.tools import Tool

class SchedulerTool(Tool):
    def __init__(self):
        super().__init__(name="PostSchedulerTool")

    def call(self, inputs: dict) -> dict:
        post = inputs.get("post", "")
        platform = inputs.get("platform", "LinkedIn")
        return {"status": "Scheduled", "platform": platform, "post": post}
