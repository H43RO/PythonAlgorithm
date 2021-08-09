from sys import stdin
from collections import deque


def bfs(start):
    count = 1
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = deque([start])

    while queue:
        com = queue.popleft()
        for x in graph[com]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
                count += 1

    return count


n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b].append(a)

hacking = []
max_hacking = 0
for i in range(1, n + 1):
    result = bfs(i)
    if max_hacking == result:
        hacking.append(i)
    if max_hacking < result:
        max_hacking = result
        hacking = [i]

print(*hacking)
