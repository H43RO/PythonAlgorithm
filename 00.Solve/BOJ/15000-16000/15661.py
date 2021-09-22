import sys
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
member = [i for i in range(n)]
score = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = sys.maxsize
for i in range(1, int((n / 2) + 1)):
    team = combinations(member, i)
    temp = sys.maxsize

    for x in team:
        start = list(x)
        link = list(set(member) - set(start))

        start_ability = 0
        link_ability = 0

        for x in combinations(start, 2):
            start_ability += score[x[0]][x[1]]
            start_ability += score[x[1]][x[0]]
        for x in combinations(link, 2):
            link_ability += score[x[0]][x[1]]
            link_ability += score[x[1]][x[0]]

        temp = min(temp, abs(start_ability - link_ability))
    result = min(result, temp)

print(result)
