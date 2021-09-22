from sys import stdin


def count(distance):
    count = 1
    current = house[0]
    for i in range(1, n):
        if current + distance <= house[i]:
            count += 1
            current = house[i]
    return count


n, c = map(int, stdin.readline().split())
house = sorted([int(stdin.readline()) for _ in range(n)])

start, end = 1, house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    if count(mid) >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
