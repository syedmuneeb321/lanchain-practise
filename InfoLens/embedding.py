from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS



def create_vector_embedding(loader: any):
    """
    Creates vector embeddings from loaded documents and stores them in a FAISS vector store.
    """

    # Step 1: Initialize the Hugging Face Embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Step 2: Load documents using the provided loader
    docs = loader.load()

    # Step 3: Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)

    # Step 4: Create FAISS vector store
    vectors = FAISS.from_documents(documents=final_documents,embedding=embeddings)

    return vectors 


    
