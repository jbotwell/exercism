def recite(start_verse, end_verse):
    results = []
    for v in range(start_verse - 1, end_verse):
        results.append(make_verse(v))
    return results


def make_verse(end):
    poem = []
    for c in range(end, -1, -1):
        poem.append(characters[c])
    return "This is " + " ".join(poem)


characters = [
    "the house that Jack built.",
    "the malt that lay in",
    "the rat that ate",
    "the cat that killed",
    "the dog that worried",
    "the cow with the crumpled horn that tossed",
    "the maiden all forlorn that milked",
    "the man all tattered and torn that kissed",
    "the priest all shaven and shorn that married",
    "the rooster that crowed in the morn that woke",
    "the farmer sowing his corn that kept",
    "the horse and the hound and the horn that belonged to",
]
