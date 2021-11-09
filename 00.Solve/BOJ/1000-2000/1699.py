from sys import stdin
from math import sqrt

n = int(stdin.readline())
dp = [0] * (n + 1)  # 편의상 1-Based 인덱싱

for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, int(sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[n])

