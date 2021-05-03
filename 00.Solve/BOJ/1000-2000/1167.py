from sys import stdin


def dfs(graph, v, visited, count, result):
    visited[v] = True
    for x in graph[v]:
        if not visited[x[0]]:
            dfs(graph, x[0], visited, count + x[1], result)

    result.append((v, count))


n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    data = list(map(int, stdin.readline().split()))
    for i in range(1, data.index(-1), 2):
        graph[data[0]].append((data[i], data[i + 1]))

result = []
count = 0
visited = [False] * (n + 1)
dfs(graph, 1, visited, count, result)
farthest = max(result, key=lambda x: x[1])

visited = [False] * (n + 1)
dfs(graph, farthest[0], visited, count, result)
print(max(result, key=lambda x: x[1])[1])