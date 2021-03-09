def solution(s):
    stack = []

    for x in s:
        if x == '(':
            stack.append(x)
        if x == ')':
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True


print(solution("(())()"))