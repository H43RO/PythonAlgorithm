from sys import stdin

n, t = map(int, stdin.readline().split())

study = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        if study[i - 1][0] <= j:
            dp[i][j] = max(dp[i - 1][j - study[i - 1][0]] + study[i - 1][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][t])
