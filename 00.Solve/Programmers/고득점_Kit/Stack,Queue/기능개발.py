from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    # 모든 작업을 배포했을 때 종료
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        temp = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            temp += 1

        if temp >= 1:
            answer.append(temp)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([99, 99, 99], [1, 1, 1]))
print(solution([99, 99, 99, 99, 99], [99, 99, 99, 99, 99]))  # 5
print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]))  # 3, 3
print(solution([1, 99], [99, 1]))  # 2
print(solution([98, 99, 97, 96], [1, 1, 1, 1]))  # 2, 1, 1
