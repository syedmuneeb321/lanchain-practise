from langchain_core.prompts import ChatPromptTemplate 



prompt = ChatPromptTemplate.from_messages([
    ("system","you are a helpfull assistant please anwser user query."),
    ("human","Question: {question}")
])