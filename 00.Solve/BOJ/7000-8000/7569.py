from sys import stdin
from collections import deque

# 방향 벡터 6개를 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    """
    하루에 한 번씩, 익은 토마토들로 부터 주변 1칸씩 BFS 를 진행하는 함수
    :return:    토마토가 모두 익을 때까지 걸리는 최소 일자
    """
    day = -1
    while ripen:
        day += 1
        for _ in range(len(ripen)):  # 하루에 한 번만 전파되기 때문에, 매일 맨 처음에 익어있던 토마토들 대해서만 BFS 탐색 해야 함
            z, x, y = ripen.popleft()
            for i in range(6):  # 6가지 방향 벡터에 대해 전파
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                # 토마토 상자 범위를 벗어나지 않고, 방문한 적이 없는 곳이라면 (안 익은 토마토가 있는 곳이라면)
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1  # 방문 처리
                    ripen.append((nz, nx, ny))

    # BFS 탐색이 모두 끝났는데 0이 남아있다면, -1을 출력해야 함
    for x in graph:
        for a in x:
            if 0 in a:
                return -1
    return day


m, n, h = map(int, stdin.readline().split())
graph = []  # 3차원 그래프에 토마토 정보를 담을 것
ripen = deque([])  # 익은 토마토를 기준으로 BFS 탐색을 할 것
for i in range(h):
    box = []
    for j in range(n):
        tomato = list(map(int, stdin.readline().split()))
        box.append(tomato)
        for k in range(m):
            if tomato[k] == 1:  # 익은 토마토는 위치를 따로 저장
                ripen.append((i, j, k))
    graph.append(box)

print(bfs())  # 토마토가 모두 익기까지 며칠 걸리는지 출력
