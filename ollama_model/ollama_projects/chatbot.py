import requests

url = "http://localhost:11434/api/generate"
def quicksort(arr):
    if len(arr) <= 1:
        return arr
while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    print("AI:", result["response"])