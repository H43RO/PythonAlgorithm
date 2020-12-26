# BFS (Breadth-First Search)
# - 최단 거리 구하기에 사용할 수 있음

from collections import deque

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


def bfs(graph, start, visited):
    # 큐 구현을 위한 Deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접 노드들을 모두 큐에 삽입 후 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
