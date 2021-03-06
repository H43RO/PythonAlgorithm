"""
    다익스트라 최단 경로 알고리즘

    1. 출발 노드 설정
    2. 최단 거리 테이블 초기화
    3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
    5. 위 과정에서 3~4번 반복
"""

# 힙을 사용하기 때문에 가장 최단 거리가 짧은 노드에 대한 정보를 찾을 때
# 순차 탐색보다 훨씬 빠르게 처리할 수 있음 (시간 복잡도 : O(logN))

import heapq
from sys import stdin

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, stdin.readline().split())
# 시작 노드 번호 입력받기
start = int(stdin.readline())
# 각 노드에 연결되어 있는 노드에 대한 정보(튜플)를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한 값으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드를 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입 (시작점 그 자리 그대니까)
    # (현재 최단 거리, 해당 노드) 튜플로 저장
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (힙의 특성 사용)
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        # - 즉, 이미 최단 경로가 저장되어 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INF) 이라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 최단 거리를 출력
    else:
        print(distance[i])
