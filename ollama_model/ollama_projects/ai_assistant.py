import requests
import sys

url = "http://localhost:11434/api/generate"

if len(sys.argv) < 2:
    print("Usage: python ai_assistant.py <file>")
    exit()

file_path = sys.argv[1]

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

print("AI Coding Assistant Ready")
print("Type 'exit' to quit\n")

while True:

    question = input("Ask about the code: ")

    if question == "exit":
        break

    prompt = f"""
You are a senior software engineer.

Analyze the following code and answer the question.

Code:
{code}

Question:
{question}
"""

    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    print("\nAI:\n")
    print(result["response"])
    print("\n----------------------------\n")