from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)

time_pay = []
# 소요 기간, 페이 함께 저장
# - [0] : 소요 기간, [1] : 페이
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    time_pay.append((a, b))

# 뒤에서부터 날짜를 줄여가며 최대 수익 계산해야 최대 수익 추적이 가능
# 점화식 : max(이전 최대 수익 값, 현재 날짜 수익 + 소요 기간 이후 최대 수익)
for i in range(n - 1, -1, -1):
    # 최대 기간 넘어서는 경우 이전 DP 값 계승
    if i + time_pay[i][0] > n:
        dp[i] = dp[i + 1]
        continue
    # 최대 기간 넘어가지 않는 경우 점화식 적용
    dp[i] = max(dp[i + 1], time_pay[i][1] + dp[i + time_pay[i][0]])

print(dp[0])
