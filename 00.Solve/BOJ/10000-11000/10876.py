from sys import stdin, stdout

n = int(stdin.readline())

data = list(map(int, stdin.readline().split()))

temp = set(data)
data = list(temp)

data.sort()

for x in data:
    print(x, end=" ")