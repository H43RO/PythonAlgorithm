from sys import stdin

k = int(stdin.readline())

dp = [0] * 47
dp[1], dp[2], dp[3] = 0, 1, 1

for i in range(4, k + 2):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[k], dp[k + 1])
