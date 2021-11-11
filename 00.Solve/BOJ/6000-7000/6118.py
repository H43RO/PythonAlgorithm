from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]  # 각 헛간로부터 다른 헛간으로 갈 수 있는 경로 저장

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)  # 양방향 경로
    graph[b].append(a)

dist = [-1] * (n + 1)  # 1번 헛간으로부터의 거리 정보를 담는 리스트 (미방문시 -1)
dist[1] = 0

queue = deque([1])
while queue:
    node = queue.popleft()
    for x in graph[node]:  # 해당 헛간으로부터 다른 헛간으로 갈 수 있는 경로들 탐색
        if dist[x] == -1:  # 만약 처음 방문하는 헛간이라면
            dist[x] = dist[node] + 1  # 거리 + 1 저장
            queue.append(x)

print(dist.index(max(dist)), max(dist), dist.count(max(dist)))  # 문제 요구사항대로 출력
