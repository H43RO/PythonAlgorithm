from sys import stdin

n = int(stdin.readline())
soldier = list(map(int, stdin.readline().split()))
soldier.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldier[i] > soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
