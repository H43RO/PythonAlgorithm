from sys import stdin

w, h = map(int, stdin.readline().split())
n = int(stdin.readline())

store_location = [list(map(int, stdin.readline().split())) for _ in range(n)]
my_location = list(map(int, stdin.readline().split()))

result = 0

if my_location[0] == 1:  # 북
    for d, l in store_location:
        if d == 1:
            result += abs(my_location[1] - l)
        elif d == 2:
            left = my_location[1] + h + l
            right = (w - my_location[1]) + h + (w - l)
            result += min(left, right)
        elif d == 3:
            result += my_location[1] + l
        elif d == 4:
            result += (w - my_location[1]) + l

elif my_location[0] == 2:  # 남
    for d, l in store_location:
        if d == 1:
            left = my_location[1] + h + l
            right = (w - my_location[1]) + h + (w - l)
            result += min(left, right)
        elif d == 2:
            result += abs(my_location[1] - l)
        elif d == 3:
            result += my_location[1] + (h - l)
        elif d == 4:
            result += (w - my_location[1]) + (h - l)

elif my_location[0] == 3:  # 서
    for d, l in store_location:
        if d == 1:
            result += my_location[1] + l
        elif d == 2:
            result += (h - my_location[1]) + l
        elif d == 3:
            result += abs(my_location[1] - l)
        elif d == 4:
            left = my_location[1] + w + l
            right = (h - my_location[1]) + w + (h - l)
            result += min(left, right)

elif my_location[0] == 4:  # 동
    for d, l in store_location:
        if d == 1:
            result += my_location[1] + (w - l)
        elif d == 2:
            result += (h - my_location[1]) + (w - l)
        elif d == 3:
            left = (h - my_location[1]) + w + (h - l)
            right = my_location[1] + w + l
            result += min(left, right)
        elif d == 4:
            result += abs(my_location[1] - l)

print(result)
