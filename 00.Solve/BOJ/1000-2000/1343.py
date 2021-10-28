from sys import stdin


def greedy(length):
    global result
    if length % 4 == 0 or length % 2 == 0:
        temp = ['AAAA'] * (length // 4)
        temp += ['BB'] * (length % 4 // 2)
        result += temp
        return True
    return False


board = list(stdin.readline().strip())
result = []
length = 0
for i, v in enumerate(board):
    if v == '.':
        if greedy(length):
            length = 0
        else:
            print(-1)
            exit(0)
        result.append('.')
        continue
    length += 1

if greedy(length):
    length = 0
else:
    print(-1)
    exit(0)
print(''.join(result))
