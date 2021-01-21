from sys import stdin, stdout

i = 1

while True:
    result = 0
    L, P, V = map(int, stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    while V > 0:
        if V < L:
            result += V
        else:
            result += L
        V -= P

    print(f"Case {i}: {result}")
    i += 1
