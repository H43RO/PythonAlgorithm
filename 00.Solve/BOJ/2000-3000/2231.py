num = int(input())

result = 0

i = 0
while True:
    sum = i
    for x in str(i):
        sum += int(x)

    if sum == num:
        result = i
        break

    if i > num:
        break

    i += 1

print(result)
