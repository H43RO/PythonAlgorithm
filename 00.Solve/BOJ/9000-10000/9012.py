
n = int(input())
result = []

for i in range(n):
    stack = []
    data = list(input())

    for x in data:
        if x == ")" and len(stack) > 0 and stack[len(stack) - 1] == "(":
            stack.pop()
            continue
        elif x == "(":
            stack.append(x)
            continue
        stack.append(x)

    if not stack:
        result.append("YES")
    else:
        result.append("NO")

for x in result:
    print(x)
