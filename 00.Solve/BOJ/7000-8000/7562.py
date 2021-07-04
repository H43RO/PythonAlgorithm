from sys import stdin
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(graph, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


T = int(stdin.readline())

for _ in range(T):
    L = int(stdin.readline())
    graph = [[0] * L for _ in range(L)]
    start_x, start_y = map(int, stdin.readline().split())
    end_x, end_y = map(int, stdin.readline().split())
    print(bfs(graph, start_x, start_y, end_x, end_y))
