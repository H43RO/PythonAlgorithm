from sys import stdin

INF = int(1e9)
n, m = map(int, stdin.readline().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

count = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            count[i] += 1
            count[j] += 1
print(count.count(n - 1))
