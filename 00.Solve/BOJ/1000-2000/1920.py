import sys

n = sys.stdin.readline()
N = sorted(list(map(int, sys.stdin.readline().split())))

m = sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    # 만약 mid 값이 target 값이면 return 1
    if array[mid] == target:
        return 1
    # 만약 mid 값이 target 값보다 크다면 왼쪽 부분 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 만약 mid 값이 target 값보다 작다면 오른쪽 부분 탐색
    else:
        return binary_search(array, target, mid + 1, end)


for x in M:
    start = 0
    end = len(N) - 1
    print(binary_search(array=N, target=x, start=start, end=end))

