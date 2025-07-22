
from openai import OpenAI
import random

# Initialize client
client = OpenAI(
    api_key="sk-0JVspnhOLC",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# Simulate a function to get random weather
def get_current_weather(arguments):
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    selected_weather = random.choice(weather_conditions)
    location = arguments["location"]
    return f"The weather in {location} is {selected_weather}."


messages = [
    {"role": "assistant", "content": "You are a helpful assistant "
                                     "that can provide weather conditions of a city."},
    {"role": "user", "content": "What is the weather like in Shanghai?"}
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Cities or counties.",
                    }
                },
                "required": ["location"]
            }
        }
    }
]


# Simulate the process of the LLM deciding to call a tool
def simulate_llm_decision(messages, tools):
    last_message = messages[-1]["content"]
    if "weather" in last_message.lower():
        # Extract location and call the corresponding function
        location = last_message.split()[-1].strip("?")
        tool_function = get_current_weather
        tool_arguments = {"location": location}
        weather_info = tool_function(tool_arguments)

        # Simulate adding tool output as an assistant's response
        messages.append({"role": "assistant", "content": weather_info})
        return weather_info
    else:
        return "I can't handle this request."


# Run the simulation
response = simulate_llm_decision(messages, tools)
print(response)
