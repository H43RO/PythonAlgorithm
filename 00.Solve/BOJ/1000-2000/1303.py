from collections import deque
from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, team):
    count = 1
    queue = deque([(i, j)])
    graph[i][j] = 'X'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == team:
                graph[nx][ny] = 'X'
                queue.append((nx, ny))
                count += 1
    return count


m, n = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(n)]
white = 0
black = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            white += bfs(i, j, 'W') ** 2
        if graph[i][j] == 'B':
            black += bfs(i, j, 'B') ** 2

print(white, black)
