from sys import stdin, stdout

# 북, 동, 남, 서 방향 벡터 정의 (Dictionary 형태)
vector = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

# 그래프 크기 세로 N, 가로 M
N, M = map(int, stdin.readline().split())
# 로봇 청소기 현재 좌표 (R, C), 방향 D (북: 0, 동: 1, 남: 2, 서 : 3)
R, C, D = map(int, stdin.readline().split())

graph = []  # 빈 곳 : 0, 벽 : 1, 청소된 곳 : 2
result = 0  # 로봇 청소기가 청소하는 칸의 개수

# 그래프 정보 입력
for x in range(N):
    graph.append(list(map(int, stdin.readline().split())))

while True:
    graph[R][C] = 2  # 현재 좌표 청소

    direction = D  # 방향을 바꿔보며 탐색하기 위해 현재 방향 복사해 둠
    move_available = False  # 이동 성공 여부 플래그 변수

    # 네 방향에 대하여 탐색
    for _ in range(4):
        if D != 0:  # 만약 현재 방향이 북쪽이 아니라면 (동, 남, 서 중 하나라면)
            direction = D - 1  # 왼쪽 방향으로 회전
        else:  # 만약 북쪽을 보고 있었다면 서쪽 방향을 보게끔 함
            direction = 3

        # 변경할 방향의 벡터 값 만큼 현재 좌표에서 이동
        nr, nc = R + vector[direction][0], C + vector[direction][1]  # 탐색할 좌표
        D = direction  # 해당 방향으로 방향 변경

        if graph[nr][nc] == 0:  # 청소되지 않은 빈 곳을 발견 했을 때
            R, C = nr, nc  # 그리고 좌표 이동
            move_available = True  # 이동 성공했기 때문에 플래그 변수 활성화
            break

        # 만약 현재 탐색중인 방향이 청소가 불가능 할 때는 다시 for 문 처음으로 돌아가는 등
        # 방향을 전부 탐색해 봄 (모두 불가능하다면 플래그 변수는 False 상태임)

    # 플래그 변수가 활성화되지 않았다면 (네 방향 모두 청소가 이미 되었거나 벽이라면)
    if not move_available:
        if D != 1:  # 만약 현재 방향이 북쪽이 아니라면 (동, 남, 서 중 하나라면)
            direction = D - 2  # 뒤쪽을 바라보게 함
        else:  # 만약 북쪽을 보고 있었다면 서쪽 방향을 보게끔 함
            direction = D + 2  # 뒤쪽을 바라보게 함 (남쪽을 바라보게 함)

        # 만약 뒤쪽 방향이 벽이라서 후진도 할 수 없는 경우 작동 멈춤
        if graph[R + vector[direction][0]][C + vector[direction][1]] == 1:
            break
        # 후진할 수 있으면 방향 유지한 채 후진
        else:
            R += vector[direction][0]
            C += vector[direction][1]

# 청소한 구역 (2) 개수 출력
for x in graph:
    result += x.count(2)
print(result)