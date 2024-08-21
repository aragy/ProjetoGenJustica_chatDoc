from langchain_community.vectorstores import FAISS
from .singleton_embedding  import FastEmbedEmbeddingsSingleton


def store_chunks(chunks: list[str]):
    embeddings = FastEmbedEmbeddingsSingleton().embeddings
    db = FAISS.from_texts(chunks, embeddings)
    db.save_local('./FAISSDB')

def search_similar_chunks(query: str, k: int = 5):
    embeddings = FastEmbedEmbeddingsSingleton().embeddings
    db = FAISS.load_local('./FAISSDB', embeddings,allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k)
    return [result.page_content for result in results]
