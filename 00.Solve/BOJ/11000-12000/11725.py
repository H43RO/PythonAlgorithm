from sys import stdin
from collections import deque


def bfs(graph, visited):
    queue = deque([1])
    visited[1] = True

    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if not visited[x]:
                queue.append(x)
                parent[x - 1] = v
                visited[x] = True


n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, visited)


for x in parent:
    if x == 0:
        continue
    print(x)