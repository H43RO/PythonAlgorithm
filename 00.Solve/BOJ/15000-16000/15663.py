from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)

result = []

for numbers in list(permutations(data, m)):
    result.append(numbers)
result = sorted(list(set(result)))

for x in result:
    for num in x:
        print(num, end=' ')
    print()
