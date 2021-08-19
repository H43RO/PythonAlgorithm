from sys import stdin
from collections import deque

# 방향벡터 6개 선언
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(stdin.readline())
graph = [[-1] * n for _ in range(n)]  # 각 좌표까지의 최소 이동 횟수 (최단 거리) 담는 2차원 그래프
r1, c1, r2, c2 = map(int, stdin.readline().split())  # 데스 나이트 출발점, 도착점 저장

graph[r1][c1] = 0  # 첫 좌표의 거리를 항상 0

queue = deque([(r1, c1)])
while queue:
    x, y = queue.popleft()
    if x == r2 and y == c2:  # 만약 도착점에 도달했다면 최단 거리 출력 후 프로그램 종료
        print(graph[x][y])
        exit(0)
    for i in range(6):  # 6가지 방향 벡터를 적용하여
        nx = x + dx[i]  # 이동한 새로운 좌표 갱신
        ny = y + dy[i]  # (x, y) -> (nx, ny)
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:  # 그래프 내에서 이동했고 방문한 적 없다면
            graph[nx][ny] = graph[x][y] + 1  # 이전 좌표의 최단 거리 + 1 을 저장
            queue.append((nx, ny))

print(-1)  # BFS 탐색을 하면서 도착점에 도달하지 못했다면, 도착을 할 수 없는 경우임
