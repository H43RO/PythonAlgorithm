from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

not_heard = []
not_seen = []

for i in range(n + m):
    if i < n:
        not_heard.append(stdin.readline().strip())
    else:
        not_seen.append(stdin.readline().strip())

not_heard_seen = list(set(not_heard) & set(not_seen))
print(len(not_heard_seen))

for x in sorted(not_heard_seen):
    print(x)