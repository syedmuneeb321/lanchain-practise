import streamlit as st 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import ChatPromptTemplate 
import os 
from llm import generate_responose
from dotenv import load_dotenv 

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"



st.title("LangTalk")


st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Please enter your google or openai or groq API key:",type="password")
model = st.sidebar.selectbox("Please select a model:",["gemini","gpt-4o-mini","llama3"])
temperature = st.sidebar.slider("Please select a temperature:",0.0,1.0,0.5)
max_tokens = st.sidebar.slider("Please select a max tokens:",0,4096,1024)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [] 


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if api_key:
    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role":"user","content":prompt})
        try:
            response = generate_responose(
                question=prompt,
                api_key=api_key,
                llm_model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Display assistant's response and add to history
            with st.chat_message("assistant"):
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Specific error messages without appending to chat history
        except ValueError as ve:
            st.error(f"Input error: {ve}. Please check your inputs and try again.")
        except KeyError as ke:
            st.warning("API key error: Missing or invalid API key. Please enter a valid key.")
        except ConnectionError:
            st.warning("Network error: Unable to connect to the server. Please check your internet connection.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
else:
    st.warning("Please enter your API key.")
        




