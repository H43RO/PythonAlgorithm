import sys

INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for x in fares:
        i, j, k = x
        graph[i][j] = k
        graph[j][i] = k

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    result = sys.maxsize
    for i in range(1, n + 1):
        if i == a or i == b or i == s:
            continue
        result = min(result, graph[a][i] + graph[i][b] + graph[i][s])

    result = min(result, graph[s][a] + graph[s][b], graph[a][b] + graph[b][s], graph[a][b] + graph[a][s])

    return result


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

# 정확도, 효율성 30분 (홀인원)
