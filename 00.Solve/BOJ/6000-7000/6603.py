from sys import stdin, stdout
from itertools import combinations


while True:
    case = list(map(int, stdin.readline().split()))

    if case[0] == 0:
        break

    data = case[1:]

    result = list(combinations(data, 6))  # 2 개 뽑는 모든 조합 구하기

    for x in result:
        for i in range(len(x)):
            if i == len(x) - 1:
                print(x[i])
            else:
                print(x[i], end=" ")

    print()