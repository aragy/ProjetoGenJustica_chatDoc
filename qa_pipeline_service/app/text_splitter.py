from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks
