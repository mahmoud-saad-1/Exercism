from collections import Counter
import string

def count_words(sentence):
    exceptions = string.punctuation
    exceptions = exceptions.replace("'", "")
    spaces = " " * len(exceptions)
    counter = sentence.translate(str.maketrans(exceptions, spaces)).lower().split()

    cleaned_words = []
    for word in counter:
        stripped = word.strip("'")
        if stripped !=  "":
            cleaned_words.append((stripped))
    count = dict(Counter(cleaned_words))
    return count
