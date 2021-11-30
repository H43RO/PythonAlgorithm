from sys import stdin

n, m = map(int, stdin.readline().split())
store_count = int(stdin.readline())

store_location = [list(map(int, stdin.readline().split())) for _ in range(store_count)]
cur_location = list(map(int, stdin.readline().split()))

result = 0

# 머리 안 좋아서 동근이 위치 동서남북 기준으로 다르게 구현

if cur_location[0] == 1:  # 북
    for direction, distance in store_location:
        if direction == 1:  # 북
            result += abs(cur_location[1] - distance)
        elif direction == 2:  # 남
            left = cur_location[1] + m + distance
            right = (n - cur_location[1]) + m + (n - distance)
            result += min(left, right)
        elif direction == 3:  # 서
            result += cur_location[1] + distance
        elif direction == 4:  # 동
            result += (n - cur_location[1]) + distance

elif cur_location[0] == 2:  # 남
    for direction, distance in store_location:
        if direction == 1:  # 북
            left = cur_location[1] + m + distance
            right = (n - cur_location[1]) + m + (n - distance)
            result += min(left, right)
        elif direction == 2:  # 남
            result += abs(cur_location[1] - distance)
        elif direction == 3:  # 서
            result += cur_location[1] + (m - distance)
        elif direction == 4:  # 동
            result += (n - cur_location[1]) + (m - distance)

elif cur_location[0] == 3:  # 서
    for direction, distance in store_location:
        if direction == 1:  # 북
            result += cur_location[1] + distance
        elif direction == 2:  # 남
            result += (m - cur_location[1]) + distance
        elif direction == 3:  # 서
            result += abs(cur_location[1] - distance)
        elif direction == 4:  # 동
            left = cur_location[1] + n + distance
            right = (m - cur_location[1]) + n + (m - distance)
            result += min(left, right)

elif cur_location[0] == 4:  # 동
    for direction, distance in store_location:
        if direction == 1:  # 북
            result += cur_location[1] + (n - distance)
        elif direction == 2:  # 남
            result += (m - cur_location[1]) + (n - distance)
        elif direction == 3:  # 서
            left = (m - cur_location[1]) + n + (m - distance)
            right = cur_location[1] + n + distance
            result += min(left, right)
        elif direction == 4:  # 동
            result += abs(cur_location[1] - distance)

print(result)
