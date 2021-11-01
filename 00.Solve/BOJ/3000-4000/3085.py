from sys import stdin


def search(graph):
    result = 0
    # 가로 탐색
    for i in range(n):
        temp = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j - 1]:
                temp += 1
                continue
            result = max(result, temp)
            temp = 1
        result = max(result, temp)

    # 세로 탐색
    for i in range(n):
        temp = 1
        for j in range(1, n):
            if graph[j][i] == graph[j - 1][i]:
                temp += 1
                continue
            result = max(result, temp)
            temp = 1
        result = max(result, temp)

    return result


n = int(stdin.readline())
graph = [list(stdin.readline().strip()) for _ in range(n)]

max_candy = 0

for i in range(n):
    for j in range(1, n):
        # 가로 탐색
        graph[i][j], graph[i][j - 1] = graph[i][j - 1], graph[i][j]
        max_candy = max(max_candy, search(graph))
        graph[i][j], graph[i][j - 1] = graph[i][j - 1], graph[i][j]

        # 세로 탐색
        graph[j][i], graph[j - 1][i] = graph[j - 1][i], graph[j][i]
        max_candy = max(max_candy, search(graph))
        graph[j][i], graph[j - 1][i] = graph[j - 1][i], graph[j][i]

print(max_candy)
