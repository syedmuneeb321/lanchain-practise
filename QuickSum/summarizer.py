

from logger import get_logger 


logger = get_logger(__name__) 


from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from logger import get_logger


def get_summary(docs,groq_api_key):
    try:
        llm = ChatGroq(api_key=groq_api_key,model="llama-3.1-70b-versatile")
        prompt_template ="""
provide a summary of the following content:
Content: {text}
"""

        prompt = PromptTemplate(template=prompt_template,input_variables=["text"])

        chain = load_summarize_chain(llm=llm,prompt=prompt,chain_type="stuff")

        logger.info("Summarizing content...")
        summary = chain.run(docs)
        logger.info("content successfully summarized")
        
        return summary
    except Exception as e:
        logger.error(f"Error in generated summary: {e}")
        raise e 