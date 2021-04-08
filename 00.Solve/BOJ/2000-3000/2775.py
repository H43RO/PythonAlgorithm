from sys import stdin

T = int(stdin.readline())

dp = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())

    print(dp[k][n - 1])

