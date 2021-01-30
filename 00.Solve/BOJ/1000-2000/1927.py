from sys import stdin, stdout
from queue import PriorityQueue

# 내부적으로 Heapq 모듈로 구현된 PriorityQueue 모듈
queue = PriorityQueue()

n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        # 우선순위 큐가 비어있지 않으면 최솟값 출력 (비어있으면 0 출력)
        if not queue.empty():
            print(queue.get())
        else:
            print(0)
    else:
        # 우선순위 큐에 입력된 값을 삽입
        queue.put(x)
