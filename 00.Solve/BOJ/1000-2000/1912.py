from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [num[0]]

for i in range(len(num) - 1):
    dp.append(max(dp[i] + num[i + 1], num[i + 1]))

print(max(dp))
