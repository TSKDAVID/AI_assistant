import math
import os 
import pathlib 
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")

# Load chat history (in-memory, can be extended to file-based)
history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_ai(user_input):
    """Sends user input to Groq AI and returns the response."""
    history.append({"role": "user", "content": user_input})

    stream = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # Adjust to your preferred model
        messages=history,
        temperature=0.5,
        max_completion_tokens=4096,
        stream=True,
    )

    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()  # Print newline after response
    history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    print("AI Chat: Type 'exit' to end")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break
        chat_with_ai(user_input)
