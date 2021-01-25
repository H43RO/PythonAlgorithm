from sys import stdin, stdout
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[v] + 1
                queue.append(i)
    return -1


n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())

# 자식, 부모가 어떻게 연결되어있는지 나타내는 그래프
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0 for _ in range(n + 1)]

count = 0

for i in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(graph, a, visited)
if result[b] != 0:
    print(result[b])
else:
    print(-1)
