from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [-1 for i in range(n + 1)]
distance[1] = 0

count = -1

queue = deque([1])  # 노드 번호, 거리 (탐색 시작 노드 1번)
while queue:
    x = queue.popleft()

    if distance[x] <= 2:  # 친구, 친구의 친구 (거리 2 이하) 초대
        count += 1

    for nx in graph[x]:
        if distance[nx] == -1:  # 방문한 적이 없다면
            distance[nx] = distance[x] + 1  # 이전 노드로부터 거리 1 증가
            queue.append(nx)

print(count)
