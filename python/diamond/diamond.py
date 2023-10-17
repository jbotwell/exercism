def rows(letter):
    num_rows = ord(letter) - ord("A")
    width = 2 * num_rows + 1

    results = [make_row(letter, num_rows, width)]
    for i in range(1, num_rows + 1):
        letter = chr(ord(letter) - 1)
        results = (
            [make_row(letter, num_rows - i, width)]
            + results
            + [make_row(letter, num_rows - i, width)]
        )

    return results


def make_row(letter, row, width):
    if row == 0:
        return letter.center(width)
    else:
        middle_spaces = 1 + 2 * (row - 1)
        return (letter + " " * middle_spaces + letter).center(width)
