def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
        return True
    return False


def solution(n, computers):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                # 상호 연결 관계 그래프에 표현
                graph[i + 1].append(j + 1)

    for i in range(1, n + 1):
        if dfs(graph, i, visited):
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
