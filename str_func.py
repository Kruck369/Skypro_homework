def uppercase_string(word):
    """получает строку и делает все буквы заглавным"""
    uppercase_word = word.upper()
    return uppercase_word


def capitalize_words(string):
    """получает строку и делает все первые буквы слов заглавными"""
    new_string = ' '.join(word[0].upper() + word[1:] for word in string.split())
    return new_string
