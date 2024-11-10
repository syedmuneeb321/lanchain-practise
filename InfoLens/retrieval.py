from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from model import setup_llm 
from prompt import prompt_template 



def retrival_chain_create(vectors):
    """
        Creates a retrieval chain using the language model, prompt template, and document embeddings.

    """

    # Step 1: Initialize the language model and prompt template

    llm = setup_llm()

    # Step 2: Create a document chain with the language model and prompt template
    document_chain = create_stuff_documents_chain(llm=llm,prompt=prompt_template)

    # Step 3: Set up a retriever from the vector store

    retriever = vectors.as_retriever()

    # Step 4: Create the retrieval chain combining the retriever and document chain

    retrieval_chain = create_retrieval_chain(retriever,document_chain)

    return retrieval_chain 


def get_response(retrieval_chain, user_prompt):
    """
        Retrieves a response from the retrieval chain based on the user's prompt.
    """

    response = retrieval_chain.invoke({"input":user_prompt})

    return response 






