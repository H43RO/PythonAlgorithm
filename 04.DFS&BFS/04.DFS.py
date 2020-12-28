# DFS (Depth - First Search)

# 각 노드가 어떻게 연결되어 있는지에 대한 정보(그래프)를 2차원 리스트로 표현
graph = [
    [],         # 0번 노드의 인접노드 ( 편의상 사용하지 않음 )
    [2, 3, 8],  # 1번 노드의 인접노드
    [1, 7],     # 2번 노드의 인접노드
    [1, 4, 5],  # 3번 노드의 인접노드
    [3, 5],     # 4번 노드의 인접노드
    [3, 4],     # 5번 노드의 인접노드
    [7],        # 6번 노드의 인접노드
    [2, 6, 8],  # 7번 노드의 인접노드
    [1, 7]      # 8번 노드의 인접노드
]

visited = [False] * 9  # 편의상 0번 노드를 비우기 위함


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



dfs(graph, 1, visited)
