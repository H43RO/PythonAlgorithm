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
            for a in candi_key:  # 저장한 후보키들을 하나씩 돌면서
                count = 0
                for num in a:  # 현재 탐색중인 후보키에 포함되는 속성 개수 검사
                    if num in x:
                        count += 1
                if count == len(a):  # 이미 후보키에 등록돼있는 경우 (모든 속성이 이미 존재)
                    available = False

            if not available:  # 최소성 보장을 위해 패스
                continue

            result = []
            for a in x:  # 현재 탐색중인 후보키에 대하여
                temp = []  # Relation 의 각 Row 에서 해당하는 속성 데이터 추출
                for row in relation:
                    temp.append(row[a])
                result.append(temp)

            # result 의 상태 예시
            # - 특정 후보키에 대해서 각 Row 에 어떤 데이터가 담겨있는지 저장 완료
            # [['music', 'math', 'computer', 'computer', 'music', 'music'],
            # ['2', '2', '3', '4', '3', '2']]

            count = []
            for j in range(total):  # 전체 Row 개수 만큼 돌아보며
                temp = []
                for a in result:  # 후보키에 해당하는 데이터 Row 별로 튜플 형태로 정리
                    temp.append(a[j])
                count.append(tuple(temp))
            if len(count) == len(set(count)):  # 만약 중복이 1도 없을 때
                candi_key.append(x)  # 후보키로 저장

    return len(candi_key)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))

# 2019 카카오 블라인드 채용 3번
# 정답률 : 16.09%
# - 40분 소요
