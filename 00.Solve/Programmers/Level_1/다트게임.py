def solution(dartResult):
    score = []
    for i, x in enumerate(dartResult):
        if x == '*':
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
        if x == '#':
            score[-1] *= -1

        if x.isalpha():
            temp = int(dartResult[i - 1])
            if dartResult[i - 2] == '1' and dartResult[i - 1] == '0':
                temp = 10
            if x == 'S':
                score.append(temp)
            if x == 'D':
                score.append(temp ** 2)
            if x == 'T':
                score.append(temp ** 3)

    return sum(score)
