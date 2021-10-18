from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(visited, i, j):
    """
    시작점으로부터 열 수 있는 모든 국경선 개방
    """
    visited[i][j] = True
    queue = deque([(i, j)])
    union_list = [(i, j)]  # 연합을 이루는 국가 (좌표) 리스트

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    union_list.append((nx, ny))
                    queue.append((nx, ny))

    if union_list:
        people = 0
        for x, y in union_list:
            people += graph[x][y]

        union_people = people // len(union_list)
        for x, y in union_list:
            graph[x][y] = union_people

    return True if len(union_list) > 1 else False  # 연합이 시작점 단 하나일 경우 연합 없는 것


N, L, R = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

count = 0
while True:
    # 모든 좌표에 대해 BFS 돌아야함 (방문처리 해주면서) -> 국경선 개방
    visited = [[False] * N for _ in range(N)]
    available = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 방문하지 않은 국가에 대해 탐색 시작
                has_union = bfs(visited, i, j)  # 열 수 있는 모든 국경선 개방
                if has_union:
                    available = True
    if available:
        count += 1
    else:
        break

print(count)
