from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())

# 자식, 부모가 어떻게 연결되어있는지 나타내는 2차원 그래프
graph = [[] for _ in range(n + 1)]
level = [-1] * (n + 1)  # 촌수를 나타낼 리스트 (방문한 적 없으면 -1)
level[a] = 0

for i in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)  # 양방향 순회 쌉 가능
    graph[y].append(x)

queue = deque([a])
while queue:
    v = queue.popleft()
    for x in graph[v]:  # 이웃노드들에 대하여
        if level[x] < 0:  # 방문한 적 없는 노드를 발견한 경우
            level[x] = level[v] + 1  # 촌수를 늘려서 해당 노드에 저장
            queue.append(x)

print(level[b] if level[b] != 0 else -1)
