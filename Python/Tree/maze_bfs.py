from collections import deque


class MazeSolver:

    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.n = len(matrix)

        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]

        self.visited = [[False for _ in range(self.n)] for _ in range(self.n)]

        self.min_distance = float('inf')

    def is_valid(self, row, col):

        if row < 0 or row >= self.n:
            return False

        if col < 0 or col >= self.n:
            return False

        if self.matrix[row][col] == 0:
            return False

        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):

        queue = deque()

        queue.append((i, j, 0))
        self.visited[i][j] = True

        while queue:

            (i, j, dist) = queue.popleft()

            if i == destination_x and j == destination_y:
                self.min_distance = dist
                return

            for move in range(4):

                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                if self.is_valid(next_x, next_y):

                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):

        if self.min_distance != float('inf'):
            print("The shortest path from source to destination:",
                  self.min_distance)
        else:
            print("NO feasible solution - the destination cannot be reached!")


if __name__ == "__main__":

    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    maze_solver = MazeSolver(m)

    maze_solver.search(0, 0, 4, 4)

    maze_solver.show_result()
