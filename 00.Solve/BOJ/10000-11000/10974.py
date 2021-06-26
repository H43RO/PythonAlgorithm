from sys import stdin
from itertools import permutations

n = int(stdin.readline())
data = list(range(1, n + 1))
result = sorted(list(permutations(data, n)))
for x in result:
    print(' '.join(str(a) for a in x))
