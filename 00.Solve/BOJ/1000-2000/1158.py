from sys import stdin, stdout
from collections import deque

queue = deque()

n, k = map(int, stdin.readline().split())

for i in range(1, n + 1):
    queue.append(i)

index = 0
result = []

while queue:
    if index == 0:
        index += 1
        continue

    if index % k == 0:
        result.append(queue.popleft())
        index += 1
        continue

    queue.append(queue.popleft())
    index += 1

result = "".join(str(result))
result = list(result)
result[0] = "<"
result[-1] = ">"
result = "".join(result)
print(result)
