from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    day = -1
    while ripen:
        day += 1
        for _ in range(len(ripen)):
            z, x, y = ripen.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    ripen.append((nz, nx, ny))

    for x in graph:
        for a in x:
            if 0 in a:
                return -1
    return day


m, n, h = map(int, stdin.readline().split())
graph = []
ripen = deque([])
for i in range(h):
    box = []
    for j in range(n):
        temp = list(map(int, stdin.readline().split()))
        box.append(temp)
        for k in range(m):
            if temp[k] == 1:
                ripen.append((i, j, k))
    graph.append(box)

print(bfs())
