import heapq
from sys import stdin, stdout

INF = int(1e9)

n, m, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
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
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


go_cost = []
come_cost = []

for i in range(1, n + 1):
    dijkstra(i)
    go_cost.append(distance[x])
    distance = [INF] * (n + 1)

    dijkstra(x)
    come_cost.append(distance[i])
    distance = [INF] * (n + 1)

result = []
for i in range(n):
    result.append(go_cost[i] + come_cost[i])

print(max(result))
