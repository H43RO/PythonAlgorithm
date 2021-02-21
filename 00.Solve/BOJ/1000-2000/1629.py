a, b, c = map(int, input().split())

form = []
while True:
    if b == 1:
        break
    if b % 2 == 0:
        form.append(False)
    else:
        form.append(True)

    b = b // 2

d = a % c
result = d

for x in form[::-1]:
    if x:
        result = result ** 2 * d
    else:
        result = result ** 2

    result = result % c


print(result)
