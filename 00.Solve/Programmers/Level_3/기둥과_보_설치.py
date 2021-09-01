import copy


def check(pillar, panel):
    for x, y in pillar:
        if y == 0 or (x - 1, y) in panel or (x, y) in panel or (x, y - 1) in pillar:
            continue
        else:
            return False
    for x, y in panel:
        if (x, y - 1) in pillar or (x + 1, y - 1) in pillar or ((x - 1, y) in panel and (x + 1, y) in panel):
            continue
        else:
            return False
    return True


def solution(n, build_frame):
    answer = []

    pillar = []
    panel = []

    for build in build_frame:
        x, y, a, b = build

        if b == 1:  # 설치
            if a == 0:  # 기둥
                temp = copy.deepcopy(pillar)
                temp.append((x, y))
                if check(temp, panel):
                    pillar.append((x, y))
            elif a == 1:  # 보
                temp = copy.deepcopy(panel)
                temp.append((x, y))
                if check(pillar, temp):
                    panel.append((x, y))
        elif b == 0:  # 삭제
            if a == 0:  # 기둥
                temp = copy.deepcopy(pillar)
                temp.remove((x, y))
                if check(temp, panel):
                    pillar.remove((x, y))
            elif a == 1:  # 보
                temp = copy.deepcopy(panel)
                temp.remove((x, y))
                if check(pillar, temp):
                    panel.remove((x, y))

    for x in pillar:
        answer.append([x[0], x[1], 0])
    for x in panel:
        answer.append([x[0], x[1], 1])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

# 2020 카카오 블라인드 공채 5번
# 정답률 : 1.9%
# - 1시간 25분
