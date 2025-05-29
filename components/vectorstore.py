from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def get_vectorstore(chunked_text):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunked_text , embedding=embeddings)