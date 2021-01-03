n = int(input())

result = []
for i in range(n):
    a, b = map(int, input().split(','))
    result.append(a+b)


for x in result:
    print(x)