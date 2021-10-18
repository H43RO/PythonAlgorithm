import copy
from sys import stdin

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, stdin.readline().split())

graph = []
island = []
for i in range(r):
    temp = list(stdin.readline().strip())
    for j in range(c):
        if temp[j] == 'X':
            island.append((i, j))
    graph.append(temp)

data = copy.deepcopy(graph)
for x, y in island:
    sea = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if data[nx][ny] == '.':
                sea += 1
        else:
            sea += 1

    if sea >= 3:
        graph[x][y] = '.'

start_row = 0
start_col = 0
end_row = 0
end_col = 0

min_index = c - 1
max_index = 0

for i in range(r):
    if 'X' in graph[i]:
        start_row = i
        break

for i in range(r - 1, -1, -1):
    if 'X' in graph[i]:
        end_row = i
        break

for i in range(start_row, end_row + 1):
    tmp = [i for i, v in enumerate(graph[i]) if v == 'X']
    if not tmp:
        continue
    min_tmp = tmp[0]
    max_tmp = tmp[-1]

    min_index = min(min_index, min_tmp)
    max_index = max(max_index, max_tmp)

for i in range(start_row, end_row + 1):
    for j in range(min_index, max_index + 1):
        print(graph[i][j], end='')
    print()
