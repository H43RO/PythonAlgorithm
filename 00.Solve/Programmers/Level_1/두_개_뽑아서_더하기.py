from itertools import combinations


def solution(numbers):
    answer = []

    data = list(combinations(numbers, 2))
    for x in data:
        answer.append(sum(x))

    answer = set(answer)
    answer = sorted(list(answer))

    return answer


print(solution([2, 1, 3, 4, 1]))