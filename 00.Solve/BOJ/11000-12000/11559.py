from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def available(i, j):
    if graph[i][j] == '.':
        return False
    color = graph[i][j]  # 뿌요 색상 저장
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True

    queue = deque([(i, j)])
    deleted = [(i, j)]  # 방문한 뿌요를 모두 저장

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나지 않고, 색상이 같은 뿌요이며 방문한 적이 없는 뿌요라면 이동
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                deleted.append((nx, ny))

    if len(deleted) >= 4:  # 방문한 뿌요가 4개 이상일 경우 (터질 수 있는 경우)
        for x, y in deleted:  # 해당 뿌요 그룹을 모두 터뜨려 줌
            graph[x][y] = '.'
        return True
    else:
        return False


graph = [list(stdin.readline().strip()) for _ in range(12)]
count = 0

while True:  # 매번 터질 수 있는 뿌요를 모두 터뜨리고, 연쇄 1 증가 후 중력 처리 함
    exploded = False
    for i in range(12):
        for j in range(6):
            # 해당 좌표가 '.' 이 아니며 뿌요가 터졌다면 플래그 활성화
            if available(i, j):
                exploded = True

    if not exploded:  # 어떤 뿌요도 터지지 않았다면 종료
        break

    count += 1

    # 중력 처리
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graph[j][i] != "." and graph[k][i] == ".":
                    graph[k][i] = graph[j][i]
                    graph[j][i] = "."
                    break

print(count)
