from sys import stdin, stdout

n = int(stdin.readline())

data = []

for i in range(n):
    temp = [0] * 2
    temp[1], temp[0] = map(int, stdin.readline().split())
    data.append(temp)

data.sort()

for x in data:
    print(f"{x[1]} {x[0]}")