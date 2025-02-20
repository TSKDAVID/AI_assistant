from groq import Groq

client = Groq(api_key="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")
def chat_with_ai(user_input):
    chat_completion = client.chat.completions.create(
        #
        # Required parameters
        #
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],

        model="deepseek-r1-distill-llama-70b-specdec",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return(chat_completion.choices[0].message.content)
