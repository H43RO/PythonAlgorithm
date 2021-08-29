from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
data = sorted(a + b)
for x in data:
    print(x, end=' ')