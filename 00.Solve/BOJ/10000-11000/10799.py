from sys import stdin, stdout

data = list(stdin.readline().strip())
stack = []
result = 0

for i, v in enumerate(data):
    if data[i - 1] == "(" and v == ")":
        stack.pop()
        result += len(stack)
    elif v == "(":
        stack.append(v)
    elif v == ")":
        stack.pop()
        result += 1

print(result)