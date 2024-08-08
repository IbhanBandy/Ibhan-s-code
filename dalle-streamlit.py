import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def dalle_completion(user_prompt):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=user_prompt,
        n=1,
        size="1024x1024",
    )
    image_url = response.data[0].url
    return image_url

st.title("DALL-E Streamlit")

message = st.text_area("Write a description of the image you would like to generate...")
button = st.button("Create Image")

if button and message:
    response = dalle_completion(message)
    st.image(response, caption="Your Image")