from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global sheep_count, wolf_count

    sheep, wolf = 0, 0  # 양과 늑대 마릿수 저장

    # 양인지 늑대인지 구분하여 카운트 증가
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

                # 양과 늑대 마릿수 저장
                if graph[nx][ny] == 'v':
                    wolf += 1
                elif graph[nx][ny] == 'o':
                    sheep += 1

                # 방문처리 겸 울타리 처리
                graph[nx][ny] = '#'

    if sheep > wolf:  # 만약 양이 더 많으면 늑대 쫓아냄
        wolf = 0
    else:  # 아니라면 양 다 죽음
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
