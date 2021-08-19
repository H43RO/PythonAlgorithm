from sys import stdin

n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]

result = 0
for i in range(n - 2, -1, -1):
    if data[i + 1] <= data[i]:
        result += data[i] - data[i + 1] + 1
        data[i] -= data[i] - data[i + 1] + 1
print(result)
