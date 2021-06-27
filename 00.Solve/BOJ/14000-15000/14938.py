from sys import stdin
import heapq

INF = int(1e9)


def dijkstra(start):
    # 최단 거리 테이블을 모두 무한 값으로 초기화
    distance = [INF] * (n + 1)
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

    result = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            result += item[i]
    return result


n, m, r = map(int, stdin.readline().split())
item = [0] + list(map(int, stdin.readline().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_item = 0
for i in range(1, n + 1):
    temp = dijkstra(i)
    max_item = max(max_item, temp)
print(max_item)
