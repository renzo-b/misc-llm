from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true" # for langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant. Please respond to the user queries."),
        (
            "human", "Question:{question}"
        )
    ]
)

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

# LLM
llm = ChatOllama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))