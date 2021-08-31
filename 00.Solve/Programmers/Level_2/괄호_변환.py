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
        if a == b:  # 두 괄호의 개수가 같은 최초 순간
            return i


def solution(p):
    if not p:  # 만약 빈 문자열이면, 빈 문자열 반환
        return ''
    if is_correct(p):  # 올바른 괄호 문자열이면 그대로 반환
        return p

    index = get_balance_index(p)
    u, v = p[:index + 1], p[index + 1:]  # 균형잡힌 문자열 기점으로 분할

    if is_correct(u):  # u 가 올바른 괄호 문자열이면 v 에 대해서 재귀 수행
        return u + solution(v)

    # U 가 올바른 문자열이 아니라면
    temp = '(' + solution(v) + ')'
    for x in u[1:len(u) - 1]:  # 괄호 방향 뒤집기
        temp += ')' if x == '(' else '('
    return temp


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

# 2020 카카오 블라인드 공채 2번
# 정답률 23.1%
# - 23분 소요
