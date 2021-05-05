from sys import stdin, stdout
from collections import deque

# N (다리를 건너는 트럭 수) , W (다리 길이), L (다리의 최대하중)
N, W, L = map(int, stdin.readline().split())

# 트럭의 무게 리스트를 덱 형태로 입력 받음 (앞에서부터 순서대로 출력하기 위해)
truck = deque(list(map(int, stdin.readline().split())))

# 다리를 건너는 상황이기 때문에 양방향 입출력이 가능한 덱 형태를 사용
bridge = deque()
result = 0  # 최단 시간을 담을 변수

# truck 과 bridge 모두 비어있을 때 까지 (모든 트럭이 다 다리를 건널 때 까지)
while truck or bridge:
    result += 1  # 어떤 일이 일어나든 항상 한 턴에 1시간은 증가한다

    for x in bridge:  # 다리 위에 있는 모든 트럭들의 이동 거리를 1씩 늘려줌
        x[1] += 1

    # 만약 가장 선두인 트럭이 다리 길이만큼 이동했을 때 (다 건넜을 때)
    if bridge and bridge[0][1] == W:
        # 가장 선두 트럭을 덱에서 제거함 (이동 완료 상황)
        bridge.popleft()

    if truck:  # 만약 아직 다리에 올라가지 않은 트럭이 남아있다면
        # 지금 다리 위에 올라가있는 트럭의 무게 합을 구함
        sum_weight = sum([x[0] for x in bridge])
        # 만약 지금 트럭 목록 중 가장 앞에 있는 트럭을 다리 위에 올려도
        # 다리의 최대 길이와 다리의 최대 하중을 넘지 않는다면,
        # 트럭 목록의 가장 앞 트럭을 다리 위에 올림
        if sum_weight + truck[0] <= L and len(bridge) + 1 <= W:
            bridge.append([truck.popleft(), 0])
        else:
            continue

print(result)
