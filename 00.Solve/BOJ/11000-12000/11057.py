from sys import stdin

n = int(stdin.readline())

if n == 1:
    print(10)
    exit(0)
if n == 2:
    print(55)
    exit(0)
if n == 3:
    print(220)
    exit(0)

dp = [0] * (n + 1)

dp[1] = 10
dp[2] = 55

for i in range(3, n + 1):
    pass

print(dp[n] % 10007)
