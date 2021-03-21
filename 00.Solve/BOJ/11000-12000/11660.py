from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []

dp = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = graph[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x1 -= 1
    y1 -= 1

    print(dp[x2][y2] - dp[x2][y1] - dp[x1][y2] + dp[x1][y1])
