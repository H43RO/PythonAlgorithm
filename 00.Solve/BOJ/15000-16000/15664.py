from itertools import combinations

N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

for x in list(combinations(data, M)):
    if x not in result:
        result.append(x)

for x in result:
    for num in x:
        print(num, end=' ')
    print()
