from sys import stdin, stdout

wine = []

n = int(stdin.readline())
for _ in range(n):
    wine.append(int(stdin.readline()))

if n <= 2:
    print(sum(wine))
elif n == 3:
    print(sum(wine) - min(wine))
else:
    dp = [0] * (n + 1)
    wine.insert(0, 0)

    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(wine[1] + wine[2], wine[2] + wine[3], wine[1] + wine[3])

    for i in range(4, n + 1):
        if dp[i - 1] <= max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i]):
            dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
        else:
            dp[i] = dp[i - 1]

    print(dp[n])
