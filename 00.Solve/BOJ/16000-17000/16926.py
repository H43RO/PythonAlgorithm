from sys import stdin

n, m, r = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = graph[x][y]

        for j in range(i + 1, n - i):  # 좌
            x = j
            previous = graph[x][y]
            graph[x][y] = temp
            temp = previous

        for j in range(i + 1, m - i):  # 하
            y = j
            previous = graph[x][y]
            graph[x][y] = temp
            temp = previous

        for j in range(i + 1, n - i):  # 우
            x = n - j - 1
            previous = graph[x][y]
            graph[x][y] = temp
            temp = previous

        for j in range(i + 1, m - i):  # 상
            y = m - j - 1
            previous = graph[x][y]
            graph[x][y] = temp
            temp = previous

[print(*graph[i]) for i in range(n)]
