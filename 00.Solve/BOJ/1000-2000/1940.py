from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
data = sorted(list(map(int, stdin.readline().split())))

result = 0
left = 0
right = n - 1

while left < right:
    temp = data[left] + data[right]
    if temp == m:
        result += 1
    if temp < m:
        left += 1
        continue
    right -= 1

print(result)
