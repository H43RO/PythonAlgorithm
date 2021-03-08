"""
    모든 노드에 대하여 각 노드에 대한 최단거리 계산

    각 단계마다 특정한 노드 k 를 거쳐 가는 경우 확인
    - a 에서 b 로 가는 최단 거리보다 a 에서 k 를 거쳐 b 로 가는 거리가 더 짧은지 검사
    D(ab) = min(D(ab), D(ak) + D(kb))

     1. 2차원 테이블에 각 노드에 대하여 인접노드로 향하는 비용 기록
     2. 기존 모든 경로에 대하여 k 번 노드를 거쳐 가는 모든 경우를 고려하여 최단 거리 발견 시 테이블 갱신
"""

INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트 (그래프) 를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a 에서 b 로 가는 비용은 c 라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 간선이 없는 경우 (도달할 수 없는 경우) 에러 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 최단 거리 출력
        else:
            print(graph[a][b], end=" ")
    print()
