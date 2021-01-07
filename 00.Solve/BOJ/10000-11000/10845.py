from collections import deque
import sys

result = []
queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    command = list(sys.stdin.readline().split())
    
    if command[0] == "push":
        queue.append(int(command[1]))
    if command[0] == "pop":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    if command[0] == "size":
        result.append(len(queue))
    if command[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    if command[0] == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
    if command[0] == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[len(queue) - 1])


for x in result:
    print(x)
