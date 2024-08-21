from langchain_community.embeddings.fastembed import FastEmbedEmbeddings


class FastEmbedEmbeddingsSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FastEmbedEmbeddingsSingleton, cls).__new__(cls)
            cls._instance._init_once(*args, **kwargs)
        return cls._instance

    def _init_once(self, *args, **kwargs):

        self.embeddings = FastEmbedEmbeddings()
