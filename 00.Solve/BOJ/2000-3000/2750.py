# sys 모듈을 활용하여 입출력을 해야 시간 초과가 나지않음

import sys

n = int(input())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

for x in sorted(list):
    sys.stdout.write(str(x)+'\n')