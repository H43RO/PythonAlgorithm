def is_promising(x):
    for i in range(1, x):
        # 행, 열, 대각선 중 경로가 겹치는 퀸이 발견되면 non-promising 한 것
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True


def n_queens(count):
    global result
    if count > n:
        result += 1
    else:
        for i in range(1, n + 1):
            col[count] = i
            if is_promising(count):
                n_queens(count + 1)


n = int(input())
result = 0
col = [0] * (n + 1)
n_queens(1)

print(result)
