from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append([0, 0, 1])

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while queue:
        x, y, w = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽으로 가로 막혀있고, 벽을 뚫을 수 있는 경우
                if graph[nx][ny] == 1 and w == 1:
                    # 벽을 뚫고 최단 거리 + 1 저장
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    # 벽을 뚫고 왔으므로 w 에 0 넣어서 경로 큐잉
                    queue.append([nx, ny, 0])
                # 이동할 수 있는 곳이고, 아직 방문하지 않은 곳이라면
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    # 최단 거리 저장 후 경로 큐잉
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1


n, m = map(int, stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(stdin.readline().strip()))))
print(bfs())
