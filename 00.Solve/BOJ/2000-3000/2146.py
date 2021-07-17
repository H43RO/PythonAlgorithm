from collections import deque
from sys import stdin, maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    queue = deque()
    queue.append((start[0], start[1]))

    result = []
    result.append((start[0], start[1]))

    graph[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                result.append((nx, ny))
                graph[nx][ny] = 0
    return result


n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
island = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            temp = bfs((i, j))
            island.append(temp)

result = maxsize
for i in range(len(island)):
    for j in range(i + 1, len(island)):
        for x in range(len(island[i])):
            for y in range(len(island[j])):
                result = min(result, abs(island[i][x][0] - island[j][y][0]) + abs(island[i][x][1] - island[j][y][1]))

print(result - 1)
