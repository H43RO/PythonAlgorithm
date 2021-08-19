from sys import stdin


def move_east():  # 1, 동
    """
    1. 0번, 1번 스왑
    2. 2번, 3번 스왑
    3. 4번, 5번 스왑
    4. 0번, 2번 스왑
    5. 3번, 5번 스왑
    6. 1번, 2번 스왑
    7. 3번, 4번 스왑
    """
    dice[0], dice[1] = dice[1], dice[0]
    dice[2], dice[3] = dice[3], dice[2]
    dice[4], dice[5] = dice[5], dice[4]
    dice[0], dice[2] = dice[2], dice[0]
    dice[3], dice[5] = dice[5], dice[3]
    dice[1], dice[2] = dice[2], dice[1]
    dice[3], dice[4] = dice[4], dice[3]


def move_west():  # 2, 서
    """
    1. 0번, 2번 스왑
    2. 3번, 5번 스왑
    3. 2번, 3번 스왑
    """
    dice[0], dice[2] = dice[2], dice[0]
    dice[3], dice[5] = dice[5], dice[3]
    dice[2], dice[3] = dice[3], dice[2]


def move_north():  # 3, 북
    """
    1. 1번, 4번 스왑
    2. 0번, 1번 스왑
    3. 4번, 5번 스왑
    """
    dice[1], dice[4] = dice[4], dice[1]
    dice[0], dice[1] = dice[1], dice[0]
    dice[4], dice[5] = dice[5], dice[4]


def move_south():  # 4, 남
    """
    1. 0번, 5번 스왑
    2. 0번, 1번 스왑
    3. 4번, 5번 스왑
    """
    dice[0], dice[5] = dice[5], dice[0]
    dice[0], dice[1] = dice[1], dice[0]
    dice[4], dice[5] = dice[5], dice[4]


dice = [0, 0, 0, 0, 0, 0]  # [0] 이 윗면, [5] 가 바닥면

# 의사 코드
# 1. 이동을 해도 된다면 (맵을 벗어나지 않는다면), 명령에 따라 이동완료
# 2. 칸이랑 주사위 바닥면 고려 로직 수행
# 3. 주사위 윗면 출력

n, m, x, y, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
command_list = list(map(int, stdin.readline().split()))
vector = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for cmd in command_list:
    nx, ny = x + vector[cmd][0], y + vector[cmd][1]
    if 0 <= nx < n and 0 <= ny < m:  # 맵 밖을 벗어나지 않으면 진행
        x, y = nx, ny  # 주사위 이동
        if cmd == 1:
            move_east()
        if cmd == 2:
            move_west()
        if cmd == 3:
            move_north()
        if cmd == 4:
            move_south()
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0

        print(dice[0])
