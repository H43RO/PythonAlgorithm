from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    coin = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    dp = [0] * (m + 1)
    dp[0] = 1

    for x in coin:
        for i in range(x, m + 1):
            dp[i] += dp[i - x]

    print(dp[m])
