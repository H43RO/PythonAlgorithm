from sys import stdin

# 옵티멀 아이디어 : 0을 1로 모두 바꾸는 상황과 1을 0으로 모두 바꾸는 상황 비교

convert_1_to_0 = 0
convert_0_to_1 = 0

data = list(map(int, stdin.readline().strip()))
for i, v in enumerate(data):
    # 연속된 시퀀스는 한 번 뒤집은걸로 간주하는 로직이 필요함 -> data[i - 1] != data[i]
    if v == 0 and (i == 0 or data[i - 1] != data[i]):  # 0을 1로 바꾸는 상황
        convert_0_to_1 += 1
    if v == 1 and (i == 0 or data[i - 1] != data[i]):  # 1을 0으로 바꾸는 상황
        convert_1_to_0 += 1

print(min(convert_1_to_0, convert_0_to_1))
