from sys import stdin
from collections import deque

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs(start_x, start_y):
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:  # 가장 가까운 아기상어를 찾았을 때 그 거리를 반환
            return visited[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  # 아기상어가 없는 곳에서 BFS 수행
            result = max(result, bfs(i, j))  # 최댓값으로 결과값 갱신
print(result)