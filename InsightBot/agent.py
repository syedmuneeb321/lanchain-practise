# import logging
from logger import get_logger
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from tools import initialize_tools

logger = get_logger(__name__)


def process_user_input(api_key, prompt, messages,callbacks=None):
    """
    Initialize agent
    """
    try:
        # logger.info("Initializing agent")

        tools = initialize_tools()
        if not tools:
            logger.error("Tools failed to initialize.")
            return "Sorry, I couldn't initialize my tools. Please check the logs."


        llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-70b-versatile", streaming=True)


        search_agent = initialize_agent(
            tools=tools,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            handle_parsing_errors=True
        )

        # logger.info("Agent initialized successfully")
        messages.append({"role": "user", "content": prompt})

        response = search_agent.run(messages,callbacks=callbacks)

        logger.info("Response generated successfully.")  # Log successful response

        messages.append({"role": "assistant", "content": response})

        return response


    
    except Exception as e:
        logger.error(f"Error initializing agent: {e}")
        return None
        