import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

# start chat
while True:
    # user input
    message = input("Ibhan: ")
    if message:
        messages.append({"role": "user", "content": message})
        
        # create assistant
        response = openai.images.generate(
            model="dall-e-3",
            prompt=message,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        print("Dall-E: ", end="", flush=True)
        
        # Generate and print assistant response
        image_url = response.data[0].url
        print(image_url)
        
        print()  # Print a newline after the response is complete
