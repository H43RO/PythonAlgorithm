from sys import stdin, stdout
import heapq

case = int(stdin.readline())

for _ in range(case):
    n = int(stdin.readline())
    if n <= 10:
        num = list(map(int, stdin.readline().split()))
    else:
        num = []
        while len(num) != n:
            num = num + list(map(int, stdin.readline().split()))

    left = []
    right = []
    mid = []
    count = 0

    for i, x in enumerate(num):
        if len(left) == len(right):
            heapq.heappush(left, (-x, x))
        else:
            heapq.heappush(right, (x, x))

        if right and left[0][1] > right[0][1]:
            left_val = heapq.heappop(left)[1]
            right_val = heapq.heappop(right)[1]
            heapq.heappush(right, (left_val, left_val))
            heapq.heappush(left, (-right_val, right_val))

        if (i + 1) % 2 == 1:
            mid.append(left[0][1])

    print(len(mid))

    for i, x in enumerate(mid):
        print(x, end=' ')
        count += 1

        if count == 10 and i != len(mid) - 1:
            print()
            count = 0
    print()
