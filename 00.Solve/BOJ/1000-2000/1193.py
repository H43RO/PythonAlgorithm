X = int(input())

n = 1

while X > n:
    X -= n
    n += 1

if n % 2 == 0:
    a = X
    b = n - X + 1
else:
    a = n - X + 1
    b = X

print(a, '/', b, sep='')