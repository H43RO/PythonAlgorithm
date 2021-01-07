from sys import stdin, stdout

n = int(stdin.readline())

result = 0

a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

a.sort()
b.sort(reverse=True)

for i in range(n):
    result += a[i] * b[i]

print(result)