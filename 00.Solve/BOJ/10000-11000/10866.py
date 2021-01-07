from collections import deque
import sys

result = []
deque = deque()

n = int(sys.stdin.readline())


def is_empty(deque):
    if len(deque) == 0:
        return True
    else:
        return False


for i in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push_back":
        deque.append(int(command[1]))
    if command[0] == "push_front":
        deque.appendleft(int(command[1]))
    if command[0] == "pop_front":
        if is_empty(deque):
            result.append(-1)
        else:
            result.append(deque.popleft())
    if command[0] == "pop_back":
        if is_empty(deque):
            result.append(-1)
        else:
            result.append(deque.pop())
    if command[0] == "size":
        result.append(len(deque))
    if command[0] == "empty":
        if is_empty(deque):
            result.append(1)
        else:
            result.append(0)
    if command[0] == "front":
        if is_empty(deque):
            result.append(-1)
        else:
            result.append(deque[0])
    if command[0] == "back":
        if is_empty(deque):
            result.append(-1)
        else:
            result.append(deque[len(deque) - 1])

for x in result:
    print(x)