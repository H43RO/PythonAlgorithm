import heapq

n = int(input())
q = list(map(int, input().split()))
heapq.heapify(q)

for _ in range(1, n):
    temp = list(map(int, input().split()))
    for x in temp:
        if x > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, x)

print(q[0])
