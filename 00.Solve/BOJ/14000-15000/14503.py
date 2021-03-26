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

    graph[R][C] = 2
    direction = D
    flag = False
    for _ in range(4):
        if D > 0:
            direction = D - 1
        else:
            direction = 3
        nr, nc = R + vector[direction][0], C + vector[direction][1]

        if graph[nr][nc] == 0:
            D = direction
            R, C = nr, nc
            flag = True
            break
        else:
            D = direction
    if flag:
        continue

    if D > 1:
        direction = D - 2
    else:
        direction = D + 2

    if graph[R + vector[direction][0]][C + vector[direction][1]] == 1:
        break
    else:
        R += vector[direction][0]
        C += vector[direction][1]

print(sum(graph, []).count(2))
