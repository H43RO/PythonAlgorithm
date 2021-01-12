d = [0] * 101

d[1] = 1
d[2] = 1
d[3] = 1

def wave(n):
    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2]

    return d[n]


for case in range(int(input())):
    n = int(input())

    print(wave(n))