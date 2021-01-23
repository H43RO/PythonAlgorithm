from itertools import combinations
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

city = []
chicken_list = []
distance = []

for i in range(n):
    street = list(map(int, stdin.readline().split()))

    # 치킨집이 있다면 치킨집 리스트에 인덱스 정보를 넣어둠
    for index, value in enumerate(street):
        if value == 2:
            chicken_list.append([i, index])

    city.append(street)

# 폐업시키지않을 최대 M 개의 치킨집 선택 (조합)
chicken_choice = list(combinations(chicken_list, m))

# 치킨집 한개 고르는 상황에선 잘 동작함
# 여러 개 고르는 상황에서 오동작

for x in chicken_choice:
    final_distance = []
    # 도시 전체 탐색
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                # 가장 가까운 치킨집과의 거리 저장
                temp_distance = []
                for chicken in x:
                    temp_distance.append(abs(i - chicken[0]) + abs(j - chicken[1]))
                final_distance.append(min(temp_distance))
    distance.append(sum(final_distance))

print(sorted(distance)[0])
