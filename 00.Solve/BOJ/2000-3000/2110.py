from sys import stdin

n, c = map(int, stdin.readline().split())
house = sorted([int(stdin.readline()) for _ in range(n)])

# 공유기 간 거리를 파라메트릭 서치
start, end = 1, house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    count = 1  # 모든 집을 커버하기 위해 필요한 공유기의 총 개수
    current = house[0]

    for i in range(1, n):
        if current + mid <= house[i]:  # 다음 집까지 커버리지가 안 닿는다면
            current = house[i]
            count += 1  # 공유기 1개 증설

    if count >= c:  # 만약 공유기를 C 보다 많이 설치했다면 거리가 너무 짧은 것이므로
        start = mid + 1  # 오른쪽으로 탐색 범위 좁힘
        result = mid
    else:  # 만약 공유기 개수가 적다면 거리가 너무 먼 것이므로
        end = mid - 1  # 왼쪽으로 탐색 범위 좁힘

print(result)
