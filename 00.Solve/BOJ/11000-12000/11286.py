from sys import stdin
import heapq

n = int(stdin.readline())
q = []

for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        # 비어있지 않으면 절댓값 가장 작은 값 출력
        if len(q) != 0:
            print(heapq.heappop(q)[1])
            continue
        # 비어있으면 0 출력
        print(0)
    else:
        # 절댓값, 원래 값 튜플로 저장
        heapq.heappush(q, (abs(x), x))
