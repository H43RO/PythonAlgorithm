from sys import stdin

m, n = map(int, stdin.readline().split())
snack = list(map(int, stdin.readline().split()))

start = 1
end = max(snack)

length = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for x in snack:
        count += (x // mid)
    if count >= m:
        length = mid
        start = mid + 1
    else:
        end = mid - 1


print(length)
