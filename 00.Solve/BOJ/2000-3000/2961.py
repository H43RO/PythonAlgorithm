import sys
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
material = []

for i in range(n):
    sour, bitter = map(int, stdin.readline().split())
    material.append((sour, bitter))

result = sys.maxsize
for i in range(1, n + 1):
    for x in combinations(material, i):
        sour = 1
        bitter = 0
        for a in x:
            sour *= a[0]
            bitter += a[1]
        result = min(result, abs(sour - bitter))

print(result)
