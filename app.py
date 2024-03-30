# Q&A Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

import streamlit as st
import os

## Function to load OpenAI model to get resposnes
## replace gpt-3.5-turbo-instruct wiht text-davinci-003
def get_openai_response(question):
	llm=OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.5,openai_api_key=os.getenv("OPENAI_API_KEY"))
	response=llm(question)
	return response
    
## Initialize our streamlitapp
st.set_page_config(page_title="Q & A Demo")
st.header("Langchain Appliation")

input = st.text_input("Input :", key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

#@ if the ask button is clicked

if submit:
	st.subheader("The Response is")
	st.write(response)
