# word_embed.py
import gensim.downloader as api

# Load pretrained word embedding model (GloVe)
word_model = api.load("glove-wiki-gigaword-100")


def get_similar_words(word: str, top_n=5):
    """
    Returns semantically similar words using embeddings.
    """
    if word in word_model:
        similar = word_model.most_similar(word, topn=top_n)
        print("candidates: ",similar)
        return [w for w, score in similar]
        
    return []
