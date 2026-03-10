
class ChatBot:
    def __init__(self):
        self.name = "PythonPal"
        self.greetings = ["Hello", "Hi", "Hey"]
        self.weather = ["sunny", "cloudy", "rainy"]
        self.info = {
            "Python": "A high-level, interpreted programming language.",
            "Java": "A high-level, object-oriented programming language.",
            "C++": "A high-performance, compiled programming language."
        }

    def greet(self):
        return random.choice(self.greetings) + ", I'm " + self.name

    def ask_weather(self):
        return "The weather is " + random.choice(self.weather) + " today."

    def ask_language_info(self, language):
        return self.info.get(language, "Sorry, I don't know about " + language + ".")

    def chat(self):
        print(self.greet())
        while True:
            query = input("User: ")
            if "hello" in query.lower():
                print(self.greet())
            elif "weather" in query.lower():
                print(self.ask_weather())
            elif "what is" in query.lower():
                language = query.split("what is")[1].strip()
                print(self.ask_language_info(language))
            elif "quit" in query.lower():
                break
            else:
                print("Sorry, I didn't understand your query.")

import random
chat_bot = ChatBot()
chat_bot.chat()

