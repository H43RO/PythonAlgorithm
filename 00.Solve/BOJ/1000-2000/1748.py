from sys import stdin

n = int(stdin.readline())

result = 0
while n > 10:
    length = len(str(n))
    threshold = 10 ** (length - 1)
    result += (n - threshold + 1) * length
    n -= (n - threshold + 1)

print(result + n)
