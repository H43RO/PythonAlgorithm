import sys
from collections import deque

sys.setrecursionlimit(10000)
n, m = map(int, input().split())

graph = []

for x in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 이동할 수 있는 칸을 만났을 때
            if graph[nx][ny] == 1:
                # 최단 경로를 기록해 줌 (이전 경로의 값에서 1 증가)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 도착 위치에 기록되어있는 값이 결국 최단 경로임
    return graph[n - 1][m - 1]


print(bfs(0, 0))
