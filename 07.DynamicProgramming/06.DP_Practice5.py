n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

# LIS (가장 긴 증가하는 부분 수열) 알고리즘
for i in range(1, n):
    for j in range(0, i):
        # 앞의 수 중 array[j] 가 array[i] 보다 작다면
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
