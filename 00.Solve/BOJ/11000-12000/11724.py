import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())

count = 0

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)

print(count)
