import os
import requests

url = "http://localhost:11434/api/generate"

project_path = input("Enter project folder path: ")

all_code = ""

for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith((".py", ".js", ".java", ".cpp", ".ts")):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    all_code += f"\n\nFile: {file}\n{content}"
            except:
                pass

prompt = f"""
Analyze this software project.

Explain:
1. What the project does
2. Architecture
3. Important components
4. Possible improvements

Project code:
{all_code[:8000]}
"""

data = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)

result = response.json()

print("\nAI Project Analysis:\n")
print(result["response"])