from sys import stdin

n, m = map(int, stdin.readline().split())
memory = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(n + 1)]
result = sum(cost)

for i in range(1, n + 1):  # 앱의 개수를 1씩 늘려가며 탐색
    for j in range(1, sum(cost) + 1):  # 최대 비용을 1씩 늘려가며 탐색
        if cost[i - 1] <= j:  # 현재 탐색하고 있는 앱의 비활성화 비용이 최대 비용 이내라면
            # 현재 앱을 끈 뒤의 메모리와 그렇지 않을 경우의 메모리 중중 큰 값을 dp에 입력한다.
            dp[i][j] = max(memory[i - 1] + dp[i - 1][j - cost[i - 1]], dp[i - 1][j])
        else:  # 그렇지 않으면 앱을 활성화 시켜둠 (현재 앱의 비활성화 비용이 최대 비용을 넘을 경우)
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= m:  # 현재 dp[i][j] 값이 m 이상이라면
            result = min(result, j)  # 현재 비용, j 와 이전의 result 와 비교하여 더 작은 값 갱신

if m != 0:
    print(result)
else:
    print(0)
