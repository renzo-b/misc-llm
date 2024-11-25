from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from langserve import add_routes
from langchain_ollama import ChatOllama

import uvicorn
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="simple API server"
)


add_routes(app, ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPEN_API_KEY"]), path="/openai")

model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPEN_API_KEY"])
model_llama = ChatOllama(model="llama2")

# Prompt template
prompt1 = ChatPromptTemplate.from_template("write me a sentence about {topic}")
prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic}")


add_routes(app, prompt1 | model, path="/sentence")
add_routes(app, prompt2 | model_llama, path="/poem")

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)