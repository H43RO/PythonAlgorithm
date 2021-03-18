from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

data = [0] * (m + 1)


def solve(data, count):
    if count > m:
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        for i in range(1, n + 1):
            data[count] = i
            solve(data, count + 1)


solve(data, 1)






