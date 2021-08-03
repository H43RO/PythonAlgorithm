from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
durability = deque(list(map(int, stdin.readline().split())))
robot = deque([0] * n)

count = 0

while durability.count(0) < k:  # 내구도가 0인 칸 개수가 K 개 이상이라면 종료
    count += 1  # 단계 1 증가

    robot.pop()
    robot.appendleft(0)
    robot[n - 1] = 0

    durability.appendleft(durability.pop())

    for i in range(n - 2, 0, -1):
        if robot[i] and not robot[i + 1] and durability[i + 1]:
            robot[i] = 0
            robot[i + 1] = 1
            durability[i + 1] = max(0, durability[i + 1] - 1)

    if not robot[0] and durability[0]:
        robot[0] = 1
        durability[0] = max(0, durability[0] - 1)

print(count)
