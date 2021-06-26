from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)
result = []

for x in list(combinations(data, M)):
    if not result:
        result.append(x)
    elif x not in result:
        result.append(x)

for x in result:
    for num in x:
        print(num, end=' ')
    print()
