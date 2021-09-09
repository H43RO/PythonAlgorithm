def solution(N, stages):
    answer = []

    data = []
    # 각 스테이지 별로 클리어 못 한 사람, 클리어 한 사람 구하기
    for i in range(1, N + 1):
        clear = 0
        not_yet = 0
        for x in stages:
            if x >= i:  # 클리어 한 플레이어
                clear += 1
            if x == i:  # 아직 클리어 못 한 플레이어
                not_yet += 1
        # 실패율 : (스테이지에 도달했으나 아직 클리어 못한 녀석 수) / (스테이지에 도달한 녀석 수)
        data.append((not_yet / clear, i))

    # 실패율 내림차순 정렬 (만약 실패율이 같을 경우 작은 번호 스테이지가 먼저 출력)
    data.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    [answer.append(x[1]) for x in data]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

# 정답률
# - 5분 소요
