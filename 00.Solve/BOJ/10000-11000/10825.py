from sys import stdin

n = int(stdin.readline())
data = []

for _ in range(n):
    data.append(list(stdin.readline().split()))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in data:
    print(x[0])
