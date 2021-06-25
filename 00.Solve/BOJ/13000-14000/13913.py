from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
MAX = 100_001
visited = [-1] * MAX
visited[n] = 0
path = [0] * MAX

queue = deque([n])
path[n] = [n]

while queue:
    pos = queue.popleft()
    route = [pos + 1, pos - 1, pos * 2]
    if pos == k:
        p = []
        while pos != n:
            p.append(pos)
            pos = path[pos]
        p.append(n)
        p.reverse()
        print(visited[k])
        print(' '.join(str(x) for x in p))
        break
    for x in route:
        if 0 <= x < MAX:
            if visited[x] == -1 or visited[x] >= visited[pos] + 1:
                visited[x] = visited[pos] + 1
                path[x] = pos
                queue.append(x)
