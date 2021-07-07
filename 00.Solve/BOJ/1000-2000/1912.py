from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [num[0]]  # 시간 제한이 빡세고 수 범위가 크므로 DP 테이블 점차 늘리는 식으로

for i in range(len(num) - 1):
    # 점화식 : 현재 인덱스의 DP 값에 다음 숫자를 더한 값과, 다음 숫자 값 중 더 큰 값 저장
    dp.append(max(dp[i] + num[i + 1], num[i + 1]))

print(max(dp))
