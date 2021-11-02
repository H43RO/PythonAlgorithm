from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global sheep_count, wolf_count

    sheep = 0
    wolf = 0

    if graph[i][j] == 'v':
        wolf += 1
    elif graph[i][j] == 'o':
        sheep += 1

    graph[i][j] = '#'  # 방문처리 겸 울타리 처리
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
                queue.append((nx, ny))

                if graph[nx][ny] == 'v':
                    wolf += 1
                elif graph[nx][ny] == 'o':
                    sheep += 1

                graph[nx][ny] = '#'

    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0

    sheep_count += sheep
    wolf_count += wolf


r, c = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(r)]

sheep_count, wolf_count = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            bfs(i, j)

print(sheep_count, wolf_count)
