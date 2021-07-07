from sys import stdin
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(graph, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:  # 탐색이 끝 지점에 도달한 경우
            return graph[x][y]  # 해당 좌표의 값을 반환 (최소 몇 번 이동했는지)
        for i in range(8):  # 나이트가 이동할 수 있는 8개의 좌표 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == 0:  # 최초 방문이라면
                graph[nx][ny] = graph[x][y] + 1  # 이동횟수 1 늘려서 저장
                queue.append((nx, ny))


T = int(stdin.readline())

for _ in range(T):
    L = int(stdin.readline())
    graph = [[0] * L for _ in range(L)]  # 체스판 정보를 담는 L X L 그래프

    start_x, start_y = map(int, stdin.readline().split())
    end_x, end_y = map(int, stdin.readline().split())

    print(bfs(graph, start_x, start_y, end_x, end_y))
