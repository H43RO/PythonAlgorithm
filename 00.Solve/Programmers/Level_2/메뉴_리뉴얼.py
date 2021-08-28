from itertools import combinations
from collections import Counter, defaultdict


def solution(orders, course):
    answer = []
    config = defaultdict(list)  # 기본 Value 를 list 로 가짐

    for x in orders:
        a = sorted(list(x))
        for n in course:  # 메뉴 구성 수에 따른
            for combi in combinations(a, n):  # 메뉴 조합 저장
                config[n].append(combi)

    counters = []
    # 가장 함께 많이 주문된 메뉴 구성을 찾기 위한 카운터 사용
    [counters.append(Counter(v)) for v in config.values()]

    for x in counters:
        for a in x:  # 메뉴 조합이 Key, 주문 횟수가 Value 인 Dict
            # 최소 두 번 이상 주문됐으면서 가장 많이 주문된 조합
            # - most_common() 함수는 (원소, 등장횟수) 튜플을 내림차순으로 정렬해서 반환해줌
            # - 즉, most_common()[0][1] 는 가장 많이 등장한 횟수를 얻는 동작을 함
            if x[a] >= 2 and x[a] == x.most_common()[0][1]:
                answer.append(''.join(a))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
