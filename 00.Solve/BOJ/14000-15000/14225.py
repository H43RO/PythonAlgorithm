from itertools import combinations
from sys import stdin

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))

sum_data = set()
for i in range(1, n + 1):  # 1개 ~ N개 까지의 모든 쌍의 조합을 탐색
    for x in list(combinations(s, i)):
        sum_data.add(sum(x))

for i in range(1, sum(s) + 2):  # 최악의 경우 모든 숫자들의 합 + 1 까지 갈 수 있음
    if i not in sum_data:  # 1부터 모든 숫자들의 합 + 1 까지 완전탐색
        print(i)
        exit(0)
