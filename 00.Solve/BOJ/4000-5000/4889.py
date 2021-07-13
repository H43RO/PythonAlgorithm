from sys import stdin

count = 1  # 케이스 번호 출력을 위한 count
while True:
    data = stdin.readline().strip()
    if data.startswith('-'):  # 종료 조건
        break
    '''
        필자의 기본 아이디어는, 안정적인 부분은 사전에 모두 없애고
        추후에 안정적이지 않은 문자열에 대해서만 한 번에 고려하는 것
    '''
    result = 0
    stack = []
    for x in data:  # 안정적인 문자열 (올바른 괄호 쌍) 은 애초에 모두 없애버리기
        if len(stack) > 0 and stack[-1] == '{' and x == '}':  # 쌍이 있는 괄호가 발견되면 없애줌
            stack.pop()
            continue
        stack.append(x)

    # stack 에는 안정적이지 않은 문자열만 남음
    while stack:  # 문자열이 항상 짝수라는 보장이 있기 때문에
        a = stack.pop()  # 두 개씩 팝해주면서
        b = stack.pop()  # 그 값을 비교해 봄
        if a == b:  # '{', '{' 혹은 '}', '}' 인 경우 1회 교체 필요
            result += 1
        else:  # '}', '{' 인 경우 2회 교체 필요
            result += 2

    print(f'{count}. {result}')
    count += 1
