from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = list(stdin.readline().strip())

pattern = 0
count = 0

i = 1
while i < m - 1:
    if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
        pattern += 1
        if pattern == n:
            pattern -= 1
            count += 1
        i += 2
    else:
        pattern = 0
        i += 1

print(count)
