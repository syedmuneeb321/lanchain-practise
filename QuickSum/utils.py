import validators
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader 
from logger import get_logger


logger = get_logger(__name__)

def get_content_from_url(url):

    if not validators.url(url):
        logger.error(f"Invalid URL: {url}")
        raise ValueError(f"Invalid URL: {url}")

    if "youtube.com" in url:

        loader = YoutubeLoader.from_youtube_url(url)

    else:
        
        loader = UnstructuredURLLoader(urls=[url],ssl_verify=False,headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
    logger.info(f"Loading content from URL: {url}")
    docs = loader.load()
    logger.info(f"Content loaded from URL: {url}")

    return docs 

# print(get_content_from_url("https://ai.gov.uk/blogs/welcome-to-the-i-ai-blog/"))