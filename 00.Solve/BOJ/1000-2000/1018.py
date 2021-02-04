from sys import stdin, stdout

white_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

black_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

n, m = map(int, stdin.readline().split())
board = []
min_result = 64  # 최댓값

for _ in range(n):
    board.append(list(stdin.readline().strip()))

for _i in range((n - 8) + 1):
    for _j in range((m - 8) + 1):
        white_count = 0
        black_count = 0
        for i in range(_i, _i + 8):
            for j in range(_j, _j + 8):
                if board[i][j] != white_board[i - _i][j - _j]:
                    white_count += 1
                if board[i][j] != black_board[i - _i][j - _j]:
                    black_count += 1

        count = min(white_count, black_count)
        min_result = min(min_result, count)

print(min_result)