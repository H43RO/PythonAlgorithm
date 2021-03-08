from sys import stdin

INF = int(1e9)
n = int(stdin.readline())
m = int(stdin.readline())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # 중복 노선이 들어올 수 있기 때문에, 기존 비용보다
    # 낮은 비용이 들어온 경우에만 값을 갱신하도록 함
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()