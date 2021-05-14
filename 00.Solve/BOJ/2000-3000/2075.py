import heapq

n = int(input())
q = list(map(int, input().split()))
heapq.heapify(q)

for _ in range(1, n):
    temp = list(map(int, input().split()))
    # 최소힙 최상단 원소보다 큰 값이 들어오면 최상단 원소를 제거하고 새로운 값을 넣는 방식으로
    # 힙의 사이즈 N 을 유지하고, 루프가 끝나면 자연스럽게 최상단 원소가 N번째로 큰 값임
    for x in temp:
        if x > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, x)

print(q[0])
