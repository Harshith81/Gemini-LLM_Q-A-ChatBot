# # This file can be used for interacting with gemini-pro model
# # only in the form of text as input it does not accept any other input formats, in simple terms 
# # it can be considered as a chatbot (text) and if we want to include images as input 
# # and need to interact with model to get summary or description about the input image then we need to use gemini-pro-vision   
# #check out vision.py
  
# 1. This will accept both text input from the user and also capable of processing any articles, blogs and give detailed summary or description about them.  

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(question):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q/A Text ChatBot")
st.header("Gemini-LLM Q/A Text ChatBot 💬")
input=st.text_input("Type your Input: ",key="input")
submit=st.button("Ask Question? ")

if submit:
    response=get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)         
   
   



