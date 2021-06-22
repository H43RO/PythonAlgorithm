from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, stdin.readline().split())
visited = [[-1] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(stdin.readline().strip()))
x1, x2, y1, y2 = map(int, stdin.readline().split())
x1, x2, y1, y2 = x1 - 1, x2 - 1, y1 - 1, y2 - 1

queue = deque([(x1, x2)])
visited[x1][x2] = 0

while queue:
    x, y = queue.popleft()
    if x == y1 and y == y2:
        break
    for i in range(4):
        # 한 방향으로 제한 거리까지 이동해보기
        for j in range(k):
            nx = x + dx[i] * (j + 1)
            ny = y + dy[i] * (j + 1)
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == '#':
                break
            if visited[nx][ny] == visited[x][y] + 1:
                continue
            elif visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            else:
                break

print(visited[y1][y2])
