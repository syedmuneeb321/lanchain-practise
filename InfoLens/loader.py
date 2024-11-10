from langchain_community.document_loaders import PyPDFDirectoryLoader 


def load_document(directory_path:str = "research_papers"):
    """
    Loads PDF documents from the specified directory.
    """
    loader = PyPDFDirectoryLoader(directory_path)
    return loader 


