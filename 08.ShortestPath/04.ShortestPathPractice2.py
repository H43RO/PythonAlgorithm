from sys import stdin, stdout

INF = int(1e9)
n, m = map(int, stdin.readline().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    # 비용은 항상 1인 양방향 그래프
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, stdin.readline().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
