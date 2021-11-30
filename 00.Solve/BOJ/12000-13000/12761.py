from sys import stdin
from collections import deque

a, b, n, m = map(int, stdin.readline().split())
dx = [1, -1, a, -a, b, -b, a, b]

visited = [0 for i in range(100001)]
visited[n] = 1
queue = deque([n])

while queue:
    x = queue.popleft()
    for i in range(8):
        if i < 6:
            nx = x + dx[i]
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1
        else:
            nx = x * dx[i]
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1

print(visited[m])
