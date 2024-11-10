from langchain_core.prompts import ChatPromptTemplate


# Define the prompt template

prompt_template = ChatPromptTemplate.from_template( 
    """
    Answer the questions based on the provided context only.
    please provide the most accurate response based on the question.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

