from sys import stdin, stdout

n = int(stdin.readline())
distance = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))

min_price = price[0]
result = 0

for i in range(n - 1):
    if i == 0:
        result += distance[0] * price[0]
    elif min_price > price[i]:
        min_price = price[i]
        result += distance[i] * price[i]
    else:
        result += distance[i] * min_price

print(result)
