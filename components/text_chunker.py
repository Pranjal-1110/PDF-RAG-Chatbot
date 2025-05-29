from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    return splitter.split_text(text)
    