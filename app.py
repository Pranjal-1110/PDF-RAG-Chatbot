import streamlit as st
from components.pdf_parser import extract_text_from_pdf
from components.text_chunker import chunk
from components.vectorstore import get_vectorstore
from components.chatbot import get_chat_chain
from components.prompt import get_custom_prompt
import os

st.set_page_config(page_title="📄 Chat with your PDF", layout="wide")
st.title("📄 Chat with your PDF")

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    os.makedirs("data", exist_ok=True)  
    with open("data/temp.pdf", "wb") as f:
        f.write(pdf.read())

    raw_text = extract_text_from_pdf("data/temp.pdf")
    chunks = chunk(raw_text)
    vectorstore = get_vectorstore(chunks)

    custom_prompt = get_custom_prompt()
    chain, memory = get_chat_chain(vectorstore, custom_prompt)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input("Ask something about the document")

    if user_question:
        response = chain.invoke(user_question)
        memory.chat_memory.add_user_message(user_question)
        memory.chat_memory.add_ai_message(response)
        st.session_state.chat_history.append(("You", user_question))
        st.session_state.chat_history.append(("Bot", response))

    for speaker, message in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {message}")