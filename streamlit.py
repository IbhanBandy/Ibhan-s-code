import os


import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


# configure streamlit page

st.set_page_config(
    page_title = "Chat GPT",
    layout = "centered"

)

# initialize chat session

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("ChatGPT-4o streamlit")

# show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# feild for user input message

user_prompt = st.chat_input("Ask a question here...")

# add user message to chat history

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    
    # send imput to chatgpt for response

    response = openai.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": "You are an intelligent assistant."},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # show chatgpt's resoponse

    with st.chat_message("assistant"):
        st.markdown(assistant_response)    