from sys import stdin
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    result = 1  # 총 면적 담을 변수
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                result += 1  # 면적 1 증가

    # 면적 반환
    return result


n, m, k = map(int, stdin.readline().split())
graph = [[0] * m for _ in range(n)]
waste = []
result = 0

for _ in range(k):
    x, y = map(int, stdin.readline().split())
    graph[x - 1][y - 1] = 1
    waste.append((x - 1, y - 1))  # 음식물 쓰레기 좌표 모두 저장

for x in waste:
    i, j = x
    result = max(result, bfs(graph, i, j))  # 면적 저장
print(result)
