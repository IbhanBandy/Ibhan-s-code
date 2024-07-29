import openai
import os
import pyttsx3
from dotenv import load_dotenv

load_dotenv()

# Initialize the GPT engine with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_gpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",  # Use the gpt-4 model
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Queue the text to be spoken
    engine.say(text)

    # Run the speech engine
    engine.runAndWait()

if __name__ == "__main__":
    # Get user input
    user_input = input("Ibhan: ")

    # Get response from GPT-4 (or any other specified model)
    gpt_response = chat_gpt_response(user_input)
    print(f"GPT-4 says: {gpt_response}")

    # Convert the GPT-4 response to speech
    text_to_speech(gpt_response)