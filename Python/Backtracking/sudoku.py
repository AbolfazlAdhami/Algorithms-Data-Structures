BOARD_SIZE = 9
MIN_NUMBER = 1
MAX_NUMBER = 9
BOX_SIZE = 3


class Sudoku:

    def __init__(self, table):
        self.table = table

    def run(self):

        if self.solve(0, 0):
            self.show_solution()
        else:
            print("There is no solution...")

    def solve(self, row, col):

        if col == BOARD_SIZE:
            row += 1
            col = 0

        if row == BOARD_SIZE:
            return True

        if self.table[row][col] != 0:
            return self.solve(row, col + 1)

        for num in range(MIN_NUMBER, MAX_NUMBER + 1):

            if self.is_valid(row, col, num):

                self.table[row][col] = num

                if self.solve(row, col + 1):
                    return True

                # Backtracking
                self.table[row][col] = 0

        return False

    def is_valid(self, row, col, num):

        # Column check
        for i in range(BOARD_SIZE):
            if self.table[i][col] == num:
                return False

        # Row check
        for j in range(BOARD_SIZE):
            if self.table[row][j] == num:
                return False

        # 3x3 box check
        box_row_offset = (row // BOX_SIZE) * BOX_SIZE
        box_col_offset = (col // BOX_SIZE) * BOX_SIZE

        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if self.table[box_row_offset + i][box_col_offset + j] == num:
                    return False

        return True

    def show_solution(self):

        for row in self.table:
            print(row)


if __name__ == "__main__":

    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    algorithm = Sudoku(table=sudoku)
    algorithm.run()
