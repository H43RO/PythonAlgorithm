from sys import stdin
from collections import deque


def bfs(graph, start, visited):
    # BFS 큐에 항상 튜플형태로 (사람 번호, 케빈 베이컨 단계) 저장
    queue = deque([(start, 0)])
    visited[start] = True
    count = 0

    while queue:
        v, level = queue.popleft()
        # 케빈 베이컨 단계만큼 결과값 더해줌
        count += level
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                # 케빈 베이컨 단계 1 증가
                queue.append((i, level + 1))

    return count


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]  # 친구 관계를 담는 그래프
kevin = []  # 케빈 베이컨 지수를 차례대로 담을 배열

for _ in range(M):
    # 양방향 관계 그래프에 명시
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번부터 N번 각각의 케빈 베이컨 지수 계산
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    kevin.append(bfs(graph, i, visited))

# 케빈 베이컨 지수가 가장 낮은 사람의 번호 출력 (Zero-base)
print(kevin.index(min(kevin)) + 1)