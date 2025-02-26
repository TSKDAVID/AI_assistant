import os
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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") # Replace with your actual key

# Chat history (in-memory)
history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_ai(user_input, update_callback):
    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Replace with your desired model
        messages=history,
        temperature=0.5,
        max_completion_tokens=32768,
        stream=True,
    )

    full_response = ""
    for chunk in response:  # Iterate directly over the generator
        if chunk.choices[0].delta.content:  # Check if content exists
            content = chunk.choices[0].delta.content
            full_response += content
            update_callback(content)

    history.append({"role": "assistant", "content": full_response})
    update_callback("", is_final_chunk=True)  # Signal end of AI message
    return full_response