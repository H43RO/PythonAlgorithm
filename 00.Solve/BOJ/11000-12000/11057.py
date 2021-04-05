from sys import stdin, stdout

n = int(stdin.readline())

dp = [[0] * 10 for i in range(n)]

# 첫 줄은 모두 1로 채움
for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    sum = 0
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]
            sum += dp[i - 1][k]

if n == 1:
    print(10)
else:
    print(sum % 10007)
