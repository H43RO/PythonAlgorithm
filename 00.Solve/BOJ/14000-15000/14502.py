from sys import stdin, stdout, setrecursionlimit
from itertools import combinations
from collections import deque
import copy

setrecursionlimit(100000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))


n, m = map(int, stdin.readline().split())

graph = []

empty = []
virus = []

safe_size = []

for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(m):
        if temp[j] == 2:
            virus.append((i, j))
        if temp[j] == 0:
            empty.append((i, j))
    graph.append(temp)

# 벽 위치의 모든 경우의 수 고려하여 저장 (조합 개념 이용)
wall_list = list(combinations(empty, 3))

for wall in wall_list:
    # 매번 새로운 벽을 만들기 위해 그래프를 복사하여 사용
    temp_graph = copy.deepcopy(graph)
    # 3개의 벽을 만들어줌
    for x in wall:
        temp_graph[x[0]][x[1]] = 1

    for x in virus:
        bfs(x[0], x[1], temp_graph)

    safe_count = 0
    for x in temp_graph:
        safe_count += x.count(0)

    safe_size.append(safe_count)

print(max(safe_size))
