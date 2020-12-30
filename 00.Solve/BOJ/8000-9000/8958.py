n = int(input())
data = []
result = [0] * n

for i in range(n):
    data.append(input())

score = 0

for i in range(len(data)):
    for v in data[i]:
        if v == 'O':
            score += 1
            result[i] += score

        if v == 'X':
            score = 0
    score = 0


for x in result:
    print(x)
