from sys import stdin, stdout

S = []

m = int(stdin.readline().strip())

for _ in range(m):
    command = list(stdin.readline().split())

    if len(command) == 2:
        op, num = command[0], int(command[1])
        if op == "add":
            if num in S:
                pass
            else:
                S.append(num)
        elif op == "remove":
            if num in S:
                S.remove(num)
            else:
                pass
        elif op == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.append(num)
    else:
        op = command[0]

        if op == "all":
            S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        elif op == "empty":
            S.clear()
