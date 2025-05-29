from langchain.prompts import PromptTemplate

def get_custom_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a PDF expert. Use the context below to answer the question.

Context:
{context}

Question:
{question}

If the answer is not in the context, say "I couldn’t find that information in the document."
"""
    )
