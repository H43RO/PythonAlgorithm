from itertools import permutations
from sys import stdin

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(stdin.readline())
sign = list(stdin.readline().split())

result = []

# 입력 범위가 크지않아, 가능한 모든 경우의 순열 리스트 생성
for x in list(permutations(num, k + 1)):
    available = True
    for i in range(k):
        # 부등호 순서대로 조건에 부합하는지 검사
        if sign[i] == '>' and x[i] > x[i + 1]:
            continue
        if sign[i] == '<' and x[i] < x[i + 1]:
            continue

        # 조건을 만족 못하는 경우 플래그 변수 False 로 변경 후 종료
        available = False
        break

    # 만약 조건에 부합하는 숫자인 경우 결과 목록에 문자열로 변환하여 저장
    if available:
        result.append(''.join(map(str, x)))

# Python 의 문자열 크기 비교 기준은 사전 순으로 정의되기 때문에
# 첫 자리가 0인 경우 또한 가장 작은 값으로 취급할 수 있음
print(max(result))
print(min(result))
