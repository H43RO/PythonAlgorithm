from sys import stdin

n, m = map(int, stdin.readline().split())
times = [int(stdin.readline()) for _ in range(n)]

start = 1
end = times[-1] * m

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for x in times:
        temp += mid // x

    if temp >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
