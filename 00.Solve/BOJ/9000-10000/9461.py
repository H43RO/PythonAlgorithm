from sys import stdin

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(4, n + 1):
        # 점화식 : dp[i] = dp[i - 3] + dp[i - 2]
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[n])
