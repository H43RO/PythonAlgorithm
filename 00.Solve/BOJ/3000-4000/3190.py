from sys import stdin
from collections import deque

N = int(stdin.readline())
graph = [[0] * N for _ in range(N)]  # 그래프 0 으로 초기화

K = int(stdin.readline())
for _ in range(K):  # 그래프에 사과 위치 표시
    x, y = map(int, stdin.readline().split())
    graph[x - 1][y - 1] = 1

rotate = deque([])  # 방향 변환 정보

L = int(stdin.readline())
for _ in range(L):
    C, D = stdin.readline().strip().split()
    rotate.append((C, D))

count = 0  # 게임 총 진행 시간
snake = deque([(0, 0)])  # 뱀의 본체 현재 좌표 정보
vector = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}  # 상 우 하 좌
direction = 2

while True:
    count += 1  # 진행 시간 증가
    x, y = snake[-1]  # 이전 뱀 대가리 좌표
    nx, ny = x + vector[direction][0], y + vector[direction][1]
    # 맵 밖으로 벗어나거나, 자기 몸이랑 부딪히면 게임 종료
    if (0 <= nx < N and 0 <= ny < N) and ((nx, ny) not in snake):
        snake.append((nx, ny))  # 뱀 대가리 이동
        if graph[nx][ny] == 1:  # 사과 먹은거면 꼬리 유지 (몸 길이 1 증가)
            graph[nx][ny] = 0
        else:
            snake.popleft()  # 사과 먹은거 아니면 꼬리 자름 (몸 길이 유지)
    else:
        break

    if rotate and count == int(rotate[0][0]):  # 해당 시간에 방향 변환 정보가 있다면
        _, V = rotate.popleft()  # 해당 정보 pop 후 방향 변환 처리
        # 방향 전환
        if V == 'L':
            direction -= 1
            if direction == 0:
                direction = 4
        if V == 'D':
            direction += 1
            if direction == 5:
                direction = 1

print(count)
