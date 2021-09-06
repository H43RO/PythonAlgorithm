import sys

INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신의 최단거리는 항상 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    # 양방향 간선 처리
    for x in fares:
        i, j, k = x
        graph[i][j] = k
        graph[j][i] = k

    # 플로이드 워셜 점화식 처리
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 경유하는 지점을 하나씩 바꿔가며 최단거리 탐색
    result = sys.maxsize
    for i in range(1, n + 1):
        if i == a or i == b or i == s:
            continue
        result = min(result, graph[a][i] + graph[i][b] + graph[i][s])

    # 엣지 케이스 처리 (e.g. 합승 안 할 때 더 빠른 경우, B 로 가는 길에 A 가 있는 경우 등)
    result = min(result, graph[s][a] + graph[s][b], graph[a][b] + graph[b][s], graph[a][b] + graph[a][s])

    return result


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

# 2021 카카오 블라인드 공채 4번
# 정답률 : 정확도 9.60%, 효율성 7.45%
# - 30분 소요
