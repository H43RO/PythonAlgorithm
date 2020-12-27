T = int(input())

list = [[] * (T) for _ in range(T)]

for i in range(T):
    num, string = input().split()
    list[i].append(int(num))
    list[i].append(str(string))

for x in list:
    for s in x[1]:
        print(s * int(x[0]), end='')
    print()