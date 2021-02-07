n = int(input())
edge = int(input())

# 노드 간 연결 정보를 담을 그래프 (2차원 리스트) 선언
graph = [[] * (n + 1) for _ in range(n + 1)]
# 방문 정보를 담을 리스트 선언
visited = [False] * (n + 1)
result = 0

# 노드 정보를 담을 그래프 만들기
for i in range(edge):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

# 각 노드의 인접 노드 정렬
for x in graph:
    x.sort()


def dfs_function(graph, v):
    global result
    # 우선 입력받은 시작 노드는 방문 처리
    visited[v] = True
    # 감염 횟수 증가
    result += 1
    # 입력받은 시작 노드의 모든 인접 노드들에 대하여
    for i in graph[v]:
        # 만약 해당 인접 노드를 방문한 적 없다면
        if not visited[i]:
            # 해당 노드를 시작으로 DFS 탐색 시작
            dfs_function(graph, i)


# 1번 노드부터 DFS 탐색 시작
dfs_function(graph, 1)

# 1번 노드 방문 제외한 결과 출력
print(result-1)
