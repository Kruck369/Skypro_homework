def uppercase_string(word):
    """получает строку и делает все буквы заглавными"""
    uppercase_word = word.upper()
    return uppercase_word


def title_sentence(string):
    """получает строку и делает первые буквы слов заглавными"""
    title_words = ' '.join(word[0].upper() + word[1:] for word in string.split())
    return title_words
