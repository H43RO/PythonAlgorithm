n, m = map(int, input().split())
# 나무 길이 정보 입력
data = list(map(int, input().split()))

# 이분 탐색 start, end 정의
start = 0
end = max(data)
result = 0

# 모든 구간에 대하여 탐색
while start <= end:
    mid = (start + end) // 2

    # 현재 절단기 높이 (mid) 에 의해 잘려진 나무 길이 총합 계산
    total = sum([x - mid if x >= mid else 0 for x in data])

    # 만약 잘려진 나무 길이 총합이 요구조건보다 부족하다면
    if total < m:
        # 절단기 높이를 낮추기 위해 end 를 mid - 1 로 변경
        end = mid - 1

    # 만약 잘려진 나무 길이 총합이 요구조건 이상이라면
    else:
        # 결과값 저장하고 더 나은 답안이 있을 수 있으니 start 를 mid + 1 로 지정
        result = mid
        start = mid + 1

print(result)
