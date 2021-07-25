from collections import deque
from sys import stdin

MAX_LITER = 201
a, b, c = map(int, stdin.readline().split())

visited = [[False] * MAX_LITER for _ in range(MAX_LITER)]
result = [0 for _ in range(MAX_LITER)]

queue = deque([(0, 0, c)])
while queue:
    x, y, z = queue.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True

    if x == 0:
        result[z] = 1

    if x + y > b:
        queue.append((x + y - b, b, z))
    else:
        queue.append((0, x + y, z))

    if x + z > c:
        queue.append((x + z - c, y, c))
    else:
        queue.append((0, y, x + z))

    if y + x > a:
        queue.append((a, y + x - a, z))
    else:
        queue.append((y + x, 0, z))

    if y + z > c:
        queue.append((x, y + z - c, c))
    else:
        queue.append((x, 0, y + z))

    if z + x > a:
        queue.append((a, y, z + x - a))
    else:
        queue.append((z + x, y, 0))

    if z + y > b:
        queue.append((x, b, z + y - b))
    else:
        queue.append((x, z + y, 0))


for i, v in enumerate(result):
    if v > 0:
        print(i, end=' ')
