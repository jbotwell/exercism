def find_anagrams(word, candidates):
    word_count = make_char_counts(word)

    results = []
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        if word_count == make_char_counts(candidate):
            results.append(candidate)

    return results


def make_char_counts(word):
    results = {}
    for c in word.lower():
        try:
            results[c] += 1
        except KeyError:
            results[c] = 1

    return results
