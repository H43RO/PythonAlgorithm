from sys import stdin

n = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))

result = 1

for x in sorted(weight):
    if result >= x:
        result += x

print(result)
