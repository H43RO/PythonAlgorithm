from sys import stdin, stdout
from itertools import combinations

N, S = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

count = 0

for i in range(1, N + 1):
    result = list(combinations(data, i))
    for x in result:
        if sum(x) == S:
            count += 1

print(count)
