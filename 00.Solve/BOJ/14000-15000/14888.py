from itertools import permutations
from sys import stdin, maxsize

operator = []
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))  # 숫자 목록
count = list(map(int, stdin.readline().split()))  # 각 연산자 등장 횟수
for i in range(4):  # 연산자 각각 등장 횟수만큼 연산자 셋에 추가
    for j in range(count[i]):
        operator.append(i)

max_result = -maxsize - 1  # 갱신형 최댓값 변수
min_result = maxsize  # 갱신형 최솟값 변수

for x in list(set(permutations(operator, len(operator)))):  # 모든 경우의 수 (연산자 순서) 에 대하여
    temp = 0
    for i, v in enumerate(num):
        if i == 0 or x[i - 1] == 0:  # 0 이면 덧셈
            temp += v
            continue  # i == 0 일 때 x[-1] 연산에 의해 아래 분기를 탈 수도 있음
        if x[i - 1] == 1:  # 1 이면 뺄셈
            temp -= v
        if x[i - 1] == 2:  # 2 이면 곱셈
            temp *= v
        if x[i - 1] == 3:  # 3 이면 나눗셈
            temp = int(temp / v)  # 파이썬은 이런식으로 C++14 표준 정수 나눗셈 가능

    max_result = max(max_result, temp)  # 최댓값 갱신
    min_result = min(min_result, temp)  # 최솟값 갱신

print(max_result)
print(min_result)
