def annotate(minefield):
    if not test_same_len(minefield):
        raise ValueError("The board is invalid with current input.")
    if not test_invalid_char(minefield):
        raise ValueError("The board is invalid with current input.")

    disassembled = disassemble(minefield)
    return reassemble(
        # this just maps count_neighboring_mines over the interior lists
        # the double map is necessary for a list of lists
        map(
            lambda row: map(
                lambda col: count_neighboring_mines(row[0], col[0], disassembled),
                enumerate(row[1]),
            ),
            enumerate(minefield),
        )
    )


def disassemble(minefield):
    return list(map(lambda row: list(row), minefield))


def reassemble(dis_minefield):
    return list(map(lambda row: "".join(row), dis_minefield))


def check_for_bomb(row, col, field):
    try:
        if row < 0 or col < 0:
            return False
        else:
            return field[row][col] == "*"

    except IndexError:
        return False


def count_neighboring_mines(row, col, field):
    if field[row][col] == "*":
        return "*"

    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if check_for_bomb(row + i, col + j, field):
                print("row", row + i, "col", col + j)
                count += 1

    if count == 0:
        return " "
    else:
        return str(count)


def test_same_len(board):
    if len(board) == 0:
        return True
    return all(len(row) == len(board[0]) for row in board)


def test_invalid_char(board):
    return all(set(row).issubset(set(" *")) for row in board)


print(disassemble(["   ", " * ", "   "]))
print(reassemble(disassemble(["   ", " * ", "   "])))
print(check_for_bomb(1, 1, disassemble(["   ", " * ", "   "])))
