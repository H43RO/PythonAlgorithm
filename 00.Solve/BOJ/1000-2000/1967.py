from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(1000000)


def dfs(graph, v, visited):
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i, w in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + w
            dfs(graph, i, visited)


n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 최장 거리 노드 탐색
visited = [0] * (n + 1)
dfs(graph, 1, visited)
visited[1] = 0
farthest = visited.index(max(visited))
# 최장 거리 노드로부터 가장 먼 노드 탐색
distance = [0] * (n + 1)
dfs(graph, farthest, distance)
distance[farthest] = 0
print(max(distance))
