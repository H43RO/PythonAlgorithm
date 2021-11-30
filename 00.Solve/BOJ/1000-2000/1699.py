from math import sqrt
from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)  # 편의상 1-Based 인덱싱

for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, int(sqrt(i)) + 1):  # 자신의 제곱근 포함 작은 숫자들 (j) 에 대해
        dp[i] = min(dp[i], dp[i - j * j] + 1)  # dp[i - j^2] + 1 값이 더 작은지 검사

print(dp[n])

