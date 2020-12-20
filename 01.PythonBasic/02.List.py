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

# N X M 크기의 2차원 리스트를 초기화할 때 효과적
# ex) 4 X 3 크기의 2차원 리스트를 초기화
array = [[0] * 3 for _ in range(4)]
print(array)
print()

# append() : 원소 하나 삽입할 때
# sort() : 오름차순으로 정렬
# sort(reverse=True) : 내림차순으로 정렬
# reverse() : 리스트를 뒤집음
# insert(index, value) : index 에 value 를 삽입
# count(value) : value 가 리스트에 몇 개 있는지
# remove(value) : value 를 갖는 원소 제거, 해당 원소가 여러 개면 하나만 제거

a = [1, 4, 3]
print(a)

a.append(2)
print(a)

a.sort()
print(a)

a.reverse()
print(a)

print(a.count(3))

a.remove(1)
print(a)
print()

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)
print()


def solution(n, lost, reserve):
    answer = 0
    answer += (n - len(lost))

    for i in range(0, len(reserve)):
        if answer >= n:
            return answer

        if reserve[i] - 1 in lost or reserve[i] + 1 in lost:
            answer += 1

    return answer


print(solution(5, [2, 4], [3, 4]))
