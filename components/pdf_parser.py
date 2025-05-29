from langchain.document_loaders import PyPDFLoader

def extract_text_from_pdf(path):
    loader = PyPDFLoader(path)
    documents = loader.load()
    return " ".join([doc.page_content for doc in documents])