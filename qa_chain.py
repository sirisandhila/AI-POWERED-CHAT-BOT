from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document

def run_qa_chain(question: str, docs: list[Document]):
    llm = ChatOpenAI(model_name="gpt-4")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=lambda _: docs, return_source_documents=False)
    return qa.run(question)
