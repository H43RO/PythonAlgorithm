while True:
    stack = []
    is_able = True
    string = input()
    if string == '.':
        break
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        if x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_able = False
        if x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_able = False

    if stack or not is_able:
        print('no')
    else:
        print('yes')
