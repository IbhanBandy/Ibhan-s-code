import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure you set your OpenAI API key in the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = input("Ibhan: ")
    if message:
        messages.append({"role": "user", "content": message})
        
        # Call the ChatCompletion API with streaming enabled
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True
        )
        
        print("ChatGPT: ", end="", flush=True)
        collected_messages = ""
        
        # Stream and print the response as it's generated
        for chunk in response:
            if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content is not None:
                chunk_message = str(chunk.choices[0].delta.content)
                print(chunk_message, end="", flush=True)
                collected_messages += chunk_message
        
        print()  # Print a newline after the response is complete
        
        # Append the assistant's reply to the messages list
        messages.append({"role": "assistant", "content": collected_messages})
