from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

data = list(permutations(num, n))
result = []

for x in data:
    temp = 0
    for i in range(n - 1):
        temp += abs(x[i] - x[i + 1])
    result.append(temp)

print(max(result))