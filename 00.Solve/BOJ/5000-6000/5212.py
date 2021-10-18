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
        if temp[j] == 'X':  # 섬의 좌표 모두 저장
            island.append((i, j))
    graph.append(temp)

data = copy.deepcopy(graph)
for x, y in island:  # 섬 좌표 각각에서부터 인근 상하좌우 검사
    sea = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if data[nx][ny] == '.':  # 인접 바다 개수 세기
                sea += 1
        else:  # 지도 범위 벗어나는 곳도 바다
            sea += 1

    if sea >= 3:  # 만약 인접 3면 이상이 바다라면 침몰
        graph[x][y] = '.'


# 섬을 포함하는 가장 작은 직사각형의 네 꼭짓점 찾을 것
start_row = 0
end_row = 0
start_col = c - 1
end_col = 0

for i in range(r):
    if 'X' in graph[i]:  # 섬이 최초로 등장하는 가장 위의 행 저장
        start_row = i
        break

for i in range(r - 1, -1, -1):
    if 'X' in graph[i]:  # 섬이 최초로 등장하는 가장 아래의 행 저장
        end_row = i
        break

for i in range(start_row, end_row + 1):
    tmp = [i for i, v in enumerate(graph[i]) if v == 'X']  # 각 열에서 섬 인덱스 추출
    if not tmp:  # 모든 열에 섬이 없다면 패스
        continue

    start_col = min(start_col, tmp[0])  # 섬이 최초로 등장하는 가장 왼쪽 열 저장 (갱신
    end_col = max(end_col, tmp[-1])  # 섬이 최초로 등장하는 가장 오른쪽 열 저장 (갱신)

# 완성한 네 꼭짓점을 통해 해당 직사각형만큼 출력
for i in range(start_row, end_row + 1):
    for j in range(start_col, end_col + 1):
        print(graph[i][j], end='')
    print()
