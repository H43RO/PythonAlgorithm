from sys import stdin, stdout
import string

# 단지 인덱싱을 위한 알파벳 리스트
alpha = list(string.ascii_uppercase)

value = [['A', 0], ['B', 0], ['C', 0], ['D', 0],
         ['E', 0], ['F', 0], ['G', 0], ['H', 0],
         ['I', 0], ['J', 0], ['K', 0], ['L', 0],
         ['M', 0], ['N', 0], ['O', 0], ['P', 0],
         ['Q', 0], ['R', 0], ['S', 0], ['T', 0],
         ['U', 0], ['V', 0], ['W', 0], ['X', 0],
         ['Y', 0], ['Z', 0]]

n = int(stdin.readline())

words = []
nums = []

# 단어 저장
for i in range(n):
    word = stdin.readline().strip()
    words.append(word)

    for i in range(len(word)):
        value[alpha.index(word[i])][1] += pow(10, len(word) - 1 - i)

value.sort(reverse=True, key=lambda x: x[1])

# 중요도 값 부여
priority = 9
for x in value:
    x[1] = priority

    if priority == 0:
        break

    priority -= 1

# 간편한 인덱싱을 위해 다시 알파벳 순으로 정렬
value.sort()

# 각 알파벳을 숫자로 치환 후 저장
for word in words:
    for x in word:
        word = word.replace(x, str(value[alpha.index(x)][1]))
    nums.append(int(word))

# 합 출력
print(sum(nums))
