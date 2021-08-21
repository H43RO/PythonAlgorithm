def is_correct(data):
    # 올바른 괄호 문자열인지 검사
    stack = []
    for x in data:
        if x == '(':
            stack.append(x)
        if x == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
                continue

    return False if stack else True


def get_balance_index(data):
    # 균형잡힌 문자열 인덱스 구하기
    a, b = 0, 0
    for i in range(len(data)):
        if data[i] == '(':
            a += 1
        else:
            b += 1
        if a == b:
            return i


def solution(p):
    if not p:  # 만약 빈 문자열이면, 빈 문자열 반환
        return ''
    if is_correct(p):  #
        return p

    index = get_balance_index(p)
    u, v = p[:index + 1], p[index + 1:]

    if is_correct(u):
        return u + solution(v)

    # U 가 올바른 문자열이 아니라면
    temp = '(' + solution(v) + ')'
    for x in u[1:len(u) - 1]:
        if x == '(':
            temp += ')'
        else:
            temp += '('
    return temp


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
