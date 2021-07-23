import copy
from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, graph, rain):
    if graph[i][j] == -1 or graph[i][j] <= rain:
        return False

    queue = deque([(i, j)])
    graph[i][j] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and graph[nx][ny] > rain:
                queue.append((nx, ny))
                graph[nx][ny] = -1

    return True


n = int(stdin.readline())
data = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, data))

result = 1  # 비가 안 올 땐 안전 영역 1 
for rain in range(1, max_height):
    graph = copy.deepcopy(data)

    section = 0
    for i in range(n):
        for j in range(n):
            if bfs(i, j, graph, rain):
                section += 1
    result = max(result, section)

print(result)
