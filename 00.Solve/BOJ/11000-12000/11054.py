from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
dp_1 = [1] * n

# LIS 계산
for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)

# LDS 계산
dp_2 = [1] * n
data.reverse()
for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)
dp_2.reverse()

result = []
for i in range(n):
    result.append(dp_1[i] + dp_2[i] - 1)

print(max(result))
