from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a 에서 b 로 가는 비용은 c 라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

result = 0
# 각 노드에 대하여 탐색
for i in range(1, n + 1):
    known = 0
    # 나로부터 다른 노드로 가는 경로, 다른 노드로부터 나에게 오는 경로의 합
    # (나보다 키가 작은 학생들)     (나보다 키가 큰 학생들)
    for j in range(1, n + 1):
        known += graph[i][j] + graph[j][i]
    # 만약 그 합이 n - 1 과 같다면 모든 노드와 비교가 가능한 것
    if known == n - 1:
        result += 1
print(result)
