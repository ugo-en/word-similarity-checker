from fuzzywuzzy import fuzz as fz


def score(word1,word2):
    """
    This function uses a sequence matcher to check the two words and using the token set ratio, determine the similarity
    in structure between two words, statements or phrases
    :param word1:
    :param word2:
    :return:
    """
    word1 = str(word1).lower().strip() if word1 is not None else ''
    word2 = str(word2).lower().strip() if word2 is not None else ''
    if word1 == word2:
        return 100
    else:
        return f"{word1} and {word2} are {fz.token_set_ratio(word1, word2)}% similar."
