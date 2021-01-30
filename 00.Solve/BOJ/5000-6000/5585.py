n = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]
result = 0

for x in coin:
    if n > 0:
        result += (n // x)
        n = n % x

print(result)
