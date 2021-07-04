from sys import stdin

n = int(stdin.readline())
people = list(reversed(list(map(int, stdin.readline().split()))))
data = []
for i, v in enumerate(people):
    data.insert(v, n - i)
print(' '.join(str(x) for x in data))
