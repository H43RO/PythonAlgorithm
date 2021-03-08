def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag


def n_queens(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)


"""
    N-Queens 경우의 수를 고려하고자 백 트래킹을 활용할 때,
    col 이라는 리스트는 각 Column 의 Queen 의 위치를 의미함.
    
    예를들어 4 X 4 체스판에서의 N-Queens 문제일 때
    col 리스트가 [2, 4, 3, 1] 이라고 되어있다면
    첫 번째 행의 2번째 열에 하나,
    두 번째 행의 4번째 열에 하나,
    세 번째 행의 3번째 열에 하나,
    네 번째 행의 1번째 열에 하나씩 퀸이 배치되어 있는 것이다.
"""

n = int(input())
col = [0] * (n + 1)
n_queens(0, col)
