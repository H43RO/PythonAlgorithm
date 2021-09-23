import sys
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
member = [i for i in range(n)]
score = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = sys.maxsize
# 전체 인원의 절반까지 조합 조사 -> 반/반으로 나누는 상황까지 고려
for i in range(1, int((n / 2) + 1)):
    team = combinations(member, i)  # i 명 끼리 팀 꾸리는 조합
    temp = sys.maxsize

    for x in team:  # i 명 끼리 팀 꾸리는 조합 하나하나 탐색
        start = list(x)  # i 명 팀을 스타트 팀으로
        link = list(set(member) - set(start))  # 나머지 인원을 모두 링크 팀으로

        start_ability = 0
        link_ability = 0

        # 팀 내의 모든 쌍에 대해 능력치 조사 (항상 2명씩 짝지음)
        for x in combinations(start, 2):
            start_ability += score[x[0]][x[1]]
            start_ability += score[x[1]][x[0]]
        for x in combinations(link, 2):
            link_ability += score[x[0]][x[1]]
            link_ability += score[x[1]][x[0]]

        # 스타트 팀이랑 링크 팀 능력치 차이 최소화
        temp = min(temp, abs(start_ability - link_ability))
    result = min(result, temp)

print(result)
