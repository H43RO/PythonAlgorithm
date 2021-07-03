from sys import stdin
from collections import deque

F, S, G, U, D = map(int, stdin.readline().split())
count = [-1] * (F + 1)
dx = [U, -D]

# BFS
queue = deque([S])
count[S] = 0
while queue:
    x = queue.popleft()
    for i in range(2):
        nx = x + dx[i]
        if 1 <= nx <= F and count[nx] == -1:
            queue.append(nx)
            count[nx] = count[x] + 1

print(count[G] if count[G] >= 0 else "use the stairs")
