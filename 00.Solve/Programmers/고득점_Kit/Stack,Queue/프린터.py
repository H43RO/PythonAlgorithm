from collections import deque
import itertools


def solution(priorities, location):
    answer = 0
    data = deque()

    for i, v in enumerate(priorities):
        data.append((v, i))

    while True and len(data) > 1:
        temp = priorities[1:]
        if data[0][0] < max(temp):
            data.append(data.popleft())
            priorities.append(priorities[0])
            del priorities[0]
        else:
            answer += 1
            x = data.popleft()
            del priorities[0]
            if x[1] == location:
                break

    if len(data) == 1 and data[0][1] == location:
        return answer + 1

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
