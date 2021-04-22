from sys import stdin, stdout
import heapq

INF = int(1e9)

start, end = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append((b, 1))  # 비용은 노 상관
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

if distance[end] == INF:
    print(-1)
else:
    print(distance[end])