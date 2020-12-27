from collections import deque

n, m, v = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] * (n + 1) for _ in range(n + 1)]

# 간선 정보에 따른 그래프 (이웃 노드) 정보 추가
for i in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

for i in range(n + 1):
    graph[i].sort()


def dfs_function(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_function(graph, i, visited)


def bfs_function(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs_function(graph, v, visited)

visited = [False] * (n + 1)
print()

bfs_function(graph, v, visited)
