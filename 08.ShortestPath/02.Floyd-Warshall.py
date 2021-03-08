"""
    모든 노드에 대하여 각 노드에 대한 최단거리 계산

    각 단계마다 특정한 노드 k 를 거쳐 가는 경우 확인
    - a 에서 b 로 가는 최단 거리보다 a 에서 k 를 거쳐 b 로 가는 거리가 더 짧은지 검사
    D(ab) = min(D(ab), D(ak) + D(kb))

     1. 2차원 테이블에 각 노드에 대하여 인접노드로 향하는 비용 기록
     2. 기존 모든 경로에 대하여 k 번 노드를 거쳐 가는 모든 경우를 고려하여 최단 거리 발견 시 테이블 갱신
"""

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
