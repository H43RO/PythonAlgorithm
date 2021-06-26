from itertools import permutations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)

result = []

for numbers in list(permutations(data, M)):
    result.append(numbers)
result = sorted(list(set(result)))

for x in result:
    for num in x:
        print(num, end=' ')
    print()
