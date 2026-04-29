import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()


def classify_with_llm(log_message):
    """
    Classifies a given log message using a Large Language Model (LLM) into predefined categories.
    This function constructs a prompt for the LLM to classify the log message into one of the specified categories:
    - Workflow Error
    - Deprecation Warning
    If the log message does not fit any category, it returns "Unclassified". The function interacts with an LLM API
    (assuming 'client' is a pre-configured API client, e.g., for Groq or similar) to generate the classification.
    Args:
        log_message (str): The log message string to be classified.
    Returns:
        str: The classification category as a string, such as "Workflow Error", "Deprecation Warning", or "Unclassified".
             The response is directly from the LLM, with no additional preamble.
    Raises:
        Any exceptions raised by the 'client.chat.completions.create' method, such as API errors or network issues,
        are not handled here and should be managed by the caller.
    Note:
        - The 'client' variable must be defined and configured externally (e.g., with API keys and endpoints).
        - The model used is "llama-3.3-70b-versatile"; ensure compatibility with the client.
        - This function relies on external API calls, which may incur costs or have rate limits.
    """

    prompt = f"""Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, return "Unclassified".
    Only return the category name. No preamble.
    Log message: {log_message}"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    print(classify_with_llm("Error: Workflow failed due to timeout."))
    print(
        classify_with_llm(
            "Warning: The function 'foo' is deprecated and will be removed in future versions."
        )
    )
    print(classify_with_llm("just chilling here bro."))
