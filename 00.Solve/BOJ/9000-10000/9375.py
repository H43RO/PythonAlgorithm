from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    clothes = {}
    n = int(stdin.readline())
    for i in range(n):
        name, spices = stdin.readline().split()
        if spices in clothes:
            clothes[spices] += 1
        else:
            clothes[spices] = 1
    result = 1
    for x in clothes.values():
        result *= (x + 1)
    print(result - 1)
