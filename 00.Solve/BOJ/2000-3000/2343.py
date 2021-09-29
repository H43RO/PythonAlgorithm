from sys import stdin

n, m = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

# 블루레이 크기 파라메트릭 서치
start, end = max(data), sum(data)
result = end

while start <= end:
    mid = (start + end) // 2  # 블루레이 크기

    count = 1  # 블루레이 개수
    temp = 0

    for x in data:  # 각 강의 길이 탐색
        if x > mid:  # 만약 블루레이 크기보다 크다면 종료
            break
        if temp + x > mid:  # 한 블루레이 다 채웠으면
            count += 1  # 블루레이 개수 1 증가
            temp = x
        else:  # 아직 블루레이 1개가 다 안 채워진 경우
            temp += x  # 블루레이 채우기

    if count <= m:  # 블루레이 크기가 M 이하라면 길이가 충분히 긴 것이므로
        end = mid - 1  # 탐색범위 왼쪽으로 좁힘
        result = mid  # 결과 저장
    else:  # 블루레이 크기가 M 초과라면 길이가 너무 짧은 것이므로
        start = mid + 1  # 탐색범위 오른쪽으로 좁힙

print(result)
