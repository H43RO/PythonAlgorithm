from sys import stdin, stdout
import heapq

# 중앙값 기준으로 큰 값은 오른쪽, 작은 값은 왼쪽에 저장
# 왼쪽 값은 max_heap, 오른쪽은 min_heap (중앙값은 항상 max_heap 최상위 원소)

# 1. 왼쪽과 오른쪽 힙의 길이가 같다면, 무조건 왼쪽에 새 값 저장
# 2. 만약 오른쪽 힙의 값보다 왼쪽 힙의 값이 더 크면 오른쪽과 왼쪽 원소값 스왑
left, right = [], []
n = int(stdin.readline())

for i in range(n):
    num = int(stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_val = heapq.heappop(left)[1]
        right_val = heapq.heappop(right)[1]
        heapq.heappush(right, (left_val, left_val))
        heapq.heappush(left, (-right_val, right_val))

    print(left[0][1])