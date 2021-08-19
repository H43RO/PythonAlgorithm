from sys import stdin

N, L = map(int, stdin.readline().split())
water = sorted(list(map(int, stdin.readline().split())))  # 물이 새는 곳의 위치 (정렬됨)

start = water[0]  # 처음 물 새는 곳부터 테이핑
end = start + L - 1  # L - 1 (좌우 0.5 합산) 만큼 커버 가능

result = 1
for x in water:  # 물 새는 위치 다 돌아보기
    if start <= x <= end:  # 만약 커버 가능한 곳이라면 스킵
        continue
    start = x  # 커버 불가능하면 테이프 하나 더 사용
    end = start + L - 1  # 마찬가지로 L - 1 만큼 커버 가능
    result += 1  # 테이프 개수 1 증가

print(result)
