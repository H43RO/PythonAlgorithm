from sys import stdin

n, m = map(int, stdin.readline().split())
data = [list(map(int, stdin.readline().split())) for _ in range(n)]

"""
맨 윗줄, 왼쪽 줄 먼저 DP 테이블 채워넣기
"""
for i in range(1, m):
    data[0][i] += data[0][i - 1]
for i in range(1, n):
    data[i][0] += data[i - 1][0]

"""
나머지 칸에 대해서 위에서 아래로 내려오는 상황과 
왼쪽에서 오른쪽으로 오는 상황 고려 (대각선은 항상 손해임)
"""
for i in range(1, n):
    for j in range(1, m):
        data[i][j] += max(data[i - 1][j], data[i][j - 1])

print(data[n - 1][m - 1])
