# 랜선의 개수와 요청한 랜선의 개수 입력
k, n = map(int, input().split(' '))
# 각 랜선의 개별 높이 정보를 입력
data = []
for _ in range(k):
    data.append(int(input()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(data)

# 이진 탐색 수행
result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for x in data:
        if x >= mid > 0:
            # 랜선이 기준 길이보다 큰 경우
            # 기준 길이로 쪼갤 수 있는 만큼 개수 증가
            count += (x // mid)
    # 랜선 개수가 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if count < n:
        end = mid - 1
    # 랜선 개수가 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        # 최대한 덜 자르는 기준 길이가 정답이므로 Result 에 기록
        result = mid
        start = mid + 1

print(result)
