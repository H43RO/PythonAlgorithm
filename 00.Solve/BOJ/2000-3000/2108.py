# 반올림 실수로 틀렸다가, round() 를 사용하여 정답 판정

from collections import Counter
import sys

n = int(input())

list = []

for i in range(n):
    num = int(sys.stdin.readline())
    list.append(num)

list.sort()

cnt = Counter(list)
order = cnt.most_common()
maximum = order[0][1]

modes = []
for num in order:
    if num[1] == maximum:
        modes.append((num[0]))

modes.sort()

avg = round(sum(list) / n)
mid = list[n//2]
scope = abs(max(list) - min(list))

print(avg)
print(mid)

if len(modes) >= 2:
    print(modes[1])
else:
    print(modes[0])

print(scope)
