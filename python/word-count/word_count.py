import re


def count_words(sentence: str) -> dict[str, int]:
    words = re.split(r"[ \t\n_.,:!?&@$%^]", sentence)

    counts = {}
    for word in words:
        word = word.lower().strip("'")
        if word == "":
            continue
        try:
            counts[word] += 1
        except KeyError:
            counts[word] = 1

    return counts
