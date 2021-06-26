from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
num.sort()

data = [0] * (m + 1)


def solve(data, count):
    if count > m:
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        for x in num:
            data[count] = x
            solve(data, count + 1)


solve(data, 1)
