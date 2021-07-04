from sys import stdin
from collections import deque
T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())  # 편의점 개수
    graph = [[0] * (n + 2) for _ in range(n + 2)]  # 간선 정보를 담을 그래프
    visited = [False] * (n + 2)
    node = []  # 노드 정보를 담을 리스트

    for i in range(n + 2):
        node.append(tuple(map(int, stdin.readline().split())))

    # 노드 간 간선 정보 입력해주기
    for i, v in enumerate(node):
        for j in range(n + 2):
            if i == j:  # 자기 자신에 대한 간선 X
                continue
            # 맥주를 마시면서 걸어갈 수 있는 최대 거리인 1000m 이내의 간선만 저장
            if abs(v[0] - node[j][0]) + abs(v[1] - node[j][1]) <= 1000:
                graph[i][j] = 1
                graph[j][i] = 1

    queue = deque([0])
    while queue:
        x = queue.popleft()
        for i in range(n + 2):
            if graph[x][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    print("happy" if visited[-1] else "sad")
