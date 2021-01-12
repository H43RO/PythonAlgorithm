def paint(n, houses):
    for i in range(2, n + 1):
        for x in range(3):
            if x == 0:
                houses[i][x] += min(houses[i - 1][1], houses[i - 1][2])
            if x == 1:
                houses[i][x] += min(houses[i - 1][0], houses[i - 1][2])
            if x == 2:
                houses[i][x] += min(houses[i - 1][0], houses[i - 1][1])

    return min(houses[n])


n = int(input())
houses = []

houses.append([0, 0, 0])
for i in range(n):
    houses.append(list(map(int, input().split())))

print(paint(n, houses))
