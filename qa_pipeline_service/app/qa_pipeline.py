from langchain.chains import VectorDBQA
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from .singleton_embedding  import FastEmbedEmbeddingsSingleton


def get_answer(question: str) -> str:
    embeddings = FastEmbedEmbeddingsSingleton().embeddings
    db = FAISS.load_local('./FAISSDB', embeddings,allow_dangerous_deserialization=True)
    llm = Ollama(model="llama3.1")
    
    qa_chain = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=db)
    response = qa_chain({"query": question})
    
    return response['result']
