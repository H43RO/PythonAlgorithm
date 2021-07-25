from sys import stdin

n = int(stdin.readline())
data = sorted([int(stdin.readline()) for _ in range(n)])
print(sum([abs(i - data[i - 1]) for i in range(1, n + 1)]))