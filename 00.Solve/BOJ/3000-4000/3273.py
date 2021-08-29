from sys import stdin

n = int(stdin.readline())
data = sorted(list(map(int, stdin.readline().split())))
x = int(stdin.readline())

result = 0

left = 0   # 왼쪽 수
right = n - 1  # 오른쪽 수

while left < right:
    temp = data[left] + data[right]
    if temp == x:
        result += 1
    if temp < x:
        left += 1
        continue
    right -= 1

print(result)
