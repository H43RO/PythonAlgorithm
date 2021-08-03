from sys import stdin
from collections import deque

# F : 층수, S : 현 위치, G : 스타트링크 위치, U : 위로 가는 층 수, D: 아래로 가는 층 수
F, S, G, U, D = map(int, stdin.readline().split())
visited = [-1] * (F + 1)
dx = [U, -D]  # 이동 가능 벡터 : U 층만큼 올라가기, D 층만큼 내려가기

queue = deque([S])  # 시작 위치 큐잉
visited[S] = 0  # 각 층까지의 최단거리 (최소 버튼 누른 수) 저장
while queue:
    x = queue.popleft()
    for i in range(2):
        nx = x + dx[i]
        if 1 <= nx <= F and visited[nx] == -1:  # 범위 안 벗어나고 방문한 적 없는 층이면
            queue.append(nx)
            visited[nx] = visited[x] + 1

print(visited[G] if visited[G] >= 0 else "use the stairs")
