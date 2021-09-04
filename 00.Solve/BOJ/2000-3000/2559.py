from sys import stdin

n, k = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

cum = sum(data[:k])
result = cum

for i in range(len(data) - k):
    cum = cum - data[i] + data[i + k]
    result = max(result, cum)

print(result)
