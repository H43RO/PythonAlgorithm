import heapq
from sys import stdin

INF = int(1e9)
n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append((b, 1))  # 단반향 간선의 거리는 무조건 1


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


dijkstra(x)
existing = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        existing = True

if not existing:
    print(-1)


