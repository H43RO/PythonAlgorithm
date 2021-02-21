from bisect import bisect_left
from sys import stdin, stdout

LIS = []

n = int(stdin.readline().strip())
num = list(map(int, input().split()))

for i, v in enumerate(num):
    if i == 0:
        LIS.append(v)
    else:
        if LIS[len(LIS) - 1] < v:
            LIS.append(v)
        else:
            LIS[bisect_left(LIS, v)] = v

print(len(LIS))
for x in LIS:
    print(x, end=' ')
print()
