from huggingface_hub import login # type: ignore
login() # You will be prompted for your HF key, which will then be saved locally
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
import numpy as np
import random
import time
from langchain_community.llms import Ollama




load_dotenv()

os.environ["HUGGING_FACE_API_KEY"] = os.getenv("HUGGING_FACE_API_KEY")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"


##creating chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. Please provide response to the user's queries very comprehensively"),
    ("user","Question:{question}")
])

##streamlit framework

# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #FFFFFF !important;
#         color: #262730 !important;
#     }
#     .reportview-container,
#     .main,
#     .block-container {
#         background-color: #FFFFFF !important;
#         color: #262730 !important;
#     }
#     .sidebar .sidebar-content {
#         background-color: #F0F2F6 !important;
#         color: #262730 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# Streamlit frontend

st.title("Chatbot Interface")
input_text=st.text_input("Search the topic you want")


# Hugging Face AI LLM call
llm = Ollama(model='llama2')
    # pipeline_kwargs={
    #     "max_new_tokens": 100,
    #     "top_k": 50,
    #     "temperature": 0.1,
    # },

output_parser=StrOutputParser()

# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
# llm.invoke("Hugging Face is")