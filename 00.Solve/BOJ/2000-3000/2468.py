import copy
from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, graph, rain):
    # 방문한 적 있거나 물에 잠기는 영역인 경우 탐색 X
    if graph[i][j] == -1 or graph[i][j] <= rain:
        return False

    queue = deque([(i, j)])
    graph[i][j] = -1  # 방문 처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동하려는 곳에 방문한 적 없으며, 비에 잠기지 않는 영역이면 이동할 수 있음
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and graph[nx][ny] > rain:
                queue.append((nx, ny))
                graph[nx][ny] = -1

    return True


n = int(stdin.readline())
data = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, data))

result = 1  # 비가 안 올 땐 항상 안전 영역 1 (전체)
for rain in range(1, max_height):
    graph = copy.deepcopy(data)  # 그래프 정보 매번 복사 (방문처리 때문)
    section = 0  # 안전 영역을 담을 변수
    for i in range(n):
        for j in range(n):
            if bfs(i, j, graph, rain):  # BFS 탐색을 수행했다면
                section += 1  # 안전 영역 1 증가
    result = max(result, section)

print(result)
