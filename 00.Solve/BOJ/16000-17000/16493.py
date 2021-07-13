from sys import stdin

n, m = map(int, stdin.readline().split())

chapter = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
page = sum([x[1] for x in chapter])
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if chapter[i - 1][0] <= j:
            dp[i][j] = max(dp[i - 1][j - chapter[i - 1][0]] + chapter[i - 1][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp)
print(dp[n][m])
