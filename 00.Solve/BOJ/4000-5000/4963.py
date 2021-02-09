from sys import stdin, stdout
import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 풀어줘야 정답 처리


def dfs(graph, x, y, w, h):
    if 0 <= y < w and 0 <= x < h:
        if graph[x][y] == 1:
            graph[x][y] = 0
            # 상하좌우, 대각선에 대하여 모두 탐색
            dfs(graph, x - 1, y - 1, w, h)
            dfs(graph, x, y - 1, w, h)
            dfs(graph, x + 1, y - 1, w, h)
            dfs(graph, x - 1, y, w, h)
            dfs(graph, x + 1, y, w, h)
            dfs(graph, x - 1, y + 1, w, h)
            dfs(graph, x, y + 1, w, h)
            dfs(graph, x + 1, y + 1, w, h)
            return True
    return False


results = []
while True:
    result = 0
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if dfs(graph, i, j, w, h):
                result += 1
    results.append(result)

for x in results:
    print(x)
