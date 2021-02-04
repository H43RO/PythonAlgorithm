from sys import stdin, stdout
from collections import deque

queue = deque()
n = int(stdin.readline())

for i in range(n):
    queue.append(i + 1)

while queue:
    if len(queue) == 1:
        print(queue[0])
        break
    else:
        queue.popleft()
        queue.append(queue.popleft())
