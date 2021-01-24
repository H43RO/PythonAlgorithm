from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))

result = []
end = 0
temp_sum = 0

for start in range(n):
    while temp_sum < s and end < n:
        temp_sum += num[end]
        end += 1
    if temp_sum >= s:
        result.append(end - start)
    temp_sum -= num[start]

if result:
    print(min(result))
else:
    print(0)
