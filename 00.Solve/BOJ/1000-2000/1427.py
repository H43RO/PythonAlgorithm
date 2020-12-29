import sys

num = list(input())

num = list(map(int, num))
num.sort(reverse=True)

for x in num:
    print(x, end='')
