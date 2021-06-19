from sys import stdin

n = int(stdin.readline())
money = list(map(int, stdin.readline().split()))
total = int(stdin.readline())

start = 0
end = max(money)

maximum = 0

# 상한가 탐색을 위한 이분탐색
while start <= end:
    temp = 0
    # 가장 적은 요청 금액과 가장 큰 요청 금액의 중간으로 출발
    mid = (start + end) // 2
    # 예산 각각에 대해서 상한가 치환 뒤 합산 게산
    for x in money:
        if x >= mid:
            temp += mid
        else:
            temp += x
    # 합산을 따져봤을 때, 총 예산보다 크면
    # 상한가를 낮춰서 탐색
    if temp > total:
        end = mid - 1
    # 합산을 따져봤을 때, 총 예산보다 작으면
    # 상한가를 높여서 탐색
    # -> 탐색 마지막 순간에 가장 최적의 상한가를 저장하게 됨
    else:
        maximum = mid
        start = mid + 1

print(maximum)
