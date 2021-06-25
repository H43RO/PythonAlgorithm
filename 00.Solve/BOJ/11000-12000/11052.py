from sys import stdin

n = int(stdin.readline())
price = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
dp[1] = price[1]

for i in range(1, n + 1):
    dp[i] = price[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])