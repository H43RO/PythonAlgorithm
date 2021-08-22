from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    config = {}

    for x in orders:
        a = sorted(list(x))
        for n in course:
            for i in combinations(a, n):
                if n not in config:
                    config[n] = [i]
                else:
                    config[n].append(i)

    counters = []
    for x in config.keys():
        counters.append(Counter(config[x]))

    for x in counters:
        for a in x:
            if x[a] >= 2 and x[a] == x.most_common()[0][1]:
                answer.append(''.join(a))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
