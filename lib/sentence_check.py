def sentence_check(string):
    punctuation = ['!', '?', '.']
    if len(string) == 0:
        return False
    if string[0].isupper() and string[-1] in punctuation:
        return True
    else:
        return False