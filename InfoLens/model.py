from langchain_groq import ChatGroq
from config import GROQ_API_KEY 



def setup_llm():
    """
    Sets up the Large Language Model (LLM) for the chatbot.
    """

    llm = ChatGroq(api_key=GROQ_API_KEY,model="llama-3.1-70b-versatile")

    return llm 
