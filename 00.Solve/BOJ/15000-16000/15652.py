from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
num.sort()

data = [0] * (m + 1)


def is_promising(data, i):
    for j in range(1, i + 1):
        if data[j] == data[i] and i != j:
            return False
    return True


def solve(data, count):
    if count > m:
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        for x in num:
            data[count] = x
            if is_promising(data, count):
                solve(data, count + 1)


solve(data, 1)
