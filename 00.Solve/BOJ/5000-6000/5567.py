from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1
visited = [False] * (n + 1)
visited[1] = True

queue = deque([(1, 0)])  # 노드 번호, 거리

while queue:
    x, dist = queue.popleft()
    if dist <= 2:
        count += 1

    for x in graph[x]:
        if not visited[x]:
            visited[x] = True
            queue.append((x, dist + 1))

print(count)
