from sys import stdin, stdout

n = int(stdin.readline())

rope = []
power = []

for i in range(n):
    rope.append(int(stdin.readline()))

rope.sort(reverse=True)

for i, v in enumerate(rope):
    power.append(v * (i + 1))

print(max(power))
