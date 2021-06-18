from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
MAX = 100_001
visited = [-1] * MAX
visited[n] = 0
count = 0

queue = deque()
queue.append(n)

while queue:
    pos = queue.popleft()
    route = [pos * 2, pos + 1, pos - 1]
    if pos == k:
        count += 1
    for x in route:
        if 0 <= x < MAX:
            if visited[x] == -1 or visited[x] >= visited[pos] + 1:
                visited[x] = visited[pos] + 1
                queue.append(x)

print(visited[k])
print(count)
