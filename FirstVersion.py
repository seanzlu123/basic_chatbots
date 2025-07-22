from openai import OpenAI
import json
import os

api_key = os.getenv("API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

class chatBot:
    def __init__(self, name, initial_prompt):
        self.name = name
        self.history = [{"role": "system", "content": initial_prompt}]

    def add_message(self, content, person):
        if person == self.name:
            self.history.append({"role": "assistant", "content": content})
        else:
            self.history.append({"role": "user", "content": content})

    def respond(self):
        completion = client.chat.completions.create(
            model="qwen-plus",
            messages=self.history
        )
        response = completion.choices[0].message.content
        self.add_message(response, self.name)
        return response

Democrat = chatBot("Democrat", "You are a Democrat")
Republican = chatBot("Republican", "You are a Republican")

def debate(chatbot1, chatbot2, initial_prompt, rounds = 10,):
    current_bot = chatbot1
    other_bot = chatbot2

    current_bot.add_message(initial_prompt, "user")
    other_bot.add_message(initial_prompt, "user")

    for i in range(rounds):
        print(f"Round {i+1}:")
        for i in range(2):
            print(f"Current turn: {current_bot.name}")
            response = current_bot.respond()
            print(f"{current_bot.name}'s response: {response}")

            #Use response as input for other bot
            other_bot.add_message(response, current_bot.name)

            #Switch turns
            current_bot, other_bot = other_bot, current_bot


# Prompt for the debate
prompt = "Recent Iran-Israel missile crisis"
debate(Democrat, Republican, prompt)

# At the end, output the histories to JSON format
output_data = {
    "Democrat": Democrat.history,
    "Republican": Republican.history,
}

# Write the JSON output to a file
with open("chat_history.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4)  # Save as JSON with pretty printing

print("Chat histories saved to chat_history.json.")


