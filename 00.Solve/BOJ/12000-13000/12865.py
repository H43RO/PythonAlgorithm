from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
items = []
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    items.append(list(map(int, stdin.readline().split())))

# items[index][0] : Weight
# items[index][1] : Value
for i in range(1, n + 1):  # 물건 개수 늘려가며 메모
    for j in range(1, k + 1):  # 무게 한도 늘려가며 메모
        # 만약 현재 보고있는 물건의 무게가 무게 한도 내 라면
        if items[i - 1][0] <= j:
            # 이전 물품 빼고 현재 보고있는 물건의 가치 넣은 값, 이전 최댓값 중 큰 값 저장
            dp[i][j] = max(dp[i - 1][j - items[i - 1][0]] + items[i - 1][1], dp[i - 1][j])
        else:
            # 현재 보고있는 물건의 무게가 한도 초과된다면 이전 최댓값 그대로 가져옴
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])

