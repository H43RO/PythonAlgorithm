from sys import stdin

convert_1_to_0 = 0
convert_0_to_1 = 0

data = list(map(int, stdin.readline().strip()))
for i, v in enumerate(data):
    if v == 0 and (i == 0 or data[i - 1] != data[i]):
        convert_0_to_1 += 1
    if v == 1 and (i == 0 or data[i - 1] != data[i]):
        convert_1_to_0 += 1

print(min(convert_1_to_0, convert_0_to_1))
