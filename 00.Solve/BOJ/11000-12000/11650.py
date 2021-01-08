from sys import stdin, stdout

n = int(stdin.readline())

data = []

for i in range(n):
    data.append(list(map(int, stdin.readline().split())))

data.sort()

for x in data:
    print(f"{x[0]} {x[1]}")