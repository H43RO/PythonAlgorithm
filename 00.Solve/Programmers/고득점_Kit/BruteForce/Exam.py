def solution(answers):
    answer = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score_1 = 0
    score_2 = 0
    score_3 = 0

    for i, v in enumerate(answers):
        if pattern_1[i % 5] == v:
            score_1 += 1
        if pattern_2[i % 8] == v:
            score_2 += 1
        if pattern_3[i % 10] == v:
            score_3 += 1

    if max(score_1, score_2, score_3) == score_1:
        answer.append(1)
        if score_1 == score_2:
            answer.append(2)
        if score_1 == score_3:
            answer.append(3)
        return answer

    if max(score_1, score_2, score_3) == score_2:
        answer.append(2)
        if score_2 == score_3:
            answer.append(3)
        return answer

    if max(score_1, score_2, score_3) == score_3:
        answer.append(3)
        return answer

    return answer