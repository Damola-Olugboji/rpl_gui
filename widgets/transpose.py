import math as m


def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])

    transpose = [[0 for x in range(n)] for y in range(m)]
    for x in range(0, n):
        for y in range(0, m):
            transpose[y][x] = matrix[x][y]

    return transpose


"""x = [
    [1, 2, 3, 4, 5],
    [7, 7, 7, 7, 7],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [7, 7, 7, 7, 7],
]
y = transpose(x)
print(type(x))
print(type(y))"""