# 완전 탐색으로 해결 가능 (Brute Force)

location = list(input())
y, x = ord(location[0]), int(location[1])

x_map = [1, 2, 3, 4, 5, 6, 7, 8]
y_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

result = 0

if x - 2 in x_map:
    if chr(y - 1) in y_map:
        result += 1
    if chr(y + 1) in y_map:
        result += 1
if x - 1 in x_map:
    if chr(y - 2) in y_map:
        result += 1
    if chr(y + 2) in y_map:
        result += 1
if x + 1 in x_map:
    if chr(y - 2) in y_map:
        result += 1
    if chr(y + 2) in y_map:
        result += 1
if x + 2 in x_map:
    if chr(y - 1) in y_map:
        result += 1
    if chr(y + 1) in y_map:
        result += 1

print(result)

# 교재 정답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)