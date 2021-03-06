import heapq
from sys import stdin

INF = int(1e9)

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # a 번 도시에서 b 번 도시로 가는 버스 비용이 c 라는 의미
    graph[a].append((b, c))

start, end = map(int, stdin.readline().split())


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
print(distance[end])
