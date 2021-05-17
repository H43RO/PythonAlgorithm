from sys import stdin
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, stdin.readline().split())
graph = [[0] * M for _ in range(N)]
section = []


def bfs(x, y):
    count = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 이전에 그렸던 직사각형 영역이거나, 방문했던 곳이면 무시
            if graph[nx][ny] == 1:
                continue
            count += 1
            graph[nx][ny] = 1
            queue.append((nx, ny))

    # 만약 시작 좌표만 유효 영역이라면 1 리턴
    if count == 0:
        return count + 1
    return count


for _ in range(K):
    # 편의 상 입력을 거꾸로 받기
    y1, x1, y2, x2 = map(int, stdin.readline().split())
    # 직사각형 그리기 (BFS 탐색 시 구분을 위해 1로 표시)
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

# 직사각형 영역, 방문했던 영역 나머지 부분에 대하여 BFS 탐색 수행
# - 직사각형 영역, 방문한 영역 모두 1로 처리
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            # 반환 받은 영역의 넓이 저장
            section.append(bfs(i, j))

# 결과 출력
print(len(section))
for x in sorted(section):
    print(x, end=' ')
