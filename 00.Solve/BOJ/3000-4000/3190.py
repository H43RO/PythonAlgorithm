from sys import stdin
from collections import deque

N = int(stdin.readline())
graph = [[0] * N for _ in range(N)]  # 그래프 0 으로 초기화

K = int(stdin.readline())
for _ in range(K):  # 그래프에 사과 위치 표시
    x, y = map(int, stdin.readline().split())
    graph[x - 1][y - 1] = 1  # 값을 1로 변경함으로써 사과 표시

L = int(stdin.readline())
rotate = deque([(stdin.readline().split()) for _ in range(L)])  # 방향 변환 정보

snake = deque([(0, 0)])  # 뱀의 본체 좌표 정보
vector = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}  # 상 우 하 좌 이동 벡터 정의
direction = 2  # 처음엔 오른쪽으로 진행

count = 0  # 게임 총 진행 시간
while True:
    count += 1  # 진행 시간 증가
    x, y = snake[-1]  # 이전 뱀 대가리 좌표
    nx, ny = x + vector[direction][0], y + vector[direction][1]  # 새로운 뱀 대가리 좌표

    # >>> 뱀 좌표 이동 시퀀스 <<<
    if (0 <= nx < N and 0 <= ny < N) and ((nx, ny) not in snake):  # 맵 밖으로 벗어나거나, 자기 몸이랑 부딪히면 게임 종료
        snake.append((nx, ny))  # 뱀 대가리 이동
        if graph[nx][ny] == 1:  # 사과 먹은거면 꼬리 유지 (몸 길이 1 증가)
            graph[nx][ny] = 0
        else:
            snake.popleft()  # 사과 먹은거 아니면 꼬리 자름 (몸 길이 유지)
    else:
        break

    # >>> 방향 변환 시퀀스 <<<
    if rotate and count == int(rotate[0][0]):  # 해당 시간에 방향 변환 정보가 있다면
        _, V = rotate.popleft()  # 해당 정보 pop() 후 방향 변환 처리
        # 방향 전환
        if V == 'L':  # 좌회전
            direction -= 1
            if direction == 0:
                direction = 4
        if V == 'D':  # 우회전
            direction += 1
            if direction == 5:
                direction = 1

print(count)
