from collections import defaultdict
import bisect


def solution(info, query):
    answer = []
    people = defaultdict(list)  # 기본 Value 를 list 로 가짐
    for x in info:
        lang, part, career, food, score = x.split()

        # 가능한 모든 하위 조건에 대하여 데이터 생성
        for a in (lang, "-"):
            for b in (part, "-"):
                for c in (career, "-"):
                    for d in (food, "-"):
                        people[(a, b, c, d)].append(int(score))

    for key in people.keys():
        people[key].sort()  # 코테 점수 오름차순 정렬

    for x in query:
        lang, part, career, food_score = x.split(" and ")
        food, score = food_score.split()

        score = int(score)
        temp = people[(lang, part, career, food)]  # 조건 만족하는 사람 목록 가져옴
        start = bisect.bisect_left(temp, score)  # 이분탐색으로 코테 커트라인 내 꼴등 인덱스 구함
        answer.append(len(temp) - start)  # 총 커트라인 합격자 수

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
))
