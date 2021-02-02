from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())

negative = []
positive = []

result = 0

for i in range(n):
    num = int(stdin.readline())
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

negative = deque(sorted(negative))
positive = deque(sorted(positive, reverse=True))

deque_list = [negative, positive]

for x in deque_list:
    while x:
        if len(x) == 1:
            result += x.popleft()
            break

        if x[0] + x[1] <= x[0] * x[1]:
            a = x.popleft()
            b = x.popleft()
            result += a * b
        else:
            a = x.popleft()
            b = x.popleft()
            result += a + b

print(result)
