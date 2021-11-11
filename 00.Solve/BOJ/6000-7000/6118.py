from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0

queue = deque([1])
while queue:
    node = queue.popleft()
    for x in graph[node]:
        if dist[x] == -1:
            dist[x] = dist[node] + 1
            queue.append(x)

print(dist.index(max(dist)), max(dist), dist.count(max(dist)))
