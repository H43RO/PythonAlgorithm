def solution(n, lost, reserve):
    common = set(lost).intersection(reserve)

    for x in common:
        reserve.pop(reserve.index(x))
        lost.pop(lost.index(x))

    answer = n - len(lost)

    for x in lost:
        if x - 1 in reserve:
            answer += 1
            reserve.pop(reserve.index(x - 1))
            continue

        if x + 1 in reserve:
            answer += 1
            reserve.pop(reserve.index(x + 1))

    return answer
