# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하기
# 단, 보트에는 두명만 탈 수 있음!!

from collections import deque


def solution(people, limit):
    answer = 0

    # 역순 정렬
    people = deque(sorted(people, reverse=True))

    while people:
        # 남은 여유 무게 계산
        limit_left = limit - people.popleft()
        # 맨 뒤 사람이 여유 무게 이내 몸무게일 때
        if len(people) >= 1 and people[-1] <= limit_left:
            people.pop()
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
