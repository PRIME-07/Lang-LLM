# Using llama3 (Ollama)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv


# Load files from .evn file
load_dotenv()


# LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the queries"),
        ("user", "Question:{question}") 
    ]
) 


# Streamlit Framework
st.title("LangChain Demo")
input_text = st.text_input("Ask Me Anything ")


# Ollama llama3 LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))