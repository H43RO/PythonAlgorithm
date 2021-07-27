from itertools import combinations
from sys import stdin, maxsize

n, m = map(int, stdin.readline().split())

city = []
house_list = []
chicken_list = []
distance = []

for i in range(n):
    street = list(map(int, stdin.readline().split()))
    # 가정집, 치킨집 좌표(인덱스)를 저장
    for index, value in enumerate(street):
        if value == 1:
            house_list.append((i, index))
        if value == 2:
            chicken_list.append((i, index))
    city.append(street)

# 폐업시키지않을 최대 M 개의 치킨집 선택 (조합)
chicken_choice = list(combinations(chicken_list, m))

for x in chicken_choice:
    whole_chicken_distance = []

    for house in house_list:
        # 가장 가까운 치킨집과의 거리 저장
        chicken_distance = maxsize
        for chicken in x:
            chicken_distance = min(chicken_distance, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        whole_chicken_distance.append(chicken_distance)

    distance.append(sum(whole_chicken_distance))

print(min(distance))
