def solve(n, data):
    # 삼각형의 1 층에서 부터 Bottom - up 으로 탐색
    for i in range(1, len(data)):
        # 각 층의 모든 정수에 대하여 고려
        for j in range(len(data[i])):
            # 이전 층의 대각선 왼쪽, 대각선 오른쪽 원소 중 최댓값을 현재 원소에 더해줌
            data[i][j] += max(data[i - 1][j], data[i - 1][j + 1])

    # 이렇게 하면 삼각형의 꼭대기 (n - 1층) 에 최댓값이 저장되어 있음
    return data[n - 1][0]


n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

# Bottom - Up
data.reverse()

print(solve(n, data))
