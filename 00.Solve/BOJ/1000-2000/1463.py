n = int(input())

dp = [0] * 1000001

for i in range(2, n + 1):
    # 우선 1을 빼는 연산을 추적
    dp[i] = dp[i - 1] + 1

    # 2로 나눌 수 있는 상황 추적
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나눌 수 있는 상황 추적
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
