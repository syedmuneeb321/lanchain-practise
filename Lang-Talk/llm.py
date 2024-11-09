from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser 
from prompt import prompt 

def generate_responose(question:str,api_key:str,llm_model:str,max_tokens:int,temperature:float):
    if llm_model == "gemini":
        model = ChatGoogleGenerativeAI(
            api_key=api_key,
            model="gemini-1.5-flash",
            temperature=temperature,
            max_tokens=max_tokens
        )
    if llm_model == "gpt-4o-mini":
        model = ChatOpenAI(
            model_name="gpt-4o-mini",
            api_key=api_key,
            temperature=temperature,
            max_tokens = max_tokens

        ) 
    
    if llm_model == "llama3":
        model = ChatGroq(
            model="llama-3.1-70b-versatile",
            temperature=temperature,
            api_key=api_key,
            max_tokens=max_tokens
        )

    chain = prompt | model | StrOutputParser()

    return chain.invoke({"question":question})

    