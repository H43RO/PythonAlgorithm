from sys import stdin

a, p = map(int, stdin.readline().split())
sequence = [a]

while True:
    num = str(sequence[-1])
    temp = 0
    for x in num:
        temp += int(x) ** p
    if temp in sequence:
        print(sequence.index(temp))
        break
    sequence.append(temp)
