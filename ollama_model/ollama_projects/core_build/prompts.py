def build_summary_prompt(context: str) -> str:
    return f"""
You are an AI project intelligence assistant.

Analyze this project data and provide a sprint health report.

{context}

Write a report covering:
1. Overall sprint progress
2. Key blockers
3. Team workload concerns
4. Recommended actions

Keep it concise.
"""


def build_standup_prompt(context: str) -> str:
    return f"""
You are an AI scrum assistant.

Generate a standup update using this format.

{context}

Format:

Yesterday:
- per person summary

Today:
- per person plan

Blockers:
- blockers list
"""