from sys import stdin, stdout
from collections import deque

# N (다리를 건너는 트럭 수) , W (다리 길이), L (다리의 최대하중)
N, W, L = map(int, stdin.readline().split())
truck = deque(list(map(int, stdin.readline().split())))

bridge = deque()
result = 0

while truck or bridge:
    result += 1

    for x in bridge:
        x[1] += 1

    if bridge and bridge[0][1] == W:
        bridge.popleft()

    if truck:
        sum_weight = 0

        for x in bridge:
            sum_weight += x[0]

        if sum_weight + truck[0] <= L and len(bridge) + 1 <= W:
            bridge.append([truck.popleft(), 0])
        else:
            continue

print(result)
