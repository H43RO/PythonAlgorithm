from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
dp = []
for x in data:
    dp.append([x])

for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [data[i]]

print(len(max(dp, key=len)))
print(' '.join(str(x) for x in max(dp, key=len)))
