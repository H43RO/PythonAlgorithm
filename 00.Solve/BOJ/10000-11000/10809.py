alpha = list("abcdefghijklmnopqrstuvwxyz")
result = [0] * len(alpha)

input = input()

for i in range(len(alpha)):
    if input.count(alpha[i]) == 0:
        result[i] = -1
    else:
        result[i] = input.index(alpha[i])

for num in result:
    print(num, end=' ')
