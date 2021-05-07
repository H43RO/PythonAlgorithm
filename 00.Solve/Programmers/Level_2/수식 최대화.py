from itertools import permutations

def solution(expression):
    numbers = []
    operators = []

    number_string = ''
    for i, v in enumerate(expression):
        if v == '*' or v == '-' or v == '+':
            operators.append(v)
            continue
        else:
            number_string += v
            if i < len(expression) - 1 and not expression[i + 1].isnumeric():
                numbers.append(int(number_string))
                number_string = ''
            elif i == len(expression) - 1:
                numbers.append(int(number_string))
                number_string = ''

    op_set = set(operators)
    priority = permutations(op_set)

    result = []

    for exp in priority:
        # copy() 없이 아래 로직을 수행하게 되면 깊은 참조가 이루어져 원본 리스트까지 바뀌어 버림
        # 이 때문에 자꾸 정답이 나오지 않다가, copy() 를 붙여 해결하였음
        num = numbers.copy()
        op = operators.copy()

        for x in exp:
            while x in op:
                i = op.index(x)
                op.remove(x)
                num = num[:i] + [int(eval(str(num[i]) + x + str(num[i + 1])))] + num[i + 2:]
        result.append(abs(num[0]))
    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
