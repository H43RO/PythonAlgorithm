from sys import stdin, stdout
import heapq

n = int(stdin.readline().strip())
max_heap = []

for _ in range(n):
    operation = int(stdin.readline().strip())

    if operation == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -operation)
