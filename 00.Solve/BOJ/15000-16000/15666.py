from itertools import combinations_with_replacement
from sys import stdin

n, m = map(int, stdin.readline().split())
data = sorted(list(map(int, stdin.readline().split())))
result = sorted(list(set(list(combinations_with_replacement(data, m)))))
for x in result:
    print(' '.join(str(a) for a in x))
