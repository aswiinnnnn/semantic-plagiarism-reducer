from find_similar_list import get_similar_words
from similarity_check import sentence_similarity

def semantic_replace_word(original_sentence, target_word, top_n=5):
    """
    Replaces a word with the best semantic candidate
    and returns the final transformed sentence.
    """
    candidates = get_similar_words(target_word, top_n=top_n)
    

    best_sentence = original_sentence
    best_score = -1

    for cand in candidates:
        temp_sentence = original_sentence.replace(target_word, cand)
        score = sentence_similarity(original_sentence, temp_sentence)

        if score > best_score:
            best_score = score
            best_sentence = temp_sentence

    return best_sentence
