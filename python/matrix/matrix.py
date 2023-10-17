class Matrix:
    def __init__(self, matrix_string):
        proto_rows = matrix_string.split("\n")

        processed = []
        for row in proto_rows:
            split_row = row.split(" ")
            processed.append(list(map(int, split_row)))

        self.rows = processed

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col_nums = []
        for row in self.rows:
            col_nums.append(row[index - 1])

        return col_nums
