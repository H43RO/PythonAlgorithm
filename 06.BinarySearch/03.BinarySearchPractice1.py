# 떡의 개수와 요청한 떡의 길이 입력
n, m = map(int, input().split(' '))
# 각 떡의 개별 높이 정보를 입력
data = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(data)

# 이진 탐색 수행 (반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in data:
        # 잘랐을 때의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        # 최대한 덜 잘랐을 때가 정답이므로 여기서 Result 에 기록
        result = mid
        start = mid + 1

print(result)

