import streamlit  as st
import time 
from loader import load_document 
from embedding import create_vector_embedding 

from retrieval import retrival_chain_create, get_response 



if "vectors" not in st.session_state:
    st.session_state.vectors = None 


st.title("RAG Document Q&A with Groq and Llama3")


with st.sidebar:
    st.header("Document Loader")
    if st.button("Load Documents"): 
        loader = load_document("./research_papers")
        # step 2: create vector embeddings
        st.session_state.vectors = create_vector_embedding(loader=loader)
        st.write("Vector Database is ready")



if st.session_state.vectors is not None:
    if user_prompt := st.chat_input("Ask a question about your documents"): 
        # Step 3: Initialize the retrieval chain
        retrieval_chain = retrival_chain_create(vectors=st.session_state.vectors)

        # Step 4: Get the response from the retrieval chain
        start = time.process_time()
        response = get_response(retrieval_chain=retrieval_chain,user_prompt=user_prompt)
        response_time = time.process_time() - start

        # Step 5: Display the response 
        st.chat_message("user").write(user_prompt)
        st.chat_message("assistant").write(response)
        st.write(f"Response Time: {response_time:.2f} seconds")


