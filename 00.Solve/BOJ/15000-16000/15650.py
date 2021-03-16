from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

data = [0] * (m + 1)


def is_promising(data, i):
    for j in range(1, i + 1):
        if data[j] == data[i] and i != j or data[j - 1] > data[j]:
            return False
    return True


def solve(data, count):
    if count > m:
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        for i in range(1, n + 1):
            data[count] = i
            if is_promising(data, count):
                solve(data, count + 1)


solve(data, 1)






