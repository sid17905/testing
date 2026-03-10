import requests

url = "http://localhost:11434/api/generate"

languages = {
    "1": "Python",
    "2": "Java",
    "3": "C++",
    "4": "JavaScript",
    "5": "Go",
    "6": "Rust"
}

print("Offline AI Smart Code Generator\n")

while True:

    print("\nChoose language:")
    for key, value in languages.items():
        print(f"{key}. {value}")

    choice = input("\nEnter number (or exit): ")

    if choice.lower() == "exit":
        break

    if choice not in languages:
        print("Invalid choice")
        continue

    language = languages[choice]

    problem = input("\nEnter programming problem: ")

    prompt = f"""
You are a senior {language} developer.

Solve the following programming problem.

Return in this format:

1. CODE
2. EXPLANATION
3. TIME COMPLEXITY
4. TEST CASES

Problem:
{problem}
"""

    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    answer = result["response"]

    print("\nAI Output:\n")
    print(answer)

    save = input("\nSave code to file? (y/n): ")

    if save.lower() == "y":

        filename = input("Enter filename: ")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(answer)

        print(f"\nSaved to {filename}")

    print("\n------------------------------------\n")