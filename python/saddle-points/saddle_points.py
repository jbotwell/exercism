def saddle_points(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    if len(matrix) == 0:
        return []

    row_maxes, col_mins = get_row_maxes(matrix), get_col_mins(matrix)

    points = []
    for i, this_max in enumerate(row_maxes):
        for j, this_min in enumerate(col_mins):
            if this_max == this_min:
                points.append({"row": i + 1, "column": j + 1})
    return points


def get_col_mins(matrix):
    mins = [float("inf") for tree in matrix[0]]
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            if matrix[i][j] < mins[j]:
                mins[j] = matrix[i][j]
    return mins


def get_row_maxes(matrix):
    return list(map(max, matrix))
