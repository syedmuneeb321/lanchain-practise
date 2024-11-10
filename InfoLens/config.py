import os 
from dotenv import load_dotenv

load_dotenv() 

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")