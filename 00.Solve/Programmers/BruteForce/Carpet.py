from collections import deque


def solution(brown, yellow):
    answer = []
    measure = deque()

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            measure.append(i)

    while measure:
        if len(measure) == 1:
            a = measure.pop()
            answer = [a + 2, a + 2]
        else:
            a = measure.pop()
            b = measure.popleft()

            if (a + 2) * 2 + (b * 2) == brown:
                answer = [a + 2, b + 2]
                break

    return answer


print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]
print(solution(50, 22))  # [24, 3]
