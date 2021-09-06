from itertools import combinations


def solution(relation):
    total = len(relation)  # 튜플 (레코드) 개수
    column = len(relation[0])  # 속성 개수

    candi_key = []

    # 최소성 보장을 위해 최소 후보키부터 유일성 만족하는 키 탐색
    for i in range(1, column + 1):
        for x in list(combinations(range(column), i)):
            # 최소성 보장 되는지
            available = True
            for a in candi_key:
                count = 0
                for num in a:
                    if num in x:
                        count += 1
                if count == len(a):
                    available = False

            if not available:
                continue

            result = []
            for a in x:
                temp = []
                for row in relation:
                    temp.append(row[a])
                result.append(temp)
            count = []

            for j in range(total):
                temp = []
                for a in result:
                    temp.append(a[j])
                count.append(tuple(temp))
            if len(count) == len(set(count)):
                candi_key.append(x)

    return len(candi_key)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))

# 2019 카카오 블라인드 채용 3번
# 정답률 : 16.09%
# - 40분 소요
