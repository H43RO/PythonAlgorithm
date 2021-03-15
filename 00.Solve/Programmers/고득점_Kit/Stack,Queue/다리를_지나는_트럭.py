from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    queue = deque(truck_weights)
    on_bridge = deque()

    while queue:

        answer += 1

        # 다리 위의 트럭들을 1 만큼 이동
        for x in on_bridge:
            x[1] += 1

        # 다리 길이만큼 건넜다면 pop() 해줌
        if on_bridge and on_bridge[0][1] == bridge_length:
            on_bridge.popleft()

        truck = queue[0]

        sum_weight = 0

        for x in on_bridge:
            sum_weight += x[0]

        # 만약 트럭을 들여보낼 시 제한 무게, 길이를 넘지 않으면 다리에 올림
        if sum_weight + truck <= weight and len(on_bridge) + 1 <= bridge_length:
            on_bridge.append([queue.popleft(), 0])  # [무게, 다리 얼마나 건넜는지]

        # 만약 제한에 걸리면 다음 루프
        else:
            continue

    while on_bridge:
        answer += 1

        # 다리 위의 트럭들을 1 만큼 이동
        for x in on_bridge:
            x[1] += 1

        # 다리 길이만큼 건넜다면 pop() 해줌
        if on_bridge and on_bridge[0][1] == bridge_length:
            on_bridge.popleft()

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
