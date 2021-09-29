import sys
from sys import stdin
from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = {  # CCTV 종류에 따른 회전 고려한 감시 방향의 모든 경우의 수
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    5: [(0, 1, 2, 3)]
}


# DFS 탐색
def watch(index, matrix, blind_spot):
    global result

    # CCTV 개수만큼 진행
    # 혹은 모두 구역이 감시당하는 경우 종료
    if index == len(cctv) or blind_spot == 0:
        result = min(result, blind_spot)
        return

    cctv_x, cctv_y = cctv[index]  # 현재 탐색중인 CCTV 의 좌표
    cctv_type = data[cctv_x][cctv_y]  # 현재 탐색중인 CCTV 가 어떤 놈인지

    for dir in direction[cctv_type]:  # 해당 CCTV 타입에 맞는 방향 벡터 하나씩 탐색
        current_blind_spot = blind_spot  # 현재 탐색중인 CCTV 감시 방향에 따른 사각지대 크기 탐색
        temp = deepcopy(matrix)  # 데이터 변형이 이루어지므로 원본 냅두고 그래프 복사본 따로 생성

        for x in dir:  # 방향 벡터 하나씩 뜯어보기
            watch_spot = 0  # 감시 당하는 구역의 크기
            nx, ny = cctv_x + dx[x], cctv_y + dy[x]  # 현재 CCTV 감시 방향에 따라 이동해보기

            while (0 <= nx < n and 0 <= ny < m) and temp[nx][ny] != 6:  # 유효한 범위 안에 있고 벽을 만나지 않은 경우
                if temp[nx][ny] == 0:  # 감시 가능한 경우
                    print(nx, ny, temp[nx][ny])
                    temp[nx][ny] = -1  # '감시 당함' 표시로 -1 삽입
                    watch_spot += 1  # 감시 당하는 구역 1 증가
                    continue

                # 종료 조건까지 한 칸 더 진행
                nx += dx[x]
                ny += dy[x]

            current_blind_spot -= watch_spot  # 감시 당하는 구역 크기만큼 사각지대 감소
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
