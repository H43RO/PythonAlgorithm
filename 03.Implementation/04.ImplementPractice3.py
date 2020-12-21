string = list(input())

alpha = []
num = 0

for x in string:
    if x.isdigit():
        num += int(x)
    if x.isalpha():
        alpha.append(x)

alpha.sort()
alpha.append(str(num))

print(''.join(alpha))
