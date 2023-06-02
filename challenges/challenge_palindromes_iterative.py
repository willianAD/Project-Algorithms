def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    word = word.lower()
    word = word.replace(" ", "")
    invertida = word[::-1]

    return word == invertida
