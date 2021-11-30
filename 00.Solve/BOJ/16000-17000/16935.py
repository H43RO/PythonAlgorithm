from sys import stdin


def operation_1():
    """
    상하반전
    """
    global graph

    graph = graph[::-1]


def operation_2():
    """
    좌우 반전
    """
    global graph

    for i in range(n):
        graph[i] = graph[i][::-1]


def operation_3():
    """
    오른쪽으로 90도 회전
    """
    global n, m, graph

    n, m = m, n
    temp = [list(x)[::-1] for x in zip(*graph)]

    graph = temp


def operation_4():
    """
    왼쪽으로 90도 회전
    """
    global n, m, graph

    n, m = m, n
    temp = [list(x) for x in list(zip(*graph))[::-1]]

    graph = temp


def operation_5():
    """
    부분 배열 시계방향 회전
    """
    global graph

    temp = [[0] * m for _ in range(n)]  # 회전한 결과를 담을 변수

    n_temp = n // 2  # 부분 배열 쪼개기
    m_temp = m // 2

    for i in range(n_temp):
        for j in range(m_temp):  # 1번 그룹을 2번 그룹으로
            temp[i][m_temp + j] = graph[i][j]

    for i in range(n_temp):
        for j in range(m_temp, m):  # 2번 그룹을 3번 그룹으로
            temp[n_temp + i][j] = graph[i][j]

    for i in range(n_temp, n):
        for j in range(m_temp, m):  # 3번 그룹을 4번 그룹으로
            temp[i][j - m_temp] = graph[i][j]

    for i in range(n_temp, n):
        for j in range(m_temp):  # 4번 그룹을 1번 그룹으로
            temp[i - n_temp][j] = graph[i][j]

    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[i][j]  # 변경된 그래프 갱신


def operation_6():
    """
    부분배열 반시계 방향 회전
    """
    global graph
    temp = [[0] * m for _ in range(n)]  # 회전한 결과를 담을 변수

    n_temp = n // 2  # 부분 배열 쪼개기
    m_temp = m // 2

    for i in range(n_temp):
        for j in range(m_temp):  # 1번 그룹을 4번 그룹으로
            temp[n_temp + i][j] = graph[i][j]

    for i in range(n_temp, n):
        for j in range(m_temp):  # 4번 그룹을 3번 그룹으로
            temp[i][j + m_temp] = graph[i][j]

    for i in range(n_temp, n):
        for j in range(m_temp, m):  # 3번 그룹을 2번 그룹으로
            temp[i - n_temp][j] = graph[i][j]

    for i in range(n_temp):
        for j in range(m_temp, m):  # 2번 그룹을 1번 그룹으로
            temp[i][j - m_temp] = graph[i][j]

    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[i][j]  # 변경된 그래프 갱신


n, m, r = map(int, stdin.readline().split())
graph = [stdin.readline().split() for _ in range(n)]
operation = list(map(int, stdin.readline().split()))

for x in operation:
    if x == 1:
        operation_1()
    elif x == 2:
        operation_2()
    elif x == 3:
        operation_3()
    elif x == 4:
        operation_4()
    elif x == 5:
        operation_5()
    elif x == 6:
        operation_6()

for x in graph:
    print(*x)
