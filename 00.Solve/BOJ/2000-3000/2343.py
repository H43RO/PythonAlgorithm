from sys import stdin

n, m = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

start = max(data)
end = sum(data)
result = end

while start <= end:
    mid = (start + end) // 2

    if mid < max(data):
        end = mid + 1
        continue

    count = 0
    temp = 0
    for x in data:
        if x > mid:
            break
        if temp + x > mid:
            count += 1
            temp = x
        else:
            temp += x

    if count <= m - 1:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1

print(result)
