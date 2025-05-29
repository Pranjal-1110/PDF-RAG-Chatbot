from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI


def get_chat_chain(vectorstore, prompt_template):
    llm = ChatOpenAI(model="gpt-4o-mini")
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(return_messages=True)

    #prompt template using LCEL
    prompt = ChatPromptTemplate.from_template(
        prompt_template.template  
    )

    #extract relevant documents
    def extract_context(docs: list) -> str:
        return "\n\n".join(doc.page_content for doc in docs)

    #rag using lcel
    rag_chain = (
    {
        "context": retriever | RunnableLambda(extract_context),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
    return rag_chain, memory
