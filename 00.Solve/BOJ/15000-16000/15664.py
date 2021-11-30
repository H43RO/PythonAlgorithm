from itertools import combinations

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

for x in list(combinations(data, m)):
    if x not in result:
        result.append(x)

for x in result:
    for num in x:
        print(num, end=' ')
    print()
