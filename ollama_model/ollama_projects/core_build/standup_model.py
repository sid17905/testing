import requests
from prompts import build_standup_prompt

def generate_standup(context):

    prompt = build_standup_prompt(context)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]