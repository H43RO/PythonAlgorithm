import math
from sys import stdin

n, m = map(int, stdin.readline().split())
jewel = [int(stdin.readline()) for _ in range(m)]

start = 1
end = max(jewel)

result = 0

# 최소 질투심에 대한 파라메트릭 서치
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for x in jewel:  # 각 색상별 보석 개수를 인원수대로 나눠보기
        temp += math.ceil(x / mid)

    # 만약 N 보다 크다면 N 명보다 더 많은 사람이 보석을 가져갔다는 건데
    # 이는 문제 조건에 위반되기 때문에 질투심을 더 높여야 함
    # * 즉, 한 명이 가져가는 보석 개수를 늘려야 함
    if temp > n:
        start = mid + 1
    else:  # N 보다 작거나 같은 사람이 보석을 가져간 경우 결과 저장
        result = mid
        end = mid - 1

print(result)
