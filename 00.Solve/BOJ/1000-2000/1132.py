from sys import stdin, stdout
import string

# 1339번 단어 수학 문제와 다른 점 : 0 으로 시작하는 숫자는 없다

# 단지 인덱싱을 위한 알파벳 리스트
alpha = list(string.ascii_uppercase)

value = [['A', 0], ['B', 0], ['C', 0], ['D', 0],
         ['E', 0], ['F', 0], ['G', 0], ['H', 0],
         ['I', 0], ['J', 0]]

n = int(stdin.readline())

words = []
first = []
nums = []

# 단어 저장
for i in range(n):
    word = stdin.readline().strip()
    words.append(word)

    # 시작하는 알파벳 저장
    first.append(word[0])

    for i in range(len(word)):
        value[alpha.index(word[i])][1] += pow(10, len(word) - 1 - i)

value.sort(reverse=True, key=lambda x: x[1])

for i in range(9, -1, -1):
    if value[i][0] not in first:
        temp = value[i]
        value.remove(temp)
        value.append(temp)
        break

priority = 9
for x in value:
    x[1] = priority

    if priority == 0:
        break

    priority -= 1

value.sort()

# 각 알파벳을 숫자로 치환 후 저장
for word in words:
    for x in word:
        word = word.replace(x, str(value[alpha.index(x)][1]))
    nums.append(int(word))

# 합 출력
print(sum(nums))
