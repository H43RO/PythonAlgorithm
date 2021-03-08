import heapq
from sys import stdin, stdout

INF = int(1e9)
n, m, start = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))


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


dijkstra(start)

result = []
for i in range(1, n + 1):
    if distance[i] != INF and distance[i] != 0:
        result.append(distance[i])

print(len(result), max(result))