from sys import stdin
from collections import deque


def rotate(number, direction, visited):
    visited[number] = True

    if number != 1:  # 2, 3, 4 번 기어
        if (gear[number][6] != gear[number - 1][2]) and not visited[number - 1]:
            rotate(number - 1, direction * -1, visited)
    if number != 4:  # 1, 2, 3 번 기어
        if (gear[number][2] != gear[number + 1][6]) and not visited[number + 1]:
            rotate(number + 1, direction * -1, visited)

    if direction == 1:  # 시계 방향 회전
        gear[number].appendleft(gear[number].pop())
    else:  # 반시계 방향 회전
        gear[number].append(gear[number].popleft())


gear = {}
for i in range(1, 5):
    gear[i] = deque(list(map(int, stdin.readline().strip())))

k = int(stdin.readline())

for _ in range(k):
    visited = [False] * 5  # 편의상 0번 인덱스 사용 X
    gear_number, direction = map(int, stdin.readline().split())
    rotate(gear_number, direction, visited)

result = 0
for i in range(4):
    result += (gear[i + 1][0] * (2 ** i))
print(result)
