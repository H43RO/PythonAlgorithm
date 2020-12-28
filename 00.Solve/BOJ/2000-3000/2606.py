n = int(input())
edge = int(input())

graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for i in range(edge):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

for x in graph:
    x.sort()


def dfs_function(graph, v):
    global result
    visited[v] = True
    result += 1
    for i in graph[v]:
        if not visited[i]:
            dfs_function(graph, i)


dfs_function(graph, 1)

# 자기 자신 제외
print(result-1)
