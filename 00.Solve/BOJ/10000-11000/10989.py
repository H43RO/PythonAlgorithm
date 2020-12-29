# 10,000 보다 작거나 같은 자연수라고 범위를 지정해주었으므로 메모리 제한 속에서 계수 정렬로 해결 가능

import sys

n = int(input())
count = [0] * (10001)

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for x in range(len(count)):
    for i in range(count[x]):
        sys.stdout.write(str(x) + '\n')



