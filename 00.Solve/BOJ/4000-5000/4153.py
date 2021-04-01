from sys import stdin

while True:
    data = sorted(list(map(int, stdin.readline().split())))
    if sum(data) == 0:
        break
    a, b, c = data[0], data[1], data[2]
    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')
