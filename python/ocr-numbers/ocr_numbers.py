def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise (ValueError("Number of input lines is not a multiple of four"))
    if not all(len(row) % 3 == 0 for row in input_grid):
        raise (ValueError("Number of input columns is not a multiple of three"))

    ocr_rows = split_into_subgrids(input_grid)
    results = ""
    for ocr_row in ocr_rows:
        for subgrid in ocr_row:
            results += do_one(subgrid)
        results += ","

    return results.rstrip(",")


def do_one(subgrid):
    try:
        return str(characters.index(subgrid))
    except ValueError:
        return "?"


def split_into_subgrids(grid):
    results = []
    for i in range(0, len(grid), 4):
        four_rows = grid[i : i + 4]
        results.append(
            [[row[n : n + 3] for row in four_rows] for n in range(0, len(grid[0]), 3)]
        )
    return results


characters = [
    [" _ ", "| |", "|_|", "   "],
    ["   ", "  |", "  |", "   "],
    [" _ ", " _|", "|_ ", "   "],
    [" _ ", " _|", " _|", "   "],
    ["   ", "|_|", "  |", "   "],
    [" _ ", "|_ ", " _|", "   "],
    [" _ ", "|_ ", "|_|", "   "],
    [" _ ", "  |", "  |", "   "],
    [" _ ", "|_|", "|_|", "   "],
    [" _ ", "|_|", " _|", "   "],
]
