from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([], maxlen=cacheSize)  # 캐시 (덱) 최대 크기 지정 가능

    for x in cities:
        city = x.lower()  # 대소문자 구분 X (이 조건 놓쳐서 한 번 오답 받음)
        if city in cache:  # 캐시 히트
            answer += 1
            cache.remove(city)  # 맨 앞으로 옮겨주기 위해서 삭제
        else:  # 캐시 미스
            answer += 5
        cache.appendleft(city)
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 2018 카카오 블라인드 공채 1번
# 정답률 : 45.26%
# - 9분 소요
