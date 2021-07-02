from sys import stdin
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (0, (0, 0)))
    changed[0][0] = True
    while True:
        count, (x, y) = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not changed[nx][ny]:
                changed[nx][ny] = True
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    heapq.heappush(q, (count + 1, (nx, ny)))
                else:
                    heapq.heappush(q, (count, (nx, ny)))


n = int(stdin.readline())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
changed = [[False] * n for _ in range(n)]
print(dijkstra())
