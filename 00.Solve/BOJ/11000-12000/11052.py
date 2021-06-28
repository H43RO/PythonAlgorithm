from sys import stdin

n = int(stdin.readline())
price = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
dp[1] = price[1]

for i in range(1, n + 1):
    # 우선 i 개 카드팩 1개 사는 가격으로 시작
    dp[i] = price[i]
    # 1개 카드팩부터 i // 2 카드팩 최대 가격 (DP 테이블) 까지 하나씩 뒤져보면서
    # 최대로 비싸게 살 수 있는 금액 저장 (카드팩 나누어 살 때 더 비싼 경우)
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])
