from sys import stdin

n, k = map(int, stdin.readline().split())
kinder = list(map(int, stdin.readline().split()))
result = []
for i in range(1, n):
    result.append(kinder[i] - kinder[i - 1])
result.sort()
print(sum(result[:n - k]))
