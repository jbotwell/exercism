verses = (
    ("first", "and a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves, "),
    ("third", "three French Hens, "),
    ("fourth", "four Calling Birds, "),
    ("fifth", "five Gold Rings, "),
    ("sixth", "six Geese-a-Laying, "),
    ("seventh", "seven Swans-a-Swimming, "),
    ("eighth", "eight Maids-a-Milking, "),
    ("ninth", "nine Ladies Dancing, "),
    ("tenth", "ten Lords-a-Leaping, "),
    ("eleventh", "eleven Pipers Piping, "),
    ("twelfth", "twelve Drummers Drumming, "),
)


def recite(start_verse, end_verse):
    verses = []
    for v in range(start_verse, end_verse + 1):
        verses.append(one_verse(v - 1))
    return verses


def one_verse(verse):
    lines = []
    if verse == 0:
        lines.append(on_the("first"))
        lines.append("a Partridge in a Pear Tree.")  # special case for no "and"
    else:
        lines.append(on_the(verses[verse][0]))

        for i in range(verse, -1, -1):
            lines.append(verses[i][1])

    return "".join(lines)


def on_the(ordinal):
    return "On the " + ordinal + " day of Christmas my true love gave to me: "
