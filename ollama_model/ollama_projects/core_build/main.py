from report_model import generate_report
from standup_model import generate_standup

with open(r"C:\Users\dhanr\OneDrive\Desktop\ollama_projects\core_build\project_data.txt") as f:
    context = f.read()

print("\n--- Sprint Report ---\n")
print(generate_report(context))

print("\n--- Standup Report ---\n")
print(generate_standup(context))