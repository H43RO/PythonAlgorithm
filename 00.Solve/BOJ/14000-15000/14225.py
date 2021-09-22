from itertools import combinations
from sys import stdin

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))

sum_data = set()
for i in range(1, n + 1):
    for x in list(combinations(s, i)):
        sum_data.add(sum(x))

for i in range(1, sum(s) + 2):
    if i not in sum_data:
        print(i)
        exit(0)
