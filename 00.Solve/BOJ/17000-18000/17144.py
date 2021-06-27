import copy
from collections import deque
from sys import stdin
from copy import deepcopy

R, C, T = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(R)]
vector = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dust = deque()
cleaner = []

for x in range(R):
    for y in range(C):
        # 공기 청정기 위치 저장
        if graph[x][y] == -1:
            cleaner.append((x, y))
            cleaner.append((x + 1, y))
            break

# 미세먼지를 큐에 담아서 한 번에 확산
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                dust.append((i, j, graph[i][j]))
    while dust:
        x, y, A = dust.popleft()
        for dx, dy in vector:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                graph[nx][ny] += A // 5
                # 기존 위치에 있던 미세먼지는 퍼진만큼 줄어든다.
                graph[x][y] -= A // 5

    temp = copy.deepcopy(graph)
    # 공기청정기 위치에 따라 먼지를 이동시켜 줌
    for x in range(R):
        for y in range(C):
            if x == cleaner[0][0] and cleaner[0][1] < y < C:
                graph[x][y] = temp[x][y - 1]
            elif y == C - 1 and x < cleaner[0][0]:
                graph[x][y] = temp[x + 1][y]
            elif x == 0 and y < C:
                graph[x][y] = temp[x][y + 1]
            elif y == 0 and x < cleaner[0][0]:
                graph[x][y] = temp[x - 1][y]
            elif x == cleaner[1][0] and cleaner[1][1] < y < C:
                graph[x][y] = temp[x][y - 1]
            elif y == C - 1 and x > cleaner[1][0]:
                graph[x][y] = temp[x - 1][y]
            elif x == R - 1 and y < C - 1:
                graph[x][y] = temp[x][y + 1]
            elif y == 0 and x > cleaner[1][0]:
                graph[x][y] = temp[x + 1][y]
    # 공기청정기가 이동하는 것을 방지
    graph[cleaner[0][0]][cleaner[0][1] + 1] = 0
    graph[cleaner[1][0]][cleaner[1][1] + 1] = 0

result = sum([sum(x) for x in graph])
# 공기청정기 (-1) 두 개가 있으므로 +2
print(result + 2)
