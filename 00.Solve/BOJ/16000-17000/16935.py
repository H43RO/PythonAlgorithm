from sys import stdin


def operation_1():
    global graph

    graph = graph[::-1]


def operation_2():
    global graph

    for i in range(n):
        graph[i] = graph[i][::-1]


def operation_3():
    global n, m, graph

    n, m = m, n
    temp = [list(row)[::-1] for row in zip(*graph)]

    graph = temp


def operation_4():
    global n, m, graph

    n, m = m, n
    temp = [list(row) for row in list(zip(*graph))[::-1]]

    graph = temp


def operation_5():
    global graph

    temp = [[0] * m for _ in range(n)]

    n_temp = n // 2
    m_temp = m // 2

    for i in range(n_temp):
        for j in range(m_temp):
            temp[i][m_temp + j] = graph[i][j]
    for i in range(n_temp):
        for j in range(m_temp, m):
            temp[n_temp + i][j] = graph[i][j]
    for i in range(n_temp, n):
        for j in range(m_temp, m):
            temp[i][j - m_temp] = graph[i][j]
    for i in range(n_temp, n):
        for j in range(m_temp):
            temp[i - n_temp][j] = graph[i][j]

    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[i][j]


def operation_6():
    global graph
    temp = [[0] * m for _ in range(n)]

    n_temp = n // 2
    m_temp = m // 2

    for i in range(n_temp):
        for j in range(m_temp):
            temp[n_temp + i][j] = graph[i][j]
    for i in range(n_temp, n):
        for j in range(m_temp):
            temp[i][j + m_temp] = graph[i][j]
    for i in range(n_temp, n):
        for j in range(m_temp, m):
            temp[i - n_temp][j] = graph[i][j]
    for i in range(n_temp):
        for j in range(m_temp, m):
            temp[i][j - m_temp] = graph[i][j]

    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[i][j]


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
