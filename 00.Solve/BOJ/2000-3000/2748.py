n = int(input())

dp = [0] * 91

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3

if n < 4:
    print(dp[n])
else:
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])
