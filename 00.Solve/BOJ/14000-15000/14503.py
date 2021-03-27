from sys import stdin, stdout

# 북, 동, 남, 서 방향 벡터 정의
vector = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

N, M = map(int, stdin.readline().split())
# 로봇 청소기 좌표 (R, C), 방향 D (북: 0, 동: 1, 남: 2, 서 : 3)
R, C, D = map(int, stdin.readline().split())

graph = []  # 빈 곳 : 0, 벽 : 1, 청소된 곳 : 2
for x in range(N):
    graph.append(list(map(int, stdin.readline().split())))

result = 0

while True:
    graph[R][C] = 2  # 현재 좌표 청소

    direction = D  # 방향을 바꿔보며 탐색하기 위해 현재 방향 복사
    move_available = False  # 이동 성공 여부 플래그 변수

    # 네 방향에 대하여 탐색
    for _ in range(4):
        if D > 0:
            direction = D - 1
        else:
            direction = 3

        nr, nc = R + vector[direction][0], C + vector[direction][1]  # 탐색할 좌표
        D = direction  # 해당 방향으로 방향 변경

        if graph[nr][nc] == 0:  # 청소되지 않은 빈 곳을 발견 했을 때
            R, C = nr, nc  # 그리고 좌표 이동
            move_available = True  # 이동 성공했기 때문에 플래그 변수 활성화
            break

    # 플래그 변수가 활성화되지 않았다면 (네 방향 모두 청소가 이미 되었거나 벽이라면)
    if not move_available:
        if D > 1:
            direction = D - 2
        else:
            direction = D + 2

        # 뒤쪽 방향이 벽이라서 후진도 할 수 없는 경우 break
        if graph[R + vector[direction][0]][C + vector[direction][1]] == 1:
            break
        # 후진할 수 있으면 방향 유지 + 후진
        else:
            R += vector[direction][0]
            C += vector[direction][1]

result = 0
for x in graph:
    result += x.count(2)
print(result)