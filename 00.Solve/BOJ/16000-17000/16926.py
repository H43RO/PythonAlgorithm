from sys import stdin


# 이전 칸에서 값 땡기는 함수
def move(x, y):
    global temp, graph

    original = graph[x][y]  # 해당 칸의 원래 값 저장
    graph[x][y] = temp  # 이전 칸의 값을 대입
    temp = original  # 다음 칸에서 원래 값 대입할 수 있도록 함


n, m, r = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
temp = graph[0][0]  # 첫 시작은 항상 (0, 0)

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = graph[x][y]

        for j in range(i + 1, n - i):  # 왼쪽 (아래로 진행)
            x = j  # 행 1 증가
            move(x, y)

        for j in range(i + 1, m - i):  # 아래 (오른쪽으로 진행)
            y = j  # 열 1 증가
            move(x, y)

        for j in range(i + 1, n - i):  # 오른쪽 (위로 진행)
            x = n - j - 1  # 행 1 감소
            move(x, y)

        for j in range(i + 1, m - i):  # 윗쪽 (왼쪽으로 진행)
            y = m - j - 1  # 열 1 감소
            move(x, y)

[print(*graph[i]) for i in range(n)]
