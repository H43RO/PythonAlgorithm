from sys import stdin
from collections import deque
import copy

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def bfs(graph):
    queue = deque()
    graph[0][0] = 1
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    if graph[n - 1][m - 1] == 0:
        return -1
    return graph[n - 1][m - 1]


n, m = map(int, stdin.readline().split())

graph = []
wall = []
result = []

# 벽의 좌표를 모두 저장하여, 벽을 차례대로 하나씩 허물어보면서 BFS 탐색 시도
for i in range(n):
    temp = list(map(int, stdin.readline().strip()))
    for j in range(m):
        # 벽 좌표 (i, j) 를 튜플 형태로 저장
        # - 편의를 위해 벽 좌표를 -1 로 변경
        if temp[j] == 1:
            wall.append((i, j))
            temp[j] = -1
    graph.append(temp)

for x in wall:
    # 원본 변형 X
    graph_copy = copy.deepcopy(graph)

    # 현재 무너뜨려볼 차례의 벽을 무너뜨림
    graph_copy[x[0]][x[1]] = 0
    result.append(bfs(graph_copy))

print(max(result))
