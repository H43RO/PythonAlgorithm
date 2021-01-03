import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
result = [0] * m

data.sort()  # 이분탐색을 위한 정렬

def binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if data[mid] == target:
        return data[mid]
    if data[mid] > target:
        return binary_search(data, target, start, mid - 1)
    if data[mid] < target:
        return binary_search(data, target, mid + 1, end)

for i in range(m):
    if binary_search(data, card[i], 0, n - 1) != None:
        result[i] = 1

for x in result:
    print(x, end=" ")



