from sys import stdin

n, k = map(int, stdin.readline().split())
study = [tuple(map(int, stdin.readline().split())) for _ in range(k)]
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if study[i - 1][1] <= j:
            dp[i][j] = max(dp[i - 1][j - study[i - 1][1]] + study[i - 1][0], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[k][n])
