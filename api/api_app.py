from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# FastAPI App
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Initialize models
model = ChatOpenAI()
llm = Ollama(model="llama3")

# Define prompts
prompt1 = ChatPromptTemplate.from_messages([
    "Write me an essay about {topic} with 100 words"
])

prompt2 = ChatPromptTemplate.from_messages([
    "Write me a poem about {topic} with 100 words"
])

# Add routes
add_routes(
    app,
    model,
    path="/openai"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay")

add_routes(
    app,
    prompt2 | llm,
    path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
