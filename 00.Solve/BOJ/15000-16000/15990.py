from sys import stdin

T = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(T)]

dp = [[0] * 4 for _ in range(100001)]  # 나머지 정리 이용
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

mod = 1_000_000_009

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod

[print(sum(dp[x]) % mod) for x in data]  # mod 처리 안 해줘서 한 번 틀림
