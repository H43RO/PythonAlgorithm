from sys import stdin


def power(m, y):
    if y == 1:
        return m
    partial = power(m, y // 2)
    partial_square = multiply(partial, partial)
    if y % 2 == 0:
        return partial_square
    elif y % 2 == 1:
        return multiply(partial_square, m)


def multiply(matrix_1, matrix_2):
    length = len(matrix_1)
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            result[i][j] = sum([(matrix_1[i][k] * matrix_2[k][j]) % MOD for k in range(length)]) % MOD
    return result


MOD = 1_000_000_007
n = int(stdin.readline())
mat = [[1, 1], [1, 0]]
result = power(mat, n)
print(result[0][1])