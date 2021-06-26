from sys import stdin, setrecursionlimit

setrecursionlimit(1000000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(graph, x, y, number):
    global result
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(graph, nx, ny, number + graph[nx][ny])


result = []
graph = [list(map(str, stdin.readline().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(graph, i, j, graph[i][j])

print(len(result))
