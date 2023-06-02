def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    word = word.lower()
    word = word.replace(" ", "")
    if high_index <= 1:
        return True
    elif word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
