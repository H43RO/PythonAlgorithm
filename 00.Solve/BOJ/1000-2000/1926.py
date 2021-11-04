from sys import stdin
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    global picture_max_size, picture_count

    size = 1
    graph[i][j] = 0  # 방문 처리로써 0 대입

    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                queue.append((nx, ny))
                size += 1  # 그림의 크기 1 증가
                graph[nx][ny] = 0  # 방문 처리

    picture_count += 1  # 그림의 개수 1 증가
    picture_max_size = max(picture_max_size, size)  # 그림의 크기 최댓값 갱신


n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

picture_count = 0  # 그림의 개수가 담길 변수
picture_max_size = 0  # 가장 넓은 그림의 너비가 담길 변수

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            bfs(i, j)

print(picture_count)
print(picture_max_size)
