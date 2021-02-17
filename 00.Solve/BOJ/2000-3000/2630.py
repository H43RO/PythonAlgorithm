from sys import stdin, stdout

WHITE = 0
BLUE = 1


def cut(n, x, y):
    global paper
    global white
    global blue

    white_count = 0
    blue_count = 0

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] == WHITE:
                white_count += 1
            if paper[i][j] == BLUE:
                blue_count += 1

    if white_count == 0:
        blue += 1
    elif blue_count == 0:
        white += 1
    else:
        cut(n // 2, x, y)
        cut(n // 2, x + n // 2, y)
        cut(n // 2, x, y + n // 2)
        cut(n // 2, x + n // 2, y + n // 2)


paper = []
white = 0
blue = 0

n = int(stdin.readline().strip())

for _ in range(n):
    paper.append(list(map(int, stdin.readline().split())))

cut(n, 0, 0)

print(white)
print(blue)
