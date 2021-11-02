from sys import stdin


def move(x, y):
    global temp, graph

    previous = graph[x][y]
    graph[x][y] = temp
    temp = previous


n, m, r = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
temp = graph[0][0]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = graph[x][y]

        for j in range(i + 1, n - i):  # 좌
            x = j
            move(x, y)

        for j in range(i + 1, m - i):  # 하
            y = j
            move(x, y)

        for j in range(i + 1, n - i):  # 우
            x = n - j - 1
            move(x, y)

        for j in range(i + 1, m - i):  # 상
            y = m - j - 1
            move(x, y)

[print(*graph[i]) for i in range(n)]
