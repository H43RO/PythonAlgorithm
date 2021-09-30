from sys import stdin

n = int(stdin.readline())
data = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
card = list(map(int, stdin.readline().split()))

for x in card:
    found = False  # 숫자가 발견됐는 지 여부 저장
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == x:  # 만약 타겟 데이터를 발견했다면 종료
            found = True
            break
        if data[mid] > x:
            end = mid - 1
        if data[mid] < x:
            start = mid + 1

    print(1 if found else 0, end=' ')  # 숫자 발견했으면 1, 아니면 0 출력
