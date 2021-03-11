def solution(participant, completion):
    answer = ''
    data = dict()
    for x in participant:
        if x in data:
            data[x] += 1
        else:
            data[x] = 1

    for x in completion:
        data[x] -= 1

    for key, value in zip(data.keys(), data.values()):
        if value != 0:
            return key


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

