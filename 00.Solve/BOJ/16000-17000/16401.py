from sys import stdin

m, n = map(int, stdin.readline().split())
snack = list(map(int, stdin.readline().split()))

start = 1
end = max(snack)

length = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    # 잘라낼 수 있는 과자 개수 계산
    for x in snack:
        count += (x // mid)
    # 잘라낼 수 있는 과자 개수가 조카 수 이상이라면
    # 조건 만족, 탐색 구역 오른쪽으로 하여 더 긴 길이 탐색해봄
    if count >= m:
        length = mid
        start = mid + 1
    # 조건 불만족 시에는, 탐색 범위 왼쪽으로 이동하여
    # 더 적은 길이만큼 잘라내볼 수 있게 함
    else:
        end = mid - 1

print(length)
