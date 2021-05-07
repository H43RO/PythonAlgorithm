from itertools import permutations
import re


def solution(expression):
    operators = set(re.findall("\D", expression))
    priority = permutations(operators)
    result = []

    for operator in priority:
        temp = re.compile("(\D)").split('' + expression)
        for exp in operator:
            while exp in temp:
                i = temp.index(exp)
                temp = temp[:i - 1] + [str(eval(''.join(temp[i - 1:i + 2])))] + temp[i + 2:]
        result.append(abs(int(temp[0])))
    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
