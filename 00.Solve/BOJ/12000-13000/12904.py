from sys import stdin

s = list(stdin.readline().strip())
t = list(stdin.readline().strip())

while len(t) >= len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        print(1)
        exit()
print(0)
