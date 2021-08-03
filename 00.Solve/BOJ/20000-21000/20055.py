from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
durability = deque(list(map(int, stdin.readline().split())))  # 벨트 (내구도)
robot = deque([False] * n)  # 각 칸에 로봇이 있는지 없는지 저장

count = 0

while durability.count(0) < k:  # 내구도가 0인 칸 개수가 K 개 이상이라면 종료
    count += 1  # 단계 1 증가

    # 로봇, 벨트 한 칸 회전
    robot.pop()
    robot.appendleft(False)
    robot[-1] = False  # 로봇이 내리는 위치 (N) 도달하면 즉시 내림
    durability.appendleft(durability.pop())

    for i in range(n - 2, 0, -1):  # 가장 먼저 올라간 로봇부터, 벨트가 회전하는 방향으로
        if robot[i] and not robot[i + 1] and durability[i + 1]:  # 한 칸 이동할 수 있는 조건이라면
            robot[i] = False                                     # 이동을 해준다
            robot[i + 1] = True
            durability[i + 1] = max(0, durability[i + 1] - 1)    # 이후 해당 칸의 내구도를 줄임 (음수 방지)

    if durability[0]:  # 올리는 위치 칸 내구도가 0이 아니라면 새로운 로봇 올림
        robot[0] = True
        durability[0] = max(0, durability[0] - 1)  # 이후 해당 칸의 내구도를 줄임 (음수 방지)

print(count)
