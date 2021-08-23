from collections import defaultdict
import bisect


def solution(info, query):
    answer = []
    people = defaultdict(list)
    for x in info:
        lang, part, career, food, score = x.split()

        for a in [lang, "-"]:
            for b in [part, "-"]:
                for c in [career, "-"]:
                    for d in [food, "-"]:
                        people[(a, b, c, d)].append(int(score))

    for key in people.keys():
        people[key].sort()  # 코테 점수 오름차순 정렬

    for i, v in enumerate(query):
        lang, part, career, food_score = v.split(" and ")
        food, score = food_score.split()

        score = int(score)
        temp = people[(lang, part, career, food)]
        start = bisect.bisect_left(temp, score)
        answer.append(len(temp) - start)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
))
