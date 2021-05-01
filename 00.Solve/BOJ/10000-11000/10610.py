from itertools import permutations

# 배수 판정법 이용
n = list(input())
n.sort(reverse=True)

if '0' not in n or int(''.join(n)) % 3 != 0:
    print(-1)
else:
    print(int(''.join(n)))