import os

import openai
from dotenv import load_dotenv
import streamlit as st
import base64
import requests
load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Streamlit interface
st.title("Image Description with GPT")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
user_input = st.text_area("Ask your question here...")
button = st.button("Generate Response")
if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    
if button and user_input and uploaded_file is not None:
    # Display the uploaded image

    # Encode the image
    base64_image = base64.b64encode(uploaded_file.read()).decode('utf-8')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    with st.spinner('Analyzing the image...'):
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            description = result['choices'][0]['message']['content']
            st.write(description)
        else:
            st.write("No description returned by the model.")
    else:
        st.write("Error:", response.json())
else:
    st.write("Please upload an image file.")