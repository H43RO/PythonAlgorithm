from sys import stdin

n, m = map(int, stdin.readline().split())

data = list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + data[i - 1]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(dp[j] - dp[i - 1])
