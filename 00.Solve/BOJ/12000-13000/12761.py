from sys import stdin
from collections import deque

a, b, n, m = map(int, stdin.readline().split())
dx = [1, -1, a, -a, b, -b, a, b]  # 총 8가지 이동 가능

distance = [-1 for i in range(100001)]
distance[n] = 0

queue = deque([n])
while queue:
    x = queue.popleft()
    for i in range(8):
        if i < 6:
            nx = x + dx[i]
        else:  # 7, 8번 백터는 A배, B배 위치로 이동
            nx = x * dx[i]
        if 0 <= nx <= 100000 and distance[nx] == -1:
            queue.append(nx)
            distance[nx] = distance[x] + 1

print(distance[m])  # 최단 거리 출력
