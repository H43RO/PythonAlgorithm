n = int(input())  # 공간의 크기
operation = input().split()

x = 1
y = 1

for command in operation:
    if command == 'L' and y != 1:
        y -= 1
    if command == 'R' and y != n:
        y += 1
    if command == 'U' and x != 1:
        x -= 1
    if command == 'D' and x != n:
        x += 1

print(x, y)


# 교재 정답

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)