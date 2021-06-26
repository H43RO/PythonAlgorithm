from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
dp = data.copy()

for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))
