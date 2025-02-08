from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI,ChatAnthropic
from dotenv import load_dotenv
from langserve import add_routes
import os

app = FastAPI(
    title="LangChain Server",
    version=1.0,
    description = "A simple api server using Langchain's Runnable Interface"
    
)

add_routes(
    app,
    ChatOpenAI(model = "gpt-3.5-turbo-0125"),
    path = "/openai"
)

add_routes(
    app,
    ChatAnthropic(model = "claude-3-haiku-20240307"),
    path = "/anthropic"
)
model = ChatAnthropic(model="claude-3-haiku-20240307")
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

add_routes(
    app,
    prompt | model,
     path="/joke",
    
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)