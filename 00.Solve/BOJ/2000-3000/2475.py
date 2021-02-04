num = list(map(int, input().split()))
result = []
for x in num:
    result.append(x ** 2)

print(sum(result) % 10)
