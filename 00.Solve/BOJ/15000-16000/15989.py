from sys import stdin

dp = [1 for i in range(10001)]

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    print(dp[n])
