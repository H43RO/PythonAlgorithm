n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

result = 0

# B 와 W 의 개수에 차이가 가장 적은 부분으로 잘라내야 다시 칠할 보드의 개수가 적음

for i in range(n):
    board[i] = list(input())
    if board[i].count('W') != board[i].count('B'):
        result += abs(board[i].count('W') - board[i].count('B')) - 1



print(result)



