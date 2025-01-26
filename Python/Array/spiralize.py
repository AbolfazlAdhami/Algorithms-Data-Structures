def spiralize(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    top, bottom = 0, size - 1
    left, right = 0, size - 1
    value = 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = value
        top += 2
        for i in range(top, bottom + 1):
            matrix[i][right] = value
        right -= 2
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = value
            bottom -= 2
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = value
            left += 2

    return matrix


# print(spiralize(5))
# print(spiralize(8))
spiral = spiralize(5)

formatted_spiral = ["".join(map(str, row)) for row in spiral]
for row in formatted_spiral:
    print(row)
