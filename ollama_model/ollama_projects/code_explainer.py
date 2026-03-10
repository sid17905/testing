import requests

url = "http://localhost:11434/api/generate"

print("AI Code Explainer v2")
print("Paste your code below.")
print("Type 'END' on a new line when finished.\n")

while True:

    print("Paste your code:")
    
    lines = []
    
    while True:
        line = input()
        
        if line == "END":
            break
        
        lines.append(line)

    code = "\n".join(lines)

    if code.lower() == "exit":
        break

    prompt = f"""
Explain the following code in simple terms.
Also mention:
1. What the code does
2. Important concepts used
3. Possible improvements

Code:
{code}
"""

    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    print("\nAI Explanation:\n")
    print(result["response"])
    print("\n---------------------------------\n")