RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
UP = [-1, 0]

MOVEMENTS = [RIGHT, DOWN, LEFT, UP]


def spiral_matrix(size):
    mat = [[0 for _ in range(0, size)] for _ in range(0, size)]

    move_index = 0
    move = MOVEMENTS[move_index]
    row, col = 0, -1  # col will increment, so first square will be 0,0
    for n in range(1, size * size + 1):
        if is_available(row + move[0], col + move[1], mat):
            row, col = row + move[0], col + move[1]
            fill(row, col, mat, n)
        else:
            move_index = (move_index + 1) % 4
            move = MOVEMENTS[move_index]
            row, col = row + move[0], col + move[1]
            fill(row, col, mat, n)

    return mat


def is_available(r, c, mat):
    if r < 0 or c < 0:
        return False
    try:
        return mat[r][c] == 0
    except IndexError:
        return False


def fill(r, c, mat, n):
    mat[r][c] = n
