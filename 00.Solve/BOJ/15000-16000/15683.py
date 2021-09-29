import sys
from sys import stdin
from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = {  # 회전 고려한 감시 방향 모든 경우의 수
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


# DFS 탐색
def watch(index, matrix, blind_spot):
    global result

    # CCTV 개수만큼 진행
    # 혹은 모두 구역이 감시당하는 경우 종료
    if index == len(cctv) or blind_spot == 0:
        result = min(result, blind_spot)
        return

    cctv_x, cctv_y = cctv[index]
    cctv_type = data[cctv_x][cctv_y]

    for dir in direction[cctv_type]:
        current_blind_spot = blind_spot
        temp = deepcopy(matrix)

        for x in dir:
            not_blind_spot = 0  # 알고보니 사각지대가 아니였던 구역의 수
            nx, ny = cctv_x + dx[x], cctv_y + dy[x]

            while True:
                if not (0 <= nx < n and 0 <= ny < m):  # 유효하지 않은 영역
                    break
                if temp[nx][ny] == 6:  # 벽 만났을 경우
                    break

                if temp[nx][ny] == 0:  # 감시 가능한 경우
                    temp[nx][ny] = -1  # 감시 당함
                    not_blind_spot += 1
                    continue

                # 방향에 따라 진행
                nx += dx[x]
                ny += dy[x]

            current_blind_spot -= not_blind_spot  # 사각지대 감소

        watch(index + 1, temp, current_blind_spot)


n, m = map(int, stdin.readline().split())
data = [list(map(int, stdin.readline().split())) for _ in range(n)]

blind_spot = 0
cctv = []

result = sys.maxsize

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            blind_spot += 1
            continue
        if 1 <= data[i][j] <= 5:
            cctv.append((i, j))

if len(cctv) == 0:
    print(blind_spot)
    exit(0)

watch(0, data, blind_spot)

print(result)
