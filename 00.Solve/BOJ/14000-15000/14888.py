import copy
from itertools import permutations
from sys import stdin, maxsize

operator = []
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
count = list(map(int, stdin.readline().split()))
for i in range(4):  # 연산자 각각 등장 횟수만큼 추가
    for j in range(count[i]):
        operator.append(i)
operator = list(set(list(permutations(operator, len(operator)))))

max_result = -maxsize - 1
min_result = maxsize
for x in operator:
    temp = 0
    for i, v in enumerate(num):
        if i == 0:
            temp += v
            continue
        if x[i - 1] == 0:
            temp += v
        if x[i - 1] == 1:
            temp -= v
        if x[i - 1] == 2:
            temp *= v
        if x[i - 1] == 3:
            temp = int(temp / v)
    max_result = max(max_result, temp)
    min_result = min(min_result, temp)

print(max_result)
print(min_result)
