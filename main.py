from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating captions

caption_template = "Give me {number} captions on {topic}"

caption_prompt = PromptTemplate(template = caption_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
caption_chain = caption_prompt | gemini_model


import streamlit as st

st.header("YT caption Generator -By Vena")

st.subheader("Generate Youtube captions using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of captions ", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    captions = caption_chain.invoke({"number" : number, "topic" : topic})
    st.write(captions.content)
    
