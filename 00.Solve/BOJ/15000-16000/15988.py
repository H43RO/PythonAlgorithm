from sys import stdin

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

mod = 1_000_000_009

for i in range(5, 1000001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % mod

T = int(stdin.readline())

for _ in range(T):
    print(dp[int(stdin.readline())] % mod)
