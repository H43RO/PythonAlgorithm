from sys import stdin

N, S, R = map(int, stdin.readline().split())
damaged = list(map(int, stdin.readline().split()))
left = list(map(int, stdin.readline().split()))

for x in left:
    if x in damaged:
        del damaged[damaged.index(x)]
        continue
    if x - 1 in damaged:
        del damaged[damaged.index(x - 1)]
        continue
    if x + 1 in damaged:
        del damaged[damaged.index(x + 1)]
        continue

print(len(damaged))
