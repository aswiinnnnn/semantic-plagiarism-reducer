import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_sentence(sentence: str):
    """
    Parses a sentence into structured tokens.
    
    Returns:
        [
            {
                "text": original word,
                "pos": part of speech,
                "lemma": base form of word
            },
            ...
        ]
    """
    doc = nlp(sentence)
    tokens = []

    for token in doc:
        tokens.append({
            "text": token.text,      # original word
            "pos": token.pos_,       # grammatical role
            "lemma": token.lemma_,   # base form
        })

    return tokens
