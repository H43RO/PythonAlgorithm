# 단지 색깔이 3가지이고 이웃 집과 같은 색이면 안 된다는 조건 뿐이므로 모든 집의 모든 색에 대한 비용을 차례대로 탐색하면서
# 만약 현재 집의 R 에 대한 비용을 탐색하던 중 이전 집이 R 로 색칠되었다면 이전 집의 G, B 에 대한 비용 중 최솟값을
# 현재 집의 R 에 대한 비용에 더해줌으로써, 모든 집의 모든 색에 대한 비용을 고려 가능하고
# 부분 문제의 해결 성질에 따라 맨 마지막 집의 색칠 비용 중 최솟값이 결국 정답이 된다.

def paint(n, houses):
    # 첫 번째 집을 제외한 모든 집에 대하여 모든 색칠 비용을 고려
    for i in range(2, n + 1):
        for x in range(3):
            if x == 0:  # R 을 탐색할 차례에는 이전 집의 G, B 중 최솟값을 더해줌
                houses[i][x] += min(houses[i - 1][1], houses[i - 1][2])
            if x == 1:  # G 를 탐색할 차례에는 이전 집의 R, B 중 최솟값을 더해줌
                houses[i][x] += min(houses[i - 1][0], houses[i - 1][2])
            if x == 2:  # B 를 탐색할 차례에는 이전 집의 R, G 중 최솟값을 더해줌
                houses[i][x] += min(houses[i - 1][0], houses[i - 1][1])

    # 부분 문제의 성질에 따라 마지막 집의 최소 색칠 비용이 곧 정답
    return min(houses[n])


n = int(input())
houses = [[0, 0, 0]]
for i in range(n):
    houses.append(list(map(int, input().split())))

print(paint(n, houses))
