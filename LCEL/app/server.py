from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq 
import os 
from langserve import add_routes 
from dotenv import load_dotenv 

load_dotenv()  # take environment variables from .env.

groq_api_key: str = os.getenv("GROQ_API_KEY") 

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.0,
    groq_api_key=groq_api_key,
)


system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{input}")
])


parser = StrOutputParser()


chain = prompt_template | llm | parser 


app = FastAPI(
    title="Langserver",
    version="0.1.0",
    description="Langchain server for Langserve",
)


add_routes(
    app,
    chain,
    path="/langserve/chain",
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,
                host="127.0.0.1",
                port=8000
                )



