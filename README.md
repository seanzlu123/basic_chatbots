Project Files Overview

1. Debate Chatbot File
This file defines a conversational debate simulator between two chatbot agents (Democrat and Republican).
Key features include:

Each agent is initialized with a political persona and an initial prompt.
The agents exchange responses in turns, leveraging the LLM API for generating replies.
The conversation is structured as a debate around a selected prompt and recorded turn by turn.
At the end, the chat histories of both agents are saved to a JSON file.

---------------------------------------------------------------------------------------------------------
2. NewsAnalyzer File
This file implements a NewsAnalyzer class that uses a language model API to analyze news articles. It performs two main NLP tasks on each article:

Sentiment Analysis: Classifies each article as positive, negative, or neutral, along with reasoning.
Entity Extraction: Identifies key entities mentioned in each article.


---------------------------------------------------------------------------------------------------------
3. Weather Function Tool Simulation
This file demonstrates how a language model can "call a tool" (function) as part of a conversation flow:

Simulates processing of a user asking about the weather in a city.
Defines a mock function for getting random weather, and the logic for using it based on the user request.
Shows how tool-like capabilities can be integrated into a messaging-based language model workflow.
