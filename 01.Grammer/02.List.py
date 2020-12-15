a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[3])
print(a[-1])
print(a[-3])

a[3] = 10
print(a)

print(a[:3])
print(a[1:4])

# 크기가 N 이고, 모든 값이 0 인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
print()

# 리스트 컴프리헨션
# - 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화할 수 있음
array = [i for i in range(10)]  # 0 부터 9 까지 담기는 리스트 초기화
print(array)

a = [i for i in range(20)]
print(a)

a = [i for i in range(20) if i % 2 == 0]
print(a)

a = [i * i for i in range(1, 10)]
print(a)