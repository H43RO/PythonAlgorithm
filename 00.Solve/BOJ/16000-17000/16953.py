a, b = map(int, input().split())

count = 0

while b > a:
    count += 1
    if str(b).endswith('1'):
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        b = b // 2
    else:
        break

if b == a:
    print(count + 1)
else:
    print(-1)