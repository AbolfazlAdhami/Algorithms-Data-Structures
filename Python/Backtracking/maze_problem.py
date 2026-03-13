class MazeProblem:

    def __init__(self, maze_matrix) -> None:
        self.maze_matrix = maze_matrix
        self.maze_size = len(maze_matrix)

        self.solution_matrix = [['-' for _ in range(self.maze_size)]
                                for _ in range(self.maze_size)]

        # right, left, down, up
        self.move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve_problem(self):

        self.solution_matrix[0][0] = 'S'

        if self.solve(0, 0):
            self.show_result()
        else:
            print("There is no feasible solution....")

    def solve(self, x, y):

        if self.is_finished(x, y):
            return True

        for move in self.move:

            next_x = x + move[0]
            next_y = y + move[1]

            if self.is_valid(next_x, next_y):

                self.solution_matrix[next_x][next_y] = 'S'

                if self.solve(next_x, next_y):
                    return True

                # Backtracking
                self.solution_matrix[next_x][next_y] = '-'

        return False

    def is_valid(self, x, y):

        if x < 0 or x >= self.maze_size:
            return False

        if y < 0 or y >= self.maze_size:
            return False

        if self.maze_matrix[x][y] == 0:
            return False

        if self.solution_matrix[x][y] == 'S':
            return False

        return True

    def is_finished(self, x, y):

        if x == self.maze_size - 1 and y == self.maze_size - 1:
            return True

        return False

    def show_result(self):

        for x in range(self.maze_size):
            for y in range(self.maze_size):
                print(self.solution_matrix[x][y], end=' ')
            print()


if __name__ == "__main__":

    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    maze_solver = MazeProblem(m)
    maze_solver.solve_problem()
