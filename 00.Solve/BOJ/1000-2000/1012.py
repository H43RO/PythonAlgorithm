import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 풀어줘야 함

def dfs(graph, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x + 1, y)
        dfs(graph, x, y + 1)
        return True
    return False


case = int(input())
result = [0] * case

for i in range(case):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for x in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for x in range(n):
        for y in range(m):
            if dfs(graph, x, y):
                result[i] += 1

for x in result:
    print(x)