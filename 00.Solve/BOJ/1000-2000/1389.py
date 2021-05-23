from sys import stdin
from collections import deque


def bfs(graph, start, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    count = 0

    while queue:
        v, level = queue.popleft()
        count += level
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, level + 1))

    return count


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]  # 친구 관계를 담는 그래프
kevin = []

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    kevin.append(bfs(graph, i, visited))

print(kevin.index(min(kevin)) + 1)