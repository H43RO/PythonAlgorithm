from sys import stdin


def dfs(v, number):
    if number == 4:
        print(1)
        exit()
    for x in graph[v]:
        if not visited[x]:
            visited[x] = True
            dfs(x, number + 1)
            visited[x] = False


n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
