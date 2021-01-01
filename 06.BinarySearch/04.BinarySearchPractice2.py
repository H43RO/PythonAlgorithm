from bisect import bisect_left, bisect_right

# 평범한 특정 수의 개수를 구하는 프로그램이지만,
# 정렬된 배열이라는 특별한 조건이 있으므로
# 특정 수의 가장 오른쪽 인덱스에서 왼쪽 인덱스를 뺀 값이 그 수의 개수이다


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
data = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면 개수 출력
else:
    print(count)


# 평범한 이분 탐색 풀이
# start = 0
# end = n - 1
#
# result = 0
#
# def binary_search(data, x, start, end):
#     global result
#
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#
#     if data[mid] == x:
#         result += 1
#
#     binary_search(data, x, start, mid - 1)
#     binary_search(data, x, mid + 1, end)
#
#
# binary_search(data, x, start, end)
#
# print(result)