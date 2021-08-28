def solution(N, stages):
    answer = []

    data = []
    for i in range(1, N + 1):
        challenge = 0
        not_yet = 0
        for x in stages:
            if x >= i:
                challenge += 1
            if x == i:
                not_yet += 1
        data.append((not_yet / challenge, i))

    data.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    [answer.append(x[1]) for x in data]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
