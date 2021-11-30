from sys import stdin, stdout
from itertools import combinations

n, S = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

count = 0

for i in range(1, n + 1):
    # 1 개 부터 N 개 까지의 모든 조합 (부분 수열) 에 대하여 합을 검사
    result = list(combinations(data, i))
    for x in result:
        if sum(x) == S:
            count += 1

print(count)
