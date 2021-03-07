import heapq
from sys import stdin


def dijkstra(index):
    q = []
    distance[0][0] = 0
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        w, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f"Problem {index}: {w}")
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nw = w + graph[nx][ny]
                if nw < distance[nx][ny]:
                    distance[nx][ny] = nw
                    heapq.heappush(q, (nw, nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
index = 1

while True:
    n = int(stdin.readline())
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

    if n == 0:
        break

    dijkstra(index)
    index += 1
