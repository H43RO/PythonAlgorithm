from sys import stdin, stdout
from collections import deque
import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 풀어줘야 정답 처리

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def dfs(graph, x, y, w, h):
    if 0 <= y < w and 0 <= x < h:
        if graph[x][y] == 1:
            graph[x][y] = 0
            # 상하좌우, 대각선에 대하여 모두 탐색
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(graph, nx, ny, w, h)
            return True
    return False


def bfs(graph, x, y, w, h):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 상하좌우, 대각선에 대하여 모두 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동한 좌표가 맵 밖으로 나가지 않고, 섬인 경우
            if 0 <= ny < w and 0 <= nx < h:
                if graph[nx][ny] == 1:
                    # 값을 0으로 바꾸고 해당 좌표를 탐색 큐에 추가
                    graph[nx][ny] = 0
                    queue.append((nx, ny))


results = []

while True:
    result = 0
    # 맵의 Width, Height 입력
    w, h = map(int, stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = []

    for _ in range(h):
        graph.append(list(map(int, stdin.readline().split())))

    # for i in range(h):
    #     for j in range(w):
    #         if dfs(graph, i, j, w, h):
    #             result += 1
    # results.append(result)
    #
    # for x in results:
    #     print(x)
    #
    # results.clear()

    # 모든 좌표에 대하여 탐색
    for i in range(h):
        for j in range(w):
            # 섬을 발견했다면 Result 를 1 늘리고 BFS 를 통해 값을 모두 0으로 바꿈
            if graph[i][j] == 1:
                result += 1
                bfs(graph, i, j, w, h)

    results.append(result)

for x in results:
    print(x)
