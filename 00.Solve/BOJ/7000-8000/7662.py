from sys import stdin, stdout
import heapq

case = int(stdin.readline().strip())

for _ in range(case):
    min_heap = []
    max_heap = []
    visited = [False] * 1_000_001
    k = int(stdin.readline().strip())
    for i in range(k):
        op, num = stdin.readline().split()
        num = int(num)
        # 최대 힙, 최소 힙에 입력값 삽입
        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        # 최대 힙에서 최댓값 제거
        elif op == 'D' and num == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        # 최소 힙에서 최솟값 제거
        elif op == 'D' and num == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
