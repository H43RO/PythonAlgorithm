from sys import stdin

n, m = map(int, stdin.readline().split())
times = [int(stdin.readline()) for _ in range(n)]

start = 1
end = times[-1] * m

result = 0

while start <= end:
    mid = (start + end) // 2

    temp = 0
    # 각 심사대 최대 수용 가능 인원 추가
    for x in times:
        temp += mid // x

    # M 명 이상 수용 가능하다면
    # 조건 만족, 탐색 범위 왼쪽으로 하여 더 작은 시간 탐색
    if temp >= m:
        end = mid - 1
        result = mid
    # 조건 불만족 시에는, 탐색 범위 오른쪽으로 하여
    # 더 긴 시간 탐색
    else:
        start = mid + 1

print(result)
