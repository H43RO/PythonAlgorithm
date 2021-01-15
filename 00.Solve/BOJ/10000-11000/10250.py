from sys import stdin, stdout


def solve(h, w, n):
    floor = n % h
    room = (n // h) + 1

    if floor == 0:
        floor = h

    if n % h == 0:
        room -= 1

    if room >= 10:
        result = "".join(str(floor) + str(room))
    else:
        result = "".join(str(floor) + "0" + str(room))

    return result


T = int(stdin.readline())

for i in range(T):
    h, w, n = map(int, stdin.readline().split())
    print(solve(h, w, n))
