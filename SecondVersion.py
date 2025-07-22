# Import necessary libraries or modules for API interaction
import json
from openai import OpenAI

# Initialize API client with authentication details
client = OpenAI(
    api_key="sk-0JVspnhOLC",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# Define a class to analyze news articles for sentiment and entity extraction
class NewsAnalyzer:
    # Initialization method that takes a list of articles
    def __init__(self, articles):
        self.articles = articles

    # Method for sentiment analysis of a given text
    def sentiment_analysis(self, text):
        # Detailed prompt for sentiment analysis with examples
        completion = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {
                    "role": "assistant",
                    "content": (
                        "Perform a detailed sentiment analysis on the given text. "
                        "Determine whether the sentiment expressed is positive, negative, or neutral. "
                        "Consider the following criteria:"

                        "1. **Tone of Writing**:  "
                        "Analyze the overall mood conveyed by the text. For example,"
                        "   - A cheerful and upbeat tone might suggest positive sentiment ('The event was a great success!').\n"
                        "   - A pessimistic or somber tone might indicate negative sentiment ('The results were disastrous.').\n\n"

                        "2. **Emotionally Charged Words**: "
                        "Identify words or phrases that evoke strong emotions. For instance,"
                        "   - Positive words: 'amazing', 'thrilled', 'accomplished'."
                        "   - Negative words: 'terrible', 'failure', 'regret'."
                        "   - Neutral words: 'normal', 'standard'. Provide examples where applicable."

                        "3. **Contextual Phrases**:"
                        "Evaluate the context in which certain phrases are used. Sometimes the sentiment is influenced by what surrounds key phrases.\n"
                        "   - Positive context: 'Despite the challenges, the team was victorious'."
                        "   - Negative context: 'Due to many setbacks, the team failed to deliver'."

                        "Provide reasoning or examples from the text that support your assessment of the sentiment. "
                        "Explain any keywords or contextual phrases that influenced your analysis."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        # Retrieve and process the sentiment result from the LLM's response
        result = completion.choices[0].message.content
        # Return the sentiment analysis outcome
        return result

    # Method for extracting entities from a given text
    def entity_extraction(self, text):
        completion = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "assistant", "content": "Extract entities from text."},
                {"role": "user", "content": text}
            ]
        )
        # Retrieve and process the entities result from the LLM's response
        result = completion.choices[0].message.content
        # Return the entities extracted from the text
        return result

    # Method to analyze all articles
    def analyze_articles(self):
        # Initialize a results dictionary for storing sentiment and entities information
        results = {}
        # Iterate over each article
        for idx, article in enumerate(self.articles):
            # Perform sentiment analysis and entity extraction for each article
            sentiment = self.sentiment_analysis(article)
            entities = self.entity_extraction(article)
            # Store results in the dictionary using appropriate keys
            results[f"Article {idx + 1}"] = {"sentiment": sentiment, "entities": entities}

        # Return the compiled analysis results
        return results

# Retrieve or define your list of news articles
articles = [
    "The recent election results have sparked widespread debate among citizens.",
    "The local wildlife conservation efforts have seen a significant boost."
]
# Create an instance of the NewsAnalyzer class, passing in the articles
news_analyzer = NewsAnalyzer(articles)
# Call the method to analyze articles and store the results
analysis_results = news_analyzer.analyze_articles()
# Write the analysis results to a JSON file for structured data representation
json_output = json.dumps(analysis_results, indent=1)
# Confirm that the results have been saved successfully
print(json_output)
