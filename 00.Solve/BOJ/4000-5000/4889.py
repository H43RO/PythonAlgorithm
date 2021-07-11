from sys import stdin

count = 1  # 1-based 인덱싱
while True:
    data = stdin.readline().strip()
    if data.startswith('-'):  # 종료 조건
        break
    result = 0
    stack = []
    for x in data:
        if len(stack) > 0 and stack[-1] == '{' and x == '}':  # 쌍이 있는 괄호가 발견되면 없애줌
            stack.pop()
            continue
        stack.append(x)

    while stack:  # 문자열이 항상 짝수라는 보장이 있기 때문에
        a = stack.pop()  # 두 개씩 팝해주면서
        b = stack.pop()  # 그 값을 비교
        if a == b:  # '{', '{' 혹은 '}', '}' 인 경우 1회 교체 필요
            result += 1
        else:  # '}', '{' 인 경우 2회 교체 필요
            result += 2

    print(f'{count}. {result}')
    count += 1
