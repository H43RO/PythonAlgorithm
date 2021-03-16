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
for i in range(1, n + 1):
    known = 0
    for j in range(1, n + 1):
        known += graph[i][j] + graph[j][i]
    if known == n - 1:
        result += 1
print(result)