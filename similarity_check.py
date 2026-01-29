from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load sentence embedding model
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

def sentence_similarity(sentence1: str, sentence2: str):
    """
    Computes semantic similarity between two sentences.
    
    Returns:
        similarity score between 0 and 1
    """
    # Encode sentences into semantic vectors
    vec1 = sentence_model.encode(sentence1)
    vec2 = sentence_model.encode(sentence2)

    # Reshape for cosine similarity
    v1 = np.array(vec1).reshape(1, -1)
    v2 = np.array(vec2).reshape(1, -1)

    # Compute cosine similarity
    similarity = cosine_similarity(v1, v2)[0][0]

    return similarity
