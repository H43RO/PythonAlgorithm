from sys import stdin

n, m, b = map(int, stdin.readline().split())

height = dict()
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for x in temp:
        if x not in height:
            height[x] = 1
        else:
            height[x] += 1

key = list(height.keys())

min_value = min(key)
max_value = max(key)

min_count = int(1e9)
highest = 0

for x in range(min_value, max_value + 1):
    count, have = 0, b
    for y in height.keys():
        if x > y:
            count += (x - y) * height[y]
            have -= (x - y) * height[y]
        elif x < y:
            count += 2 * (y - x) * height[y]
            have += (y - x) * height[y]

    if have >= 0:
        min_count = min(min_count, count)
        if min_count == count:
            highest = x

print(min_count, highest)
