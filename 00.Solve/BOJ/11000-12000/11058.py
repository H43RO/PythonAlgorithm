from sys import stdin

n = int(stdin.readline())
dp = [i for i in range(n + 1)]
for i in range(6, n + 1):
    dp[i] = max(dp[i - 5] * 4, dp[i - 4] * 3, dp[i - 3] * 2)
print(dp[n])
