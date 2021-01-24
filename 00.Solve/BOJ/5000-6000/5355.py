from collections import deque

case = int(input())

for i in range(case):
    operator = deque(input().split())
    num = float(operator.popleft())

    for x in operator:
        if x == "@":
            num *= 3
        if x == "%":
            num += 5
        if x == "#":
            num -= 7

    print(format(num, ".2f"))