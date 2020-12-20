result = sum([1, 2, 3, 4, 5])
print(result)

min = min(7, 3, 5, 2)
max = max(7, 3, 5, 2)
print(min, max)

result = eval("(3+5)*7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

array = [('홍길동', 35), ('이순신', 70), ('김현준', 60)]
print(sorted(array, key=lambda x : x[1], reverse=True))

from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

from itertools import combinations
data = ['A', 'B', 'C']

result = list(combinations(data, 2))  # 2 개 뽑는 모든 조합 구하기
print(result)

from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2))  # 중복 순열
print(result)

from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))  # 중복 조합
print(result)

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # blue 등장 횟수
print(counter['green'])  # green 등장 횟수
print(counter['red'])  # red 등장 횟수
print()

import math

# 최소 공배수 (LCM) 를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14
print(math.gcd(a, b))  # 최대 공약수
print(lcm(a, b))  # 최소 공배수

print(math.pi)