REPLACE_POS = {"NOUN", "VERB", "ADJ", "ADV"}

def filter_replaceable_tokens(tokens):
    """
    Filters tokens to find only replaceable (meaning-carrying) words.
    
    Input:
        tokens = output from parse_sentence()
    
    Output:
        replaceable_tokens = list of token dicts
    """
    replaceable = []

    for token in tokens:
        if token["pos"] in REPLACE_POS:
            replaceable.append(token)

    return replaceable
