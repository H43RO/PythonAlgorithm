from sys import stdin

n = int(stdin.readline())

graph = []

for a in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for x in range(n):
    for y in range(n):
            print(graph[x][y], end=' ')
    print()