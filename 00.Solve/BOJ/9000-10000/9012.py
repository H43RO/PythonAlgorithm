n = int(input())
result = []

for i in range(n):
    stack = []
    data = list(input())

    for x in data:
        # Pairing 되는 괄호가 발견되면 pop() 하고 계속 진행
        if x == ")" and len(stack) > 0 and stack[len(stack) - 1] == "(":
            stack.pop()
            continue
        # "(" 가 입력된 경우 일단 Stack 에 push()
        elif x == "(":
            stack.append(x)
            continue
        # 모두 해당하지 않는 경우에도 일단 Stack 에 push()
        stack.append(x)

    # Stack 내 모든 괄호가 Pairing 된 경우 Stack 이 비어있어야 함
    if not stack:
        result.append("YES")
    else:
        result.append("NO")

for x in result:
    print(x)
