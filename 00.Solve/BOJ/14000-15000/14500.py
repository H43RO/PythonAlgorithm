from sys import stdin

n, m = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for i in range(n)]

tetromino = [[[0, 1], [0, 2], [0, 3]],
             [[1, 0], [2, 0], [3, 0]],
             [[0, 1], [1, 0], [1, 1]],
             [[1, 0], [2, 0], [2, 1]],
             [[1, 0], [2, 0], [2, -1]],
             [[0, 1], [0, 2], [1, 0]],
             [[0, 1], [0, 2], [1, 2]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 0], [2, 0]],
             [[0, 1], [0, 2], [-1, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[1, 0], [1, 1], [2, 1]],
             [[1, 0], [1, -1], [2, -1]],
             [[0, 1], [-1, 1], [-1, 2]],
             [[0, 1], [1, 1], [1, 2]],
             [[0, 1], [0, 2], [1, 1]],
             [[1, 0], [1, 1], [2, 0]],
             [[1, 0], [1, -1], [2, 0]],
             [[0, 1], [0, 2], [-1, 1]]]

result = 0
temp = 0
for i in range(n):
    for j in range(m):
        for shape in tetromino:
            temp = graph[i][j]
            for k in range(3):
                nx = j + shape[k][1]
                ny = i + shape[k][0]
                if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                    temp += graph[ny][nx]

            result = max(result, temp)

print(result)
