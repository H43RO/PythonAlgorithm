from sys import stdin, maxsize

n, m = map(int, stdin.readline().split())

data = [int(stdin.readline()) for _ in range(n)]

start = 0
end = maxsize
result = maxsize

while start <= end:
    mid = (start + end) // 2  # 인출할 금액

    money = mid  # 현재 가진 돈 저장 (첫 인출)
    count = 1  # 인출 횟수 저장 (첫 인출 했으므로 1)

    for x in data:  # 사용 계획 탐색
        if mid < x:  # 출금을 해도 모자란 경우는 불가능 처리
            count = m + 1
            break
        if money < x:  # 만약 가진 돈이 부족하다면 돈 인출
            money = mid
            count += 1  # 인출 횟수 증가
        money -= x  # 충분하면 그대로 사용

    if count > m:  # 인출 횟수 초과
        start = mid + 1  # 범위 뒤로 빼서 탐색 (mid 를 늘려보기)
    else:
        end = mid - 1  # 충분했다면 범위를 앞으로 빼서 탐색 (mid 를 최소화해보기)
        result = min(result, mid)

print(result)
