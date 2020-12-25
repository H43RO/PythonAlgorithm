# DFS ( Depth - First Search )

graph = [
    [],  # 0번 노드의 인접노드 ( 편의상 사용하지 않음 )
    [2, 3, 8],  # 1번 노드의 인접노드
    [1, 7],  # 2번 노드의 인접노드
    [1, 4, 5],  # 3번 노드의 인접노드
    [3, 5],  # 4번 노드의 인접노드
    [3, 4],  # 5번 노드의 인접노드
    [7],  # 6번 노드의 인접노드
    [2, 6, 8],  # 7번 노드의 인접노드
    [1, 7]  # 8번 노드의 인접노드
]

visited = [False] * 9  # 편의상 0번 노드를 비우기 위함


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)