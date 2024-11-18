from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from logger import get_logger 

logger = get_logger(__name__) 

def initialize_tools():
    """
    Initialize tools
    """

    try: 
        logger.info("Initializing tools")

        arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
        arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

        wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
        wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

        search = DuckDuckGoSearchRun(name="search")

        logger.info("Tools initialized successfully")

        return [arxiv, wiki, search]


    
    except Exception as e:
        logger.error(f"Error initializing tools: {e}")  
        return None 
