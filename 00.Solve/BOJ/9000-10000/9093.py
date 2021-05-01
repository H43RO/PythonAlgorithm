n = int(input())

for _ in range(n):
    data = list(input().split())
    for x in data:
        print(''.join(reversed(x)), end=' ')