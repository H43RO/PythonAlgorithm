from sys import stdin, setrecursionlimit

setrecursionlimit(10000)


def solve(n, x, y, cnt):
    if n == 1:
        if x == r and y == c:
            return cnt
        elif x == r and y + 1 == c:
            return cnt + 1
        elif x + 1 == r and y == c:
            return cnt + 2
        else:
            return cnt + 3
    else:
        if x + 2 ** (n - 1) > r:
            if y + 2 ** (n - 1) > c:
                # 1 사분면으로 이동
                return solve(n - 1, x, y, cnt)
            else:
                # 2 사분면으로 이동
                return solve(n - 1, x, y + 2 ** (n - 1), cnt + 2 ** (2 * n - 2))
        else:
            if y + 2 ** (n - 1) > c:
                # 3 사분면으로 이동
                return solve(n - 1, x + 2 ** (n - 1), y, cnt + 2 * 2 ** (2 * n - 2))
            else:
                # 4 사분면으로 이동
                return solve(n - 1, x + 2 ** (n - 1), y + 2 ** (n - 1), cnt + 3 * 2 ** (2 * n - 2))


n, r, c = map(int, stdin.readline().split())
result = solve(n, 0, 0, 0)
print(result)
