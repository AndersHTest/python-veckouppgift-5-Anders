def count_words(sentence):
    if sentence == "":
        return None
    elif sentence != "":
        words = sentence.split(" ")
        return len(words)
    else:
        return None