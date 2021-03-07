import heapq
from sys import stdin, stdout

n = int(stdin.readline())
m = int(stdin.readline())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
path = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, stdin.readline().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    path[start].append(start)

    while q:
        # 현재로써 가장 최단 거리가 짧은 노드의 정보
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드의 인접 노드들에 대하여
        for x in graph[now]:
            # 거리 + 비용 따져봤을 때
            cost = dist + x[1]
            # 기존보다 더 짧은 경로라고 파악되면
            if distance[x[0]] > cost:
                # 최단 거리 정보를 갱신하고
                distance[x[0]] = cost
                # 기존 경로 정보를 삭제한 뒤
                path[x[0]] = []
                # 새로운 최단 경로 정보를 입력하고
                for i in path[now]:
                    path[x[0]].append(i)
                path[x[0]].append(x[0])
                # 힙에 (거리, 해당 노드) 정보를 푸시
                heapq.heappush(q, (cost, x[0]))


dijkstra(start)
print(distance[end])
print(len(path[end]))
for x in path[end]:
    print(x, end=' ')
