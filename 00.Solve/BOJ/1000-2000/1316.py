n = int(input())

list = []

result = 0

for x in range(n):
    list.append(input())

alpha = []

for word in list:
    for i, v in enumerate(word):
        alpha.append(v)
        if 1 <= i and word[i - 1] != word[i] and alpha.count(word[i]) >= 2:
            break
        if i == len(word) - 1:
            result += 1
    alpha.clear()

print(result)
