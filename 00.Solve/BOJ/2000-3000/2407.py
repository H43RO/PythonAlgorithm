from sys import stdin

n, m = map(int, stdin.readline().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][1] = i

for i in range(2, n + 1):
    for j in range(2, m + 1):
        if i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][m])
