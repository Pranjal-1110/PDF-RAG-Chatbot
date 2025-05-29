# PDF-RAG-Chatbot

**PDF-RAG-Chatbot** is a Python-based application that enables users to interactively query PDF documents using a Retrieval-Augmented Generation (RAG) approach. By combining document retrieval techniques with the capabilities of Large Language Models (LLMs), this chatbot provides contextually relevant answers to user queries based on the content of uploaded PDFs.

---

##  Features

- **PDF Upload**: Seamlessly upload and process PDF documents.  
- **Contextual Q&A**: Pose questions related to the uploaded PDF and receive accurate, context-aware responses.  
- **RAG Architecture**: Utilizes Retrieval-Augmented Generation to fetch pertinent information from the document before generating responses.  
- **User-Friendly Interface**: Interact with the chatbot through a simple and intuitive interface.  

---
## Project Structure


PDF-RAG-Chatbot Project Structure<br>
PDF-RAG-Chatbot/<br>
├── components/          # Modular components for PDF processing and chatbot functionality<br>
│   ├── __pycache__/     # Python cache directory<br>
│   ├── chatbot.py       # Chatbot functionality<br>
│   ├── pdf_parser.py    # PDF parsing component <br> 
│   ├── prompt.py        # Prompt engineering component<br>
│   ├── text_chunker.py  # Text chunking component<br>
│   └── vectorstore.py   # Vector store management<br>
├── app.py              # Main application script<br>
├── req.txt             # List of required Python packages<br>
└── README.md           # Project documentation



