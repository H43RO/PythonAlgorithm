from sys import stdin

dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
R, C = map(int, stdin.readline().split())

for _ in range(R):
    input_string = stdin.readline().strip()
    # 만약 숫자가 포함되어있지 않다면
    if not any(char.isdigit() for char in input_string):
        continue
    for i in range(C - 1, -1, -1):
        if input_string[i].isdigit():
            dic[input_string[i]] = C - 1 - i
            break

rank = sorted(list(set(dic.values())))

for x in dic.keys():
    print(rank.index(dic[x]) + 1)
