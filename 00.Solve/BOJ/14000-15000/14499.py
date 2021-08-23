from sys import stdin


def move(direction):
    if direction == 1:  # 0, 1번 스왑, 2, 3번 스왑, 4, 5번 스왑, 0, 2번 스왑, 3, 5번 스왑, 1, 2번 스왑, 3, 4번 스왑
        dice[0], dice[1] = dice[1], dice[0]
        dice[2], dice[3] = dice[3], dice[2]
        dice[4], dice[5] = dice[5], dice[4]
        dice[0], dice[2] = dice[2], dice[0]
        dice[3], dice[5] = dice[5], dice[3]
        dice[1], dice[2] = dice[2], dice[1]
        dice[3], dice[4] = dice[4], dice[3]
    if direction == 2:  # 0, 2번 스왑, 3, 5번 스왑, 2, 3번 스왑
        dice[0], dice[2] = dice[2], dice[0]
        dice[3], dice[5] = dice[5], dice[3]
        dice[2], dice[3] = dice[3], dice[2]
    if direction == 3:  # 1, 4번 스왑, 0, 1번 스왑, 4, 5번 스왑
        dice[1], dice[4] = dice[4], dice[1]
        dice[0], dice[1] = dice[1], dice[0]
        dice[4], dice[5] = dice[5], dice[4]
    if direction == 4:  # 0, 5번 스왑, 0, 1번 스왑, 4, 5번 스왑
        dice[0], dice[5] = dice[5], dice[0]
        dice[0], dice[1] = dice[1], dice[0]
        dice[4], dice[5] = dice[5], dice[4]


dice = [0, 0, 0, 0, 0, 0]  # [0] 이 윗면, [5] 가 바닥면

n, m, x, y, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
command_list = list(map(int, stdin.readline().split()))
vector = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for cmd in command_list:
    nx, ny = x + vector[cmd][0], y + vector[cmd][1]
    if 0 <= nx < n and 0 <= ny < m:  # 맵 밖을 벗어나지 않으면 진행
        x, y = nx, ny  # 주사위 이동
        move(cmd)
        if graph[x][y] == 0:  # 바닥이 0이면
            graph[x][y] = dice[5]  # 바닥에 주사위 밑면 복사
        else:  # 바닥이 0이 아니라면
            dice[5] = graph[x][y]  # 주사위 바닥면에 밟고 있는 값 이동
            graph[x][y] = 0

        print(dice[0])
