import math
from sys import stdin

n, m = map(int, stdin.readline().split())
jewel = [int(stdin.readline()) for _ in range(m)]

start = 1
end = max(jewel)

result = 0

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for x in jewel:
        temp += math.ceil(x / mid)

    if temp > n:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
