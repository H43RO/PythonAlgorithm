import sys

n = int(sys.stdin.readline())
stack = []
result = []

for i in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push":
        stack.append(int(command[1]))
    if command[0] == "pop":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    if command[0] == "size":
        result.append(len(stack))
    if command[0] == "empty":
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    if command[0] == "top":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack) - 1])

for x in result:
    print(x)
