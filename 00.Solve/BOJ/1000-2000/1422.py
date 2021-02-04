from sys import stdin, stdout
from functools import cmp_to_key

k, n = map(int, stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(k)]

best = max(nums)
for i in range(n - k):
    nums.append(best)

# b + a 한 값보다 a + b 한 값이 더 크면 a 를 앞으로 하고 b 를 뒤로 (아닌 경우 반대로)
nums = sorted(nums, key=cmp_to_key(lambda a, b: -1 if int(str(a) + str(b)) > int(str(b) + str(a)) else 1))

print(*nums, sep='')
