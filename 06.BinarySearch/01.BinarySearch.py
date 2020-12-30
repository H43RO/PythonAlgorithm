def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)  # 왼쪽 부분을 탐색
    else:
        return binary_search(array, target, mid + 1, end)  # 오른쪽 부분을 탐색


n, target = list(map(int, input().split()))
target = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)