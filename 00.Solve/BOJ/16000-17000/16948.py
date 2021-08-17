from sys import stdin
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(stdin.readline())
graph = [[-1] * n for _ in range(n)]
r1, c1, r2, c2 = map(int, stdin.readline().split())

graph[r1][c1] = 0

queue = deque([(r1, c1)])
while queue:
    x, y = queue.popleft()
    if x == r2 and y == c2:
        print(graph[x][y])
        exit(0)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
print(-1)
