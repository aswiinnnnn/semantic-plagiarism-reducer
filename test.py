from nlp_preprocess import parse_sentence
from filter_replaceable import filter_replaceable_tokens
from replace_best_match import semantic_replace_word

s = "Replaces a word with the best semantic candidate and returns the final transformed sentence."
sc = s
tokens = parse_sentence(s)
replaceable = filter_replaceable_tokens(tokens)
print("\n\n\n\n")
for r in replaceable:
    s = semantic_replace_word(s,r["word"])
    print("replaced ",r["lemma"],"::: ",s)
    
print("original sentence: ",sc)
print("transformed sentence: ",s)



