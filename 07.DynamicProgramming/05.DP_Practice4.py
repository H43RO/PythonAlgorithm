
for case in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = [data[i * m:(i + 1) * m] for i in range((len(data) - 1 + m) // m)]

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:  # 첫 번째 금광은 왼쪽 위가 없음
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1:  # 마지막 금광은 왼쪽 아래가 없음
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]

            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
