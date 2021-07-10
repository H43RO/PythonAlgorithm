from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
J = list(map(int, stdin.readline().split()))

hello = list(zip(L, J))  # (잃는 체력, 얻는 기쁨) 튜플 형태로 저장
dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if hello[i - 1][0] <= j:
            dp[i][j] = max(dp[i - 1][j - hello[i - 1][0]] + hello[i - 1][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][99])  # 100 되면 기쁨 못 느낌
