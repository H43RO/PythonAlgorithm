from sys import stdin

n, m = map(int, stdin.readline().split())
memory = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(n + 1)]
result = sum(cost)

for i in range(1, n + 1):
    for j in range(1, sum(cost) + 1):
        if cost[i - 1] <= j:
            dp[i][j] = max(memory[i - 1] + dp[i - 1][j - cost[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)
