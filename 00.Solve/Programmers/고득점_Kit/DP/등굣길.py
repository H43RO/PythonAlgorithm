def solution(m, n, puddles):
    # 편의상 경로 값을 모두 0 으로 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    MOD = 1_000_000_007

    dp[1][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 물 웅덩이인 경우 제외
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
