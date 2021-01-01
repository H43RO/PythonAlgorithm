import sys

n = sys.stdin.readline()
N = sorted(list(map(int, sys.stdin.readline().split())))

m = sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)  # 왼쪽 부분을 탐색
    else:
        return binary_search(array, target, mid + 1, end)  # 오른쪽 부분을 탐색


for x in M:
    start = 0
    end = len(N) - 1
    print(binary_search(array=N, target=x, start=start, end=end))

