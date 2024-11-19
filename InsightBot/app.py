import streamlit as st 
from logger import get_logger 

from langchain.callbacks import StreamlitCallbackHandler
from agent import process_user_input


logger = get_logger(__name__)


st.title("InsightBot - Chat with Search")
st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your groq API key", type="password") 


if "messages" not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant", "content": "Hello! How can I help you?"}] 


logger.info("Application started successfully")


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"]) 




if prompt:= st.chat_input(placeholder="Ask me anything!"):
    if api_key:
        st.chat_message("user").write(prompt) 

        st.session_state.messages.append({"role": "user", "content": prompt})


        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)

            response = process_user_input(api_key=api_key,prompt=prompt,messages=st.session_state.messages,callbacks=[st_cb])

            st.write(response)

            st.session_state.messages.append({"role": "assistant", "content": response})

    else:
        st.warning("Please enter your Groq API key in the sidebar.")

      
