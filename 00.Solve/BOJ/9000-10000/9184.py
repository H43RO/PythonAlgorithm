# 어차피 음수로 떨어지면 1을 반환하고, 20을 넘어가면 20으로 고정하기 때문에
# 3차원 DP Table 최대 Range 는 21로 지정해주면 됨
# Memoization 기법 사용

dp = [[[0] * 21 for _ in range(21)] for __ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    result = w(a, b, c)

    print(f"w({a}, {b}, {c}) = {result}")
